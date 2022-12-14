import datetime
from django import forms
from vehiculos.models import Vehiculo, Marca, Mantencion
from vehiculos.models import Vehiculo

class FiltrarMantencionesFormulario(forms.Form):
    mantencion = forms.ModelChoiceField(queryset=Mantencion.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    fecha_inicial = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}), required=False)
    fecha_final = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date'}), required=False)


class VehiculoFormulario(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'
        exclude = ('mantenciones', 'usuario')
        widgets = {
            'marca': forms.widgets.Select(attrs={'class': 'form-select'}),
            'modelo': forms.widgets.Select(attrs={'class': 'form-select'}),
            'año': forms.widgets.NumberInput(attrs={'class': 'form-control', 'min': '1970', 'max': f'{datetime.datetime.now().year}'}),
        }

    def clean_año(self):
        año = self.cleaned_data['año']
        if año > datetime.datetime.now().year or año < 1970:
            raise forms.ValidationError('Año incorrecto')
        return año

    def clean_modelo(self):
        modelo = self.cleaned_data['modelo']
        marca = self.cleaned_data['marca']
        if marca != modelo.marca:
            raise forms.ValidationError('El modelo no coincide con la marca')
        return modelo


class FiltrarVehiculosFormulario(forms.Form):
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    año = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
