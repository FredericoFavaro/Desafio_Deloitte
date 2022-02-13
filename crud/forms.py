from django.forms import ModelForm
from crud.models import equipe

# Create the form class.
class EquipeForm(ModelForm):
     class Meta:
         model = equipe
         fields = ['nome', 'sobrenome', 'cargo', 'telefone', 'email']
