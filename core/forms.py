from django import forms

from core.models import Toy


class ToyForm(forms.ModelForm):
    class Meta:
        model = Toy
        fields = (
            'name',
            'description',
            'photo',
            'type',
            'owner_name',
            'owner_phone_number'
        )
