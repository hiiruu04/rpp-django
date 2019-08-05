# membuat form
from django import forms

from .models_randomForest import RandomForest as RandomForestModel


class RandomForestForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = RandomForestModel
        fields = (
            'dataset',
            'setlabel',
            'setfitur',
            'hyperparameter',
            'test_prosentase',
        )

        labels = {
            'setlabel': ' Label(y)',
            'setfitur': 'Fitur(X)',
            'hyperparameter': 'Hyperparameter Random Forest',
            'test_prosentase': 'Prosentase Tesst Split (%)',
        }

        widgets = {
            'dataset': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'setlabel': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'setfitur': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'hyperparameter': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'test_prosentase': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 5,
                    'value': 30,
                    'max': 50,
                }
            ),
        }
