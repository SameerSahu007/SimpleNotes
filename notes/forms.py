from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "textarea is-success is-medium",
            }
        ),
        label="",
    )
    description = forms.CharField(
        required= True,
        widget=forms.Textarea
        
    )

    class Meta:
        model = Post
        exclude = ("user", )
