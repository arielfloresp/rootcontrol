from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import DatacenterForm, LogbookForm
from .models import Datacenter, Logbook
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home(request):
    return render (request, 'rootcontrol/home.html')

def dash(request):
    return render(request, 'core/dash.html')

def datacenterList(request):
    datacenters = Datacenter.objects.all()
    return render(request, 'core/datacenter_list.html', {'datacenters': datacenters})

def logbook(request):
    return render(request, 'modules/logbook/logbook.html')

def users(request):
    return render(request, 'users/users.html')

def lista_datacenters(request):
    datacenters = Datacenter.objects.all().order_by('id')  # Puedes ajustar el orden si es necesario
    print(datacenters)  # Imprime los objetos en la consola para verificar
    paginator = Paginator(datacenters, 20)  # 20 datacenters por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'modules/datacenter/datacenterlist.html', {'page_obj': page_obj})

@login_required
def create_logbook_entry(request):
    if request.method == 'POST':
        form = LogbookForm(request.POST)
        if form.is_valid():
            logbook_entry = form.save(commit=False)  # No guardar aún en la base de datos
            logbook_entry.usuario = request.user  # Asignar el usuario actual
            logbook_entry.datacenter = Datacenter.objects.first()  # Asignar el primer datacenter
            logbook_entry.save()  # Guardar el registro en la base de datos
            
            return redirect('logbook')  # Cambia esto a donde quieras redirigir
    else:
        form = LogbookForm()

    datacenter = Datacenter.objects.first()  # Obtiene el primer datacenter

    return render(request, 'modules/logbook/logbook.html', {
        'form': form,
        'username': request.user.username,  # Nombre de usuario
        'email': request.user.email,  # Correo electrónico
        'datacenter': datacenter  # Primer datacenter
    })