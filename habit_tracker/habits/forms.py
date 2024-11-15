from django import forms
from .models import Habit, Progress

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description']

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['completed']
