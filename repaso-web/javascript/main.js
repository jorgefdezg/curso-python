var nombre = "Jorge Fernandez";
var altura = 165;

/* var concatenacion = nombre + " " + altura;

var datos = document.getElementById("datos");
datos.innerHTML = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <H3>Mido: ${altura} cm</h3>
`;

if(altura > 190){
    datos.innerHTML += '<h1>Eres una persona ALTA</h1>';
}else{
    datos.innerHTML += '<h1>Eres una persona BAJA</h1>';
}

for(var i = 2000; i<=2020;i++){
    datos.innerHTML +='<h2>Estamos en el año ' +i;
} */


function MuestraMiNombre(nombre,altura){
    var misdatos = `
    <h1>Soy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <H3>Mido: ${altura} cm</h3>
`;

    return misdatos;
}

function impimir(){
    var datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre("Jorge Fernandez",165);
}

impimir();

var nombres = ["Jorge", "Samuel", "Pablo"];

document.write("<h1>Listado de nombres</h1>");

/* for (i=0;i<nombres.length;i++){
    document.write(nombres[i] + "<br/>");
} */

nombres.forEach((nombre) => {
    document.write(nombre + "<br/>");
});


