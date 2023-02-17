from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from .models import Roles, Hired
from .forms import RolesForm, HiredForm
from django.contrib.auth.models import User

# Create your views here.
@login_required()
def index(request):
    hires = Hired.objects.all()
    if request.method=='POST':
        form = HiredForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = HiredForm()
    context = {
        'hires': hires,
        'form' : form,
    }
    return render(request, 'dashboard/index.html',context)

@login_required()
def staff(request):
    workers = User.objects.all()
    context = {
        'workers': workers
    }
    return render(request, 'dashboard/staff.html', context)

@login_required()
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers':workers,
    }
    return render(request, 'dashboard/staff_detail.html',context)

@login_required()
def roles(request):
    items = Roles.objects.all() #ORM
    # items = Product.objects.raw('SELECT * FROM dashboard_product')

    if request.method == 'POST':
        form = RolesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-roles')
    else:
        form = RolesForm()
    context = {
        'items':items,
        'form': form,
    }
    return render(request, 'dashboard/roles.html',context)

@login_required()
def roles_delete(request, pk):
    item = Roles.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-roles')
    return render(request, 'dashboard/roles_delete.html')

@login_required()
def roles_update(request, pk):
    item = Roles.objects.get(id=pk)
    if request.method=='POST':
        form = RolesForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-roles')
    else:
        form = RolesForm(instance=item)
    context = {
        'form':form,
    }
    return render(request, 'dashboard/roles_update.html', context)

@login_required()
def hired(request):
    hires = Hired.objects.all()
    context = {
        'hires':hires,
    }
    return render(request, 'dashboard/hired.html',context)