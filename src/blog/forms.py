from django import forms
from .models import Category, Post


choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for choice in choices:
    choice_list.append(choice)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(
                choices=choice_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
