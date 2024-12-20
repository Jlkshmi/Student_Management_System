from django.shortcuts import render, get_object_or_404, redirect
from task_app.form import StudyForm
from task_app.models import Study


# Create your views here.
def study_list(request):
    studies = Study.objects.all()
    return render(request, 'home.html', {'studies': studies})

def add_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm()
    return render(request, 'add_study.html', {'form': form})

def edit_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm(instance=study)
    return render(request,'add_study.html', {'form': form})

def delete_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    study.delete()
    return redirect('study_list')