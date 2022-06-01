from django import forms


class MoviesForm(forms.Form):
    name= forms.CharField(label='Ingresa el nombre',min_length=3, max_length=30)
    code= forms.IntegerField()
    sala= forms.CharField(label='Ingresa la sala',min_length=3, max_length=30)

class SalaForm(forms.Form):
    number= forms.IntegerField()
    code= forms.IntegerField()

class ScheduleForm(forms.Form):
    horario= forms.DateField(widget=forms.SelectDateWidget)
    pelicula= forms.CharField(max_length=20, label='Ingresa la pelicula')
    sala=forms.CharField(max_length=10, label='Ingresa la sala')
    code= forms.IntegerField()

class PromocionesForm(forms.Form):
    precio= forms.IntegerField()
    code= forms.IntegerField()
    descripcion= forms.CharField(min_length=3, max_length=100, label='Ingresa una descripcion', widget=forms.Textarea)