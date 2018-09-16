from django import forms
from .models import BaseTable


class BaseTableForm(forms.ModelForm):
    class Meta:
        model = BaseTable
        fields = ['name', 'CustomerID', 'Account']


