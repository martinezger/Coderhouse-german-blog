from django import forms


class AvatarFormulario(forms.Form):

    imagen = forms.ImageField(required=True)
