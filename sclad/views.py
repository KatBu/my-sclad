from django.shortcuts import render
from .models import Category
from .models import Tovar
from .models import ScladTov
from .forms import TovarForm
from .forms import ScladTovForm
from django.shortcuts import redirect,render, get_object_or_404,render_to_response
from django.contrib import auth
from datetime import datetime, date, time

# Create your views here.

def myminisclad(request):
    #tov = Tovar.objects.filter(category=Category.objects.get(full_name='Декоративная косметика')).order_by('full_name')
    #Scladik = ScladTov.objects.order_by('mytovars')
    #Scladik = ScladTov.objects.All()filter(kol>'0')
    #Scladik = ScladTov.objects.filter(srokgod='20').order_by('mytovars')
    #Scladik = ScladTov.objects.filter(myuser=request.user).order_by('mytovars')
    if request.user.is_authenticated():
        Scladik = ScladTov.objects.filter(myuser=request.user).order_by('mytovars')
    else:
        Scladik = ScladTov.objects.order_by('mytovars')
    return render(request, 'sclad/minisclad.html', {'tovar': Scladik, 'username':auth.get_user(request).username})

def tovar(request):
    tov=Tovar.objects.order_by("full_name")
    return render(request, 'sclad/tovar.html', {'tovar': tov, 'username':auth.get_user(request).username})

def tov_new(request):
    if request.method == "POST":
        form = TovarForm(request.POST)
        if form.is_valid():
            tovarcik = form.save(commit=False)
            tovarcik.save()
            return redirect('tov_edit', pk=tovarcik.pk)
    else:
        form = TovarForm()
    return render(request, 'sclad/tov_edit.html', {'TovarNewForm': form, 'username':auth.get_user(request).username})

def tov_edit(request, pk):
    tovarcik = get_object_or_404(Tovar, pk=pk)
    if request.method == "POST":
        form = TovarForm(request.POST, instance=tovarcik)
        if form.is_valid():
            tovarcik = form.save(commit=False)
            tovarcik.save()
            #return redirect('tov_edit', pk=tovarcik.pk)
            tov=Tovar.objects.order_by("full_name")
            return render(request, 'sclad/tovar.html', {'tovar': tov, 'username':auth.get_user(request).username})
    else:
        form = TovarForm(instance=tovarcik)
    return render(request, 'sclad/tov_edit.html', {'TovarNewForm': form, 'username':auth.get_user(request).username})

def tov_del(request, pk):
    tovarcik = get_object_or_404(Tovar, pk=pk)
    tovarcik.delete()
    tov=Tovar.objects.order_by("full_name")
    return render(request, 'sclad/tovar.html', {'tovar': tov, 'username':auth.get_user(request).username})
    
def scladtov_new(request):
    if request.method == "POST":
        form = ScladTovForm(request.POST)
        if form.is_valid():
            tovarcik = form.save(commit=False)    
            tovarcik.myuser = request.user        
            tovarcik.save()
            return redirect('scladtov_edit', pk=tovarcik.pk)
    else:
        form = ScladTovForm()
    return render(request, 'sclad/scladtov_edit.html', {'ScladTovForm': form, 'username':auth.get_user(request).username})

def scladtov_edit(request, pk):
    tovarcik = get_object_or_404(ScladTov, pk=pk)
    if request.method == "POST":
        form = ScladTovForm(request.POST, instance=tovarcik)
        if form.is_valid():
            tovarcik = form.save(commit=False)
            tovarcik.save()
            #return redirect('scladtov_edit', pk=tovarcik.pk)
            if request.user.is_authenticated():
                Scladik = ScladTov.objects.filter(myuser=request.user).order_by('mytovars')
            else:
                Scladik = ScladTov.objects.order_by('mytovars')
            return render(request, 'sclad/minisclad.html', {'tovar': Scladik, 'username':auth.get_user(request).username})
    else:
        form = ScladTovForm(instance=tovarcik)
    return render(request, 'sclad/scladtov_edit.html', {'ScladTovForm': form, 'username':auth.get_user(request).username})

def scladtov_del(request, pk):
    tovarcik = get_object_or_404(ScladTov, pk=pk)
    tovarcik.delete()
    if request.user.is_authenticated():
        Scladik = ScladTov.objects.filter(myuser=request.user).order_by('mytovars')
    else:
        Scladik = ScladTov.objects.order_by('mytovars')
    return render(request, 'sclad/minisclad.html', {'tovar': Scladik, 'username':auth.get_user(request).username})

def login(request):
    args={}
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            login_error = "Пользователь не найден"
            args = {'login_error': login_error}
            return render(request, 'sclad/login.html',args)
    else:
        return render(request, 'sclad/login.html',args)

def logout(request):
    auth.logout(request)
    return redirect('/')
    
def scladtov_srokgod(request):
    mydate=datetime.today()
    tt=mydate.strftime("%y")
    god=int(tt)+1
    Scladik = ScladTov.objects.filter(srokgod=str(god)).order_by('mytovars')
    return render(request, 'sclad/minisclad1year.html', {'tovar': Scladik, 'username':auth.get_user(request).username})

def scladtov_srok2god(request):
    mydate=datetime.today()
    tt=mydate.strftime("%y")
    god=int(tt)+2
    Scladik = ScladTov.objects.filter(srokgod=str(god)).order_by('mytovars')
    return render(request, 'sclad/minisclad1year.html', {'tovar': Scladik, 'username':auth.get_user(request).username})

def scladtov_prosrocheno(request):
    mydate=datetime.today()
    tt=mydate.strftime("%y")
    god=int(tt)
    Scladik = ScladTov.objects.filter(srokgod=str(god)).order_by('mytovars')
    return render(request, 'sclad/minisclad1year.html', {'tovar': Scladik, 'username':auth.get_user(request).username})

def scladtov_minus(request, pk):
    tovarcik = get_object_or_404(ScladTov, pk=pk)
    tovarcik.kol = tovarcik.kol-1      
    tovarcik.save()
    if request.user.is_authenticated():
        Scladik = ScladTov.objects.filter(myuser=request.user).order_by('mytovars')
    else:
        Scladik = ScladTov.objects.order_by('mytovars')
    return render(request, 'sclad/minisclad.html', {'tovar': Scladik, 'username':auth.get_user(request).username})

def scladtov_plus(request, pk):
    tovarcik = get_object_or_404(ScladTov, pk=pk)
    tovarcik.kol = tovarcik.kol+1      
    tovarcik.save()
    if request.user.is_authenticated():
        Scladik = ScladTov.objects.filter(myuser=request.user).order_by('mytovars')
    else:
        Scladik = ScladTov.objects.order_by('mytovars')
    return render(request, 'sclad/minisclad.html', {'tovar': Scladik, 'username':auth.get_user(request).username})
    
   