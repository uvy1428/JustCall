from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    required_job = forms.CharField(label='requirement', max_length=300)
