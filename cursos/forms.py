from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Curso


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

class Registro_user_form(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=30,label='Nombre' )
    last_name = forms.CharField(required=True, max_length=30, label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['username'].label = 'Nombre de Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar Contraseña'



class Curso_form(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'description', 'fecha_inicio', 'fecha_fin', 'cupos', 'estado']

        widgets ={
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
        }
