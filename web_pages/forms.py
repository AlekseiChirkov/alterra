from django import forms

from web_pages.models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'


