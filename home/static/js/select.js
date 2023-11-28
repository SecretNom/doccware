document.getElementById('asignatura').addEventListener('change', function() {
    var selectedAsignatura = this.value;

    document.querySelectorAll('.profesor').forEach(function(profesor) {
        var asignaturaIds = profesor.dataset.asignaturaIds.split(',');

        if (asignaturaIds.includes(selectedAsignatura) || selectedAsignatura === "") {
            profesor.style.display = 'table-row';  // Mostrar la fila de la tabla
        } else {
            profesor.style.display = 'none';  // Ocultar la fila de la tabla
        }
    });
});


function redirectToInfoPage() {
    var selectedProfesorId = document.getElementById('profesorId').value;
    window.location.href = '/info/' + selectedProfesorId + '/';
}

document.getElementById('profesorForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Evitar que el formulario se envíe normalmente
    redirectToInfoPage();
});

document.getElementById('verDetalles').addEventListener('click', redirectToInfoPage);

var checkboxes = document.querySelectorAll('.profesorCheckbox');
checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        var verDetallesButton = document.getElementById('verDetalles');
        
        // Desmarcar todos los demás checkboxes
        checkboxes.forEach(function(cb) {
            if (cb !== checkbox) {
                cb.checked = false;
            }
        });

        if (checkbox.checked) {
            verDetallesButton.disabled = false;
            document.getElementById('profesorId').value = checkbox.getAttribute('data-profesor-id');
        } else {
            verDetallesButton.disabled = true;
            document.getElementById('profesorId').value = '';
        }
    });
});