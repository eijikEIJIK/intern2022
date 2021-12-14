from django import forms

from microhr.models import Work

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('title', 'salary_min', 'salary_max', 'text')
        labels = {
            'title': '求人タイトル',
            'salary_min': '給与下限(万円)',
            'salary_max': '給与上限(万円)',
            'text': '委細',
        }