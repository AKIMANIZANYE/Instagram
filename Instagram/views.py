# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.contrib.auth.decorators import login_required.

def welcome(request):
    return HttpResponse('Welcome to the Instagram')
def news_of_day(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
@login_required(login_url='/accounts/login/')
def user(request, user_id):     



