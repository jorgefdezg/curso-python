from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages


# Create your views here.
#MVC = Modelo Vista Controlador -> Acciones(metodos)
#MVT = Modelo Vista Template -> Acciones(metodos)

layout = """
<h1>Sitio web con Django</h1>
<hr/>
<ul>
    <li>
        <a href="/inicio">Inicio</a>
    </li>
    <li>
        <a href="/hola-mundo">Hola Mundo!</a>
    </li>
        <li>
        <a href="/pagina-pruebas">Pagina de pruebas</a>
    </li>
            <li>
        <a href="/contacto">Contacto</a>
    </li>
</ul>
<hr/>
"""


def index(request):

    year = 2023
    hasta = range(year,2051)
    nombre = "Jorge Fernandez Gonzalez"
    lenguajes = ['JavaScript','Python','PHP','C']

    return render(request,'index.html',{
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que esta en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta
    })


def hola_mundo(request):

    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):

    if redirigir == 1:
        return redirect('contacto',nombre="Jorge",apellidos="Fernandez")


    return render(request, 'pagina.html', {
        'texto': 'Este es mi texto',
        'lista': ['uno','dos','tres']
    })

def contacto(request, nombre = "", apellidos = ""):
    html = ""

    if nombre and apellidos:
        html = f"<h3>El nombre completo es {nombre} {apellidos}</h3>"

    return HttpResponse(layout +"<h2>Contacto</h2>"+html)


def crear_articulo(request, title, content, public):

    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    articulo.save()

    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")


def save_article(request):

    if request.method == "POST":

        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        articulo.save()
        return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content}")
    
    else:
        return HttpResponse("<h2>No se ha podido crear el articulo</h2>")


    

    

def create_article(request):

    return render(request, 'create_article.html')


def create_full_article(request):

    if request.method == "POST":

        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get("title")
            content = data_form["content"]
            public = data_form["public"]

            articulo = Article(
            title = title,
            content = content,
            public = public
            )

            articulo.save()

            #Crear mensaje flash (Sesion que solo se muestra una vez)
            messages.success(request,f'Se ha creado correctamente el articulo:  {articulo.title}')

            return redirect('articulos')

            #return HttpResponse(articulo.title + " - " + articulo.content + " - " +str(articulo.public))

    else:
        formulario = FormArticle()

    return render(request,'create_full_article.html',{
        'form': formulario
    })

def articulo(request):

    try:
        articulo = Article.objects.get(title="Superman", public = True)
        response = f"Articulo:{articulo.id} - {articulo.title}"
    except:
        response = "Articulo no encontrado"

    return HttpResponse(response)

def editar_articulo(request, id):
    
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo editado: {articulo.id} editado. {articulo.title} - {articulo.content}")

def articulos(request):

    articulos = Article.objects.all().order_by('-id')
    # articulos = Article.objects.order_by('id')[0:1]

    # articulos = Article.objects.filter(id__lte=10, title__contains="2")

    # articulos = Article.objects.filter(title="Articulo").exclude(public=False)

    # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo 2' AND public=1")

    # articulos = Article.objects.filter(
    #     Q(title__contains="2")| Q(public=True)
    # )

    return render(request, 'articulos.html',{
        'articulos':articulos
    })


def borrar_articulos(request, id):

    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')