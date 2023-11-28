from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def home (request):
    asignaturas = Asignatura.objects.all()
    teachers = Teacher.objects.all()
    context={
        'teachers': teachers,
        'asignaturas':asignaturas
    }
    return render(request, 'home.html', context)
@login_required
def add(request):
    if request.method == 'POST':
        form = DoceForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home') 
        else:
            print('form no valido:',form.errors)
    else:
        form = DoceForm()
    
    context = {
        'form': form
        }
    return render(request, 'add.html', context)
    
@login_required
def info(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    licencias = Licencia.objects.filter(id=teacher.id).count()


    if request.method == 'POST':
        date = request.POST['date']
        imagen =request.FILES['file']
        file_path = default_storage.save('uploads/' + imagen.name, imagen)

        licencia = Licencia(
            date=date, 
            imagen= imagen,
            aceptada=True,
            teacher=teacher
            ) 
        licencia.save()
    
    context = {
        'teacher': teacher,
        
        'licencias': licencias,
        }

    return render(request, 'info.html', context)