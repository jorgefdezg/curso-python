from django.shortcuts import render, HttpResponse, redirect

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

    return render(request,'index.html')


def hola_mundo(request):

    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):

    if redirigir == 1:
        return redirect('contacto',nombre="Jorge",apellidos="Fernandez")


    return render(request, 'pagina.html')

def contacto(request, nombre = "", apellidos = ""):
    html = ""

    if nombre and apellidos:
        html = f"<h3>El nombre completo es {nombre} {apellidos}</h3>"

    return HttpResponse(layout +"<h2>Contacto</h2>"+html)