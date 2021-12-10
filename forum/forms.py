from django import forms
from .models import Post, Comment, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('title','description')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','post_content','image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content', 'image')
