from django.shortcuts import render, get_object_or_404, redirect,  reverse
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
    success_asistencia=False
    porcentaje_dp = 0
    teacher = get_object_or_404(Teacher, id=teacher_id)
    licencias = Licencia.objects.filter(id=teacher.id).count()
    total_dias = teacher.dias_presente + teacher.dias_ausente

    if total_dias > 0:
        porcentaje_dp = round((teacher.dias_presente * 100) / total_dias)
        porcentaje_da = round((teacher.dia_admi * 100) / total_dias)
        porcentaje_dl = round((teacher.dia_licencia * 100)/total_dias)
        porcentaje_dausente = round((teacher.dias_ausente * 100)/total_dias)


    dias_ausente = 0
    dias_presente = 0
    admin_days = 0

    if request.method == 'POST':
        if 'form_licencia' in request.POST:
            date = request.POST['date']
            imagen = request.FILES['file']
            file_path = default_storage.save('uploads/' + imagen.name, imagen)

            licencia = Licencia(
                date=date,
                imagen=imagen,
                aceptada=True,
                teacher=teacher
            )
            

            licencia.save()
            teacher.dia_licencia += 1
            teacher.save() 

            return redirect(reverse('info', args=[teacher.id]))
        elif 'form_asistencia' in request.POST:
            if request.POST['asistencia'] == 'ausente':
                dias_ausente = 1
                if request.POST['admin_days'] == 'si':
                    admin_days = 1
            elif request.POST['asistencia'] == 'presente':
                dias_presente = 1

            teacher.dias_ausente += dias_ausente
            teacher.dias_presente += dias_presente
            teacher.dia_admi += admin_days

            new_asistencia_date = AsistenciaDate.objects.create(date=request.POST['asistencia_date'])

            teacher.asistencia_dates.add(new_asistencia_date)

            success_asistencia=True
            teacher.save()
            return redirect(reverse('info', args=[teacher.id]))

            

    context = {
        'teacher': teacher,
        'licencias': licencias,
        'total_dias': total_dias,
        'porcentaje_dp': porcentaje_dp,
        'success_asistencia':success_asistencia,
        'porcentaje_da':porcentaje_da,
        'porcentaje_dl':porcentaje_dl,
        'porcentaje_dausente':porcentaje_dausente
    }

    return render(request, 'info.html', context)

