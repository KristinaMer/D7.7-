from django.forms import ModelForm, BooleanField
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post_author', 'post_category']

