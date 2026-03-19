from django import forms
from .models import Report, Feedback
from django.contrib.auth.models import User


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['week_number', 'content']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comments']


class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        help_texts = {
            'username': None,  
            'email': None,
            'password': None,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")