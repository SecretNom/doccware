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