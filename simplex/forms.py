from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.Select(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)