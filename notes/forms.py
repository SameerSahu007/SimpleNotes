from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Title",
                "class": "textarea is-success is-medium postitle",
            }
        ),
        label="Title",
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Description",
                "class": "textarea is-success is-medium postdes",
            }
        )
    )

    class Meta:
        model = Post
        exclude = ("user", "username", )
