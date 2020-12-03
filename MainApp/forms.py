from django.forms import ModelForm
from MainApp.models import Snippet, Comment


class SnippetForm(ModelForm):
   class Meta:
       model = Snippet
       # Описываем поля, которые будем заполнять в форме
       fields = ['name', 'lang', 'code']


class CommentForm(ModelForm):
   class Meta:
       model = Comment
       # Описываем поля, которые будем заполнять в форме
       fields = ['text']