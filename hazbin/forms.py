from django import forms
from .models import Registration, Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'account_type')

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('client', 'administration', 'hotelroom', 'start_date_time', 'end_date_time')

    def clean(self):
        cleaned_data = super().clean()
        start_date_time = cleaned_data.get('start_date_time')
        end_date_time = cleaned_data.get('end_date_time')
        if start_date_time and end_date_time and start_date_time >= end_date_time:
            raise forms.ValidationError('Start date must be before end date')
        return cleaned_data