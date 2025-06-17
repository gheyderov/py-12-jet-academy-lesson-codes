from django import forms
from blog.models import Blog


class BlogCreationForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = [
            'title',
            'description',
            'category',
            'image'
        ]
        widgets = {
            'title' : forms.TextInput(attrs={
                'class' : 'form-control',
            }),
            'description' : forms.Textarea(attrs={
                'class' : 'form-control'
            }),
            'category' : forms.Select(attrs={
                'class' : 'form-control'
            }),
            
        }