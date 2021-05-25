from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# models
from .models import Tarefa

# forms
from .forms import TarefaForm

# Create your views here.
def index(request):
    tarefas = Tarefa.objects.all()
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TarefaForm()
    context = {'tarefas': tarefas, "form": form}
    return render(request, "index.html", context)

def update(request):
    if request.method == "POST":
        if request.POST["tarefa"] != "":
            tarefa_id = request.POST["id"]
            tarefa_titulo = request.POST["titulo"]
            tarefa_detalhe = request.POST["tarefa"]
            tUpdate = Tarefa(id=tarefa_id, titulo=tarefa_titulo, tarefa=tarefa_detalhe)
            tUpdate.save()
            return redirect("index")
    else:
        return redirect("index")

def delete(request):
    if request.method == "POST":
        tarefa_id = request.POST["id"]
        tarefa = get_object_or_404(Tarefa, id=tarefa_id)
        tarefa.delete()
        return redirect("index")
    else:
        return redirect("index")

def archive(request):
    if request.method == "POST":
        tarefa_id = request.POST["id"]
        Tarefa.objects.filter(id=tarefa_id).update(public=False)
        return redirect("index")
    else:
        return redirect("index")