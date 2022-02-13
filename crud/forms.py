from django.forms import ModelForm
from crud.models import equipe, servicos, posts

# Create the form class.
class EquipeForm(ModelForm):
     class Meta:
         model = equipe
         fields = ['nome', 'sobrenome', 'cargo', 'telefone', 'email']

class ServicosForm(ModelForm):
    class Meta:
        model = servicos
        fields = ['nome_servico', 'descricao']

class PostsForm(ModelForm):
    class Meta:
        model = posts
        fields = ['titulo', 'autor', 'data_publi', 'conteudo']
