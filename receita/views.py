from django.shortcuts import render,redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Receita, Categoria,Historico
from.forms import CadastroReceita,CategoriaReceita
from django import forms

# Create your views here.
def home(request):
    if request.session.get('usuario'): #se o usuário  estiver logado, mostre:
        usuario = Usuario.objects.get(id = request.session['usuario']) #pegou o usuario, na posição dele
        status_categoria=request.GET.get('cadastro_categoria')
        receitas =Receita.objects.filter(usuario=usuario) #filtando todas as receitas do usuario logado
       # return HttpResponse(f'olá {usuario}')
        form=CadastroReceita()#instanciando o formulário
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        form_categoria= CategoriaReceita()
       
        return render(request,'receita/home.html', {'receitas': receitas,'usuario_logado':request.session.get('usuario'),"form":form,
                                                    'status_categoria':status_categoria,'form_categoria':form_categoria})  #{'receita': receita} enviando os livros para o html, o 'usuario_logado' é para mostrar o botão de sair nessa página
    else:  #senão tiver logado
        return redirect('/auth/login/?status=2') #retornar para a pagina de
    
def detalhe(request, id):
    if request.session.get('usuario'): #se o usuario ta logado
        receita= Receita.objects.get(id=id)# o get(id=id)pega apenas a receita especifica
       
        if request.session.get('usuario')== receita.usuario.id:
           
            usuario = Usuario.objects.get(id = request.session['usuario'])
            categoria_receita = Categoria.objects.filter(usuario = request.session.get('usuario')) #filtro as categoria dos usuario logado
            historico=Historico.objects.filter(receita=receita)
            form=CadastroReceita()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
            form_categoria= CategoriaReceita()

            return render(request,'receita/detalhe.html',{'receita':receita,'categoria_receita': categoria_receita, 
                                                          'historico':historico,'usuario_logado':request.session.get('usuario'),
                                                          "form":form,'id_receita':id, 'form_categoria':form_categoria}) # o 'usuario_logado' é para mostrar o botão de sair nessa página


            
        else:
            return  HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')

def Cadastrar_Receita(request):
    if request.method == "POST":
        form = CadastroReceita(request.POST)
        if form.is_valid(): #se o formulário for válido
            form.save() # salve ele 
            return redirect('/receita/home') #retorne 
        else:
            return HttpResponse('Dados invalidos')
        

def cadastrar_categoria(request):
    form = CategoriaReceita(request.POST)
    nome = form.data['nome']
    descricao = form.data['descricao']
    id_usuario = request.POST.get('usuario')
    if int(id_usuario) == int(request.session.get('usuario')):
        user = Usuario.objects.get(id = id_usuario) #instancia
        categoria = Categoria(nome = nome, descricao = descricao, usuario = user )
        categoria.save()
        return redirect('/receita/home?cadastro_categoria=1')
    else:
        return HttpResponse('erro')
        
def Excluir_Receita(request, id):
    receita=Receita.objects.get(id=id).delete()
    return redirect('/receita/home')
