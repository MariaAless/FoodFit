from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Receita, Categoria,Comentario,Historico
from.forms import CadastroReceita,CategoriaReceita, ComentarioForm
from django.db.models import Q
from django import forms

# Create your views here.
def home(request):
    if request.session.get('usuario'): #se o usuário  estiver logado, mostre:
        usuario = Usuario.objects.get(id = request.session['usuario']) #pegou o usuario, na posição dele
        status_categoria=request.GET.get('cadastro_categoria')
        receitas =Receita.objects.filter(usuario=usuario) #filtrando todas as receitas do usuario logado
       # return HttpResponse(f'olá {usuario}')
        form=CadastroReceita()#instanciando o formulário
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        form_categoria= CategoriaReceita()
        usuarios= Usuario.objects.all() # pega todos os usuarios
       
        return render(request,'receita/home.html', {'receitas': receitas,'usuario_logado':request.session.get('usuario'),"form":form,
                                                    'status_categoria':status_categoria,'form_categoria':form_categoria, "usuarios":usuarios})  #{'receita': receita} enviando os livros para o html, o 'usuario_logado' é para mostrar o botão de sair nessa página
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
            usuarios= Usuario.objects.all()
            receitas= Receita.objects.filter(usuario_id=request.session.get('usuario'))


            return render(request,'receita/detalhe.html',{'receita':receita,'categoria_receita': categoria_receita, 
                                                          'historico':historico,'usuario_logado':request.session.get('usuario'),
                                                          "form":form,'id_receita':id, 'form_categoria':form_categoria,
                                                          "usuarios":usuarios,"receitas":receitas}) # o 'usuario_logado' é para mostrar o botão de sair nessa página

        else:
            return  HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')

def Cadastrar_Receita(request):
    if request.method == "POST":
        form = CadastroReceita(request.POST,request.FILES)
        
        if form.is_valid(): #se o formulário for válido
            form.save() # salve ele 
            return redirect('/receita/home') #retorne 
        else:
            return HttpResponse('Dados inválidos')
        
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
    receita=Receita.objects.get(id=id)
    receita.delete()
    return redirect('/receita/home')

from django.db.models import Q

def listarTodos(request):
    query = request.GET.get('q')
    # No seu arquivo views.py

    if query:
        listReceita = Receita.objects.filter(Q(nome__icontains=query) | Q(categoria__nome__icontains=query))
    else:
        listReceita = Receita.objects.all()

    return render(request, 'receita/listtodos.html', {'listReceita': listReceita, 'usuario_logado': request.session['usuario'], 'query': query})




def detalheLista(request, id):
    receita = get_object_or_404(Receita, id=id)
    comentarios = Comentario.objects.filter(receita=receita)

    if request.method == 'POST':
        form = ComentarioForm(request.POST, user=request.user, receita=receita)
        if form.is_valid():
            form.save()

            # Limpar o formulário após salvar o comentário
            form = ComentarioForm(user=request.user, receita=receita)
    else:
        form = ComentarioForm(user=request.user, receita=receita)

    return render(request, "receita/detalheListatodos.html", {
        'usuario_logado': request.user,
        'receita': receita,
        'comentarios': comentarios,
        'form': form
    })



     

def alterarReceita(request):
    receita_id = request.POST.get('receita_id') #pega no nome lá na pagina de detalhes
    nome_receita= request.POST.get('nome_receita')
    ingredientes= request.POST.get('ingredientes')
    modo_preparo= request.POST.get('modo_preparo')
    tempo_preparo= request.POST.get('tempo_preparo')
    categoria_id=request.POST.get('categoria_id')

    categoria = Categoria.objects.get(id = categoria_id)
    receita = Receita.objects.get(id= receita_id)

    if receita.usuario.id == request.session['usuario']: # se o usuario desse livro for igual ao usuario logado eu posso alterar
        receita.nome = nome_receita
        receita.ingredientes = ingredientes
        receita.modo_preparo = modo_preparo
        receita.tempo_preparo = tempo_preparo
        receita.categoria = categoria
        receita.save()
        return redirect(f'/receita/detalhe/{receita_id}')
    else:
        return redirect('/auth/sair')

