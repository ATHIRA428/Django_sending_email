from django import forms
from django.forms import  Form ,ModelForm
from model_setup . models import Post,Profile,Comment

class AddPost(ModelForm):
    class Meta:
        model=Post
        fields='__all__'


class Profile(ModelForm):
    class Meta:
        model=Profile
        fields='__all__'

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']