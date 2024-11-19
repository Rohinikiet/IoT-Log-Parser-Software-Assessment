from django import forms

class LogFileForm(forms.Form):
    file = forms.FileField(label='Upload Log File')
