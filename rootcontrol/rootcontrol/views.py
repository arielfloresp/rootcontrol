from django.shortcuts import render
from django.core.paginator import Paginator
from core.models import Datacenter 

def home(request):
    return render(request, 'base.html') 

def addDatacenter(request):
    return render(request, 'modules/datacenter/datacenters.html')



def baseDash(request):
    return render(request, 'baseDash.html')


def datacenters(request):
    datacenters = Datacenter.objects.all().order_by('id')  # Puedes ajustar el orden si es necesario
    paginator = Paginator(datacenters, 10)  # 20 datacenters por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'modules/datacenter/datacenters.html', {'page_obj': page_obj})

def logbook(request):
    return render(request, 'modules/logbook/logbook.html')
