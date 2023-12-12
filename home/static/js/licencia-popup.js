const newLicenciaBtn = document.querySelector('.btn_licencia');
const formLicenciaDiv = document.querySelector('.form__licencia');
const closeButton = document.getElementById('close_button');
const bodyElement = document.body;


newLicenciaBtn.addEventListener('click', () => {
    formLicenciaDiv.classList.add('form__licencia-active');
    document.body.style.overflow = "hidden";
    

});

closeButton.addEventListener('click', (event) => {
    event.preventDefault();
    formLicenciaDiv.classList.remove('form__licencia-active');
    document.body.style.overflow = "auto";

});


function mostrarOcultarSelect() {
    var estadoSelect = document.getElementById("estado");
    var selectDiasAdministrativos = document.getElementById("select__dias_administrativos");

    if (estadoSelect.value === "ausente") {
        selectDiasAdministrativos.style.display = "flex";
        
        
    } else {
        selectDiasAdministrativos.style.display = "none";
    }
}

function mostrarOcultarP(){
    var estadoAdministrativo = document.getElementById('dias_administrativos')
    var pDiasAdministrativos =  document.getElementById("text-da");

        console.log(estadoAdministrativo)
        if(estadoAdministrativo.value === "no"){
            console.log("hola")
            pDiasAdministrativos.style.display = "flex";

        }else{
            pDiasAdministrativos.style.display = "none";

        }
}