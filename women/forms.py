from django import forms
from .models import Women, Category


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255,
                            label='Заголовок',
                            widget=forms.TextInput(attrs=
                                                   {'class': 'form-input'}))
    slug = forms.SlugField(max_length=255,
                           label='URL',
                           widget=forms.TextInput(attrs=
                                                  {'class': 'form-input'}))
    content = forms.CharField(widget=forms.Textarea(attrs=
                                                    {'cols': 60, 'rows': 10}),
                              label='Сожержание')
    is_published = forms.BooleanField(label='Публикация',
                                      required=False,
                                      initial=True)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),
                                 label='Категория',
                                 empty_label='Категория не выбрана')