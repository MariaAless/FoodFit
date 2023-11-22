from django import forms
from .models import Receita
from datetime import date
from usuarios.models import Usuario

class CadastroReceita(forms.ModelForm):
    class Meta:
        model = Receita
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):  #sempre que ouver uma instancia,to sobreescrevendo, to usando para tirar o campo do usuario no cadastro
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()
        self.fields['ingredientes'].widget = forms.Textarea()
        self.fields['modo_preparo'].widget = forms.Textarea()
        



class CategoriaReceita(forms.Form):
    nome = forms.CharField(max_length=30)
    descricao = forms.CharField(max_length=60)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['descricao'].widget = forms.Textarea()

        
        
    
