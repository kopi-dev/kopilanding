from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['email','description', 'document']
        #exclude = ['full_name', 'email']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_base, provider = email.split('@')
    #     domain, extension = provider.split('.')
    #     if extension != 'ru':
    #         raise forms.ValidationError("Please use a RU zone")
    #     return email

    # def clean_full_name(self):
    #     full_name = self.cleaned_data.get('full_name')
    #     #write validation code
    #     return full_name