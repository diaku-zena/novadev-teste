# import form class from django
from django import forms
  
# import GeeksModel from models.py
from .models import Contacto
  
# create a ModelForm
class ContactoForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Contacto
        fields = "__all__"
    nome= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Nome'}))
    telefone= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Telefone'}))
    email= forms.CharField(widget= forms.EmailInput(attrs={'placeholder':'Email'}))
    mensagem= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Mensagem'}))