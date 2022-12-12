from django import forms
from .models import *


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        labels = {'text':''}

        widgets = {'text': forms.Textarea(attrs={'cols':80})}