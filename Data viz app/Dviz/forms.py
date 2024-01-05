from django import forms
from .models import UserInput
import json

class DataForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = ['data', 'chart_type']

    def clean_data(self):
        data = self.cleaned_data['data']
        try:
            json.loads(data)
        except json.JSONDecodeError:
            raise forms.ValidationError("Invalid JSON format for data.")
        return data
