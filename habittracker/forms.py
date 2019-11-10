from django import forms
from habittracker.models import Habit, Record
from django.forms import ModelForm


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'target']

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['record', 'met_goal', 'actual', 'created_at']
