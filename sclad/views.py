from django.shortcuts import render
from .models import Category
from .models import Tovar
from .models import ScladTov

# Create your views here.
def tovar(request):
    tov = Tovar.objects.filter(category=Category.objects.get(full_name='Декоративная косметика')).order_by('full_name')
    Scladik = ScladTov.objects.filter(srokgod='20').order_by('mytovars')
   # Scladik = ScladTov.objects.All()
    return render(request, 'sclad/tovar.html', {'tovar': Scladik})