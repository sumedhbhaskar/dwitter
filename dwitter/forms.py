from django import forms
from .models import Dweet

class dweetForms(forms.ModelForm):

    body = forms.CharField(required=True,
    widget=forms.widgets.Textarea(
        attrs={
            "placeholder":"Dweet something...",
            "class":"textarea is-sucess is-medium"
        }
        ),
        label="",
    )

    class Meta:
        model = Dweet
        exclude = ("user",)
