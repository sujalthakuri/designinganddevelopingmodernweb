from django import forms 
from . models import profile_image
  
class ImageForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = profile_image
		fields = "__all__" 