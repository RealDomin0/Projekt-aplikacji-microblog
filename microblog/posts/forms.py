from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'rows': 3,
                    'placeholder': 'Co słychać?',
                }
            ),
        }
