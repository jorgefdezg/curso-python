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

    html = """
    <h1>Inicio</h1>
    <p>Años hasta 2050:</p>
    <ul>
    """

    year = 2023
    while year <= 2050:

        if year%2==0:
            html += f"<li> {str(year)}</li>"
        year +=1

    html +="</ul>"

    return HttpResponse(layout + html)


def hola_mundo(request):
    return HttpResponse(layout +"""
    <h1>Hola mundo con Django!</h1>
    <h3>Soy Jorge Fernandez</h3>
    """)

def pagina(request, redirigir = 0):

    if redirigir == 1:
        return redirect('contacto',nombre="Jorge",apellidos="Fernandez")


    return HttpResponse(layout +"""
    <h1>Pagina de mi web</h1>
    <p>Creado por Jorge Fernandez</p>
    """)

def contacto(request, nombre = "", apellidos = ""):
    html = ""

    if nombre and apellidos:
        html = f"<h3>El nombre completo es {nombre} {apellidos}</h3>"

    return HttpResponse(layout +"<h2>Contacto</h2>"+html)