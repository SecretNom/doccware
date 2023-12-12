const newAsistenciaBtn = document.getElementById('btn_asistencia');
const formAsistenciaDiv = document.querySelector('.form__asistencia');
const closeAsisButton = document.getElementById('closeasistencia_button');


newAsistenciaBtn.addEventListener('click', () => {
    formAsistenciaDiv.classList.add('form__asistencia-active');
    document.body.style.overflow = "hidden";
    

});

closeAsisButton.addEventListener('click', (event) => {
    event.preventDefault();
    formAsistenciaDiv.classList.remove('form__asistencia-active');
    document.body.style.overflow = "auto";

});