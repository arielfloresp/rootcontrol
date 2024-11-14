from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import DatacenterForm
from .models import Datacenter

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


    



def lista_datacenters(request):
    datacenters = Datacenter.objects.all().order_by('id')  # Puedes ajustar el orden si es necesario
    print(datacenters)  # Imprime los objetos en la consola para verificar
    paginator = Paginator(datacenters, 20)  # 20 datacenters por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'modules/datacenter/datacenterlist.html', {'page_obj': page_obj})

