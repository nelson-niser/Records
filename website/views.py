from django.shortcuts import render, redirect
from .models import DueForm, Due
from django.utils.timezone import  datetime
today = datetime.now().date()

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        form = DueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        dueForm = DueForm()
        return render(request, 'add.html', {'dueForm':DueForm, 'today':today})

def check(request):
    
    if request.method == 'POST':
        val = request.POST.get("pk")
        Due.objects.filter(pk=val).update(status=True)
        Due.objects.filter(pk=val).update(payment=today)

        return redirect('home')
    
    
    else:
        due = Due.objects.all()
        return render(request, 'check.html', {'due':due})

def history(request):
    due = Due.objects.all()
    return render(request, 'history.html', {'due':due})