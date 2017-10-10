from django.shortcuts import render

# Create your views here.
def tovar(request):
    return render(request, 'sclad/tovar.html', {})