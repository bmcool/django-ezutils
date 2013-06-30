from django import forms
from hhb.widgets import DatePickerWidget

class DatePickerField(forms.DateField):
    widget = DatePickerWidget
