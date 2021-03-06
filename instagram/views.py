# -  *  - coding:utf-8 -  *  - 
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Image, PhotosLetterRecipients
from .forms import PhotosLetterForm, NewImageForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
# Create your views here.
# def welcome(request):
#     return render(request, 'all-photos/today-photos.html',  {"date":date, })

@login_required(login_url = '/accounts/login/')
def photos_today(request):
	date = dt.date.today()
	all_images = Image.all_images()
	images = Image.objects.all()
	print(images)
# image = Image.today - photos()
	if request.method == 'POST':
		form = PhotosLetterForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']

			recipient = PhotosLetterRecipients(name = name, email = email)
			recipient.save()
			send_welcome_email(name, email)

			HttpResponseRedirect('photos_today')
	else:
		form = PhotosLetterForm()
		form = NewImageForm()
	return render(request, 'all-photos/today-photos.html',  {"date":date, "letterForm":form, "ImageForm":form, "images":all_images})


def past_days_photos(request, past_date):

	try:
	# Converts data from the string Url
			date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
	except ValueError:
	# Raise 404 error when ValueError is thrown
		raise Http404()
		assert False

		if date == dt.date.today():
			return redirect(photos_today)

	photos = Image.days_photos(date)
	return render(request, 'all-photos/past-photos.html',  {"date":date, "photos":photos})

def search_results(request):

	if 'image' in request.GET and request.GET["image"]:
			search_term = request.GET.get("image")
			searched_images = Image.search_by_name(search_term)
			message = f"{search_term}"

			return render(request, 'all-photos/search.html',  {"message":message, "images":searched_images})

	else:
		message = "You haven't searched for any term"
	return render(request, 'all-photos/search.html',  {"message":message})

@login_required(login_url = '/accounts/login/')
def image(request, image_id):
	try:
		image = Image.objects.get(id = image_id)
	except DoesNotExist:
		raise Http404()
	return render(request, "all-photos/image.html",  {"image":image})

@login_required(login_url = '/accounts/login/')
def new_image(request):
	current_user = request.user
	title = 'New image'
	if request.method == 'POST':
		form = NewImageForm(request.POST, request.FILES)
		if form.is_valid():
			image = form.save(commit = False)
			image.user = current_user
			image.save()
		return redirect('photosToday')

	else:
		form = NewImageForm()
	return render(request, 'new_image.html',  {"form":form, "current_user":current_user, "title":title})

@login_required(login_url = '/accounts/login/')
def comment(request, id):
	
	post = get_object_or_404(Image, id = id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit = False)
			comment.user = current_user
			comment.image = post
			comment.save()
			return redirect('index')
	else:
		form = CommentForm()

	return render(request, 'comment.html',  {"form":form})

