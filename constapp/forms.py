from django import forms
from .models import GoalModel,GoalsList
from django.forms import ModelForm


class GoalFormGoal(forms.ModelForm):

    class Meta:
        model=GoalModel
        fields=['Goals']


class GoalFormDate(forms.ModelForm):

    class Meta:
        model=GoalModel
        fields=[ 'Date']

class GoalFormCheck(forms.ModelForm):

    class Meta:
        model=GoalModel
        fields=['Check']
