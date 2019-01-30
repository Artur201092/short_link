from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(max_length=255, required=True)
