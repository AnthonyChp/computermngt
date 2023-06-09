from django import forms
from django.core.exceptions import ValidationError

class AddMachineForm(forms.Form):

    nom = forms.CharField(required=True, label='Nom de la machine')

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) != 10:
            raise ValidationError( ("Erreur de format pour le nom"))

        return data