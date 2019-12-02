from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import(
    FormView, CreateView
)

# Create your views here.


def index(request):
    company_list = Company.objects.order_by('name')
    context = {
        'company_list': company_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, id):
    company = Company.objects.get(id=id)
    context ={
        'company': company
    }
    return render(request, 'polls/detail.html', context)


class CreateWorker(CreateView):
    model = Worker
    field = ['name']
    
