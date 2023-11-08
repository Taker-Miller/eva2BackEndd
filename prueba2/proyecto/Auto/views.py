from django.shortcuts import render, get_object_or_404, redirect
from .models import Auto
from .forms import AutoForm
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html', {})

def lista_auto(request):
    autos = Auto.objects.all()
    return render(request, 'auto/lista_auto.html', {'autos': autos})

def detalle_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    return render(request, 'auto/detalle_auto.html', {'auto': auto})

def agregar_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_auto')
        else:
            print(form.errors.as_json())  
    else:
        form = AutoForm()
    return render(request, 'auto/agregar_auto.html', {'form': form})

def editar_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('detalle_auto', pk=auto.pk)
    else:
        form = AutoForm(instance=auto)
    return render(request, 'auto/editar_auto.html', {'form': form})

def eliminar_auto(request, pk):
    auto = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        auto.delete()
        return redirect('lista_auto')
    return render(request, 'auto/eliminar_auto.html', {'auto': auto})
    

