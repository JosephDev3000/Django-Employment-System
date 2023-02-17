from django import forms
from .models import Roles, Hired


class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['name','category','quantity']


class HiredForm(forms.ModelForm):

    class Meta:
        model = Hired
        fields = ['roles', 'hired_quantity']