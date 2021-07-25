from django import forms
from .models import GrossBag


class GrossBagForm(forms.ModelForm):
    class Meta:
        model = GrossBag
        fields = '__all__'
