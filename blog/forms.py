from django import forms
from .models import Blog

class PostForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title', 'body', 'category')

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ('title', 'slug')
