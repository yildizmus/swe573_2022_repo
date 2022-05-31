from django import forms
from space.models import StepModel

class CreateStepModelForm(forms.ModelForm):
    class Meta:
        model=StepModel
        fields= ('stepspace', 'steptitle', 'stepcontent', 'attachment')