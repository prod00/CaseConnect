from django import forms


class ApplicationForm(forms.Form):
    email_body = forms.Textarea()
