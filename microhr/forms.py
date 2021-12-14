from django import forms

from microhr.models import Work

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('title', 'salary_min', 'salary_max', 'text')