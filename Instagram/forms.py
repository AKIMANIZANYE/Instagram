from django import forms
from .models import Image

class NewsPicturesForm(forms.ModelForm):
     class Meta:
        model = Image
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
     your_name = forms.CharField(label='First Name',max_length=30)
     your_location = forms.CharField(label='Location',max_length=30)
     