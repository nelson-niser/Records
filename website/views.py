from django.shortcuts import render, redirect
from .models import DueForm, Due
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def add(request):
    if request.method == 'POST':
        update_form = request.POST.copy()
        update_form.update({'query':datetime.now().date()})
        form = DueForm(update_form)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        dueForm = DueForm()
        return render(request, 'add.html', {'dueForm':DueForm, 'today':datetime.now().date()})

def check(request):
    
    if request.method == 'POST':
        val = request.POST.get("pk")
        Due.objects.filter(pk=val).update(status=True)
        Due.objects.filter(pk=val).update(payment=datetime.now().date())

        return redirect('home')
    
    
    else:
        due = Due.objects.all()
        return render(request, 'check.html', {'due':due})


def checkall(request):
    
    if request.method == 'POST':
        val = request.POST.get("item")
        val2 = request.POST.get("item2")
        guy1 = User.objects.filter(username=val)
        guy2 = User.objects.filter(username=val2)
        a = Due.objects.all()

        l = []
        for item in a:
            if item.person == guy1[0]:
                if item.to == guy2[0]:
                    if item.status==False:
                        Due.objects.filter(pk=item.pk).update(status=True)
                        Due.objects.filter(pk=item.pk).update(payment=datetime.now().date())


        return redirect('home')

    
    
    else:
        due = Due.objects.all()
        usr = User.objects.all()
        val = []
        if len(due) > 0:
            for guy1 in usr:
                for guy2 in usr:
                    if guy1!=guy2:
                        sum = 0
                        for item in due:
                            if item.status == False and item.person==guy1 and item.to==guy2:
                                sum += item.amount
                        if sum!=0:
                            val.append((guy1,guy2,sum))
                        
                    

        return render(request, 'check_all.html', {'due':val})

def history(request):
    due = Due.objects.all()
    return render(request, 'history.html', {'due':due})