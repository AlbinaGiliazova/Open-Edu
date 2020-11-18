"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment, Article


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class PoolForm(forms.Form):
    """Form for feedback."""
    username = forms.CharField(max_length=254, min_length=2, label='Имя',
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя',
                                   }))
    gender = forms.ChoiceField(label='Ваш пол', 
                               choices=[('1', 'Мужской'), ('2', 'Женский')],
                               widget=forms.RadioSelect, initial=1)
    likes = forms.BooleanField(label='Нравится ли Вам этот сайт?', required=False, 
                               widget=forms.CheckboxInput({
                                   'class': 'form-control',
                                   'checked' : ''}))
    WHERE_CHOICES = [
    ('link', 'Ссылка на другом сайте'),
    ('author', 'От автора'),
    ('another', 'Другие способы'),
    ]
    where = forms.CharField(label='Откуда Вы узнали об этом сайте?', widget=forms.RadioSelect(choices=WHERE_CHOICES))
    MARK_CHOICES = [
        ('Отлично', 'Отлично'),
        ('Хорошо', 'Хорошо'),
        ('Могло бы быть и лучше', 'Могло бы быть и лучше'),
        ]
    mark = forms.ChoiceField(choices=MARK_CHOICES, label='Оцените сайт')
    text = forms.CharField(label='Ваши пожелания', widget=forms.Textarea(attrs={'rows':12,'cols':20}))


class CommentForm (forms.ModelForm):

        class Meta:

            model = Comment # используемая модель

            fields = ('text',) # требуется заполнить только поле text

            labels = {'text': "Комментарий"} # метка к полю формы text

class ArticleForm (forms.ModelForm):

        class Meta:

            model = Article # используемая модель

            fields = ('header', 'description', 'content', 'image') 

            labels = {'header': 'Заголовок', 'description': 'Описание', 'content': 'Содержимое', 
                      'image':'Картинка'} 
