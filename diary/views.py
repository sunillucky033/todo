from django.shortcuts import render,redirect
from .models import memory
from django.utils import timezone
from django.contrib.auth.models import User
def show(request):
    log_user=request.user
    memories=memory.objects.filter(user=log_user)
    return render(request,'show.html',{'m':memories})

def add(request):
    if request.method=='POST':
        data=request.POST['data']
        current_date=timezone.now()
        new=memory(content=data,date=current_date, user=request.user)
        new.save()
        return render(request,'add.html')
    else:
        return render(request,'add.html')

def delete(request,pid):
    a=memory.objects.get(id=pid)
    a.delete()
    return redirect('/')