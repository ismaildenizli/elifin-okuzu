from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserExtendedCreationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username","email")
    def save(self, commit=True):
        user = super(UserExtendedCreationForm, self).save(commit=False)  # type: object
        user.email = self.cleaned_data["email"]
        if commit:
           user.save()
        return user

