from django.shortcuts import render
from django.http import HttpResponse

def calculatorView(request):
    return render(request, 'calc.html')

def scitat(request):
    try:
        cislo1 = float(request.POST["cislo1"])
        cislo2 = float(request.POST["cislo2"])
        vysledek = cislo1 + cislo2
        return render(request, 'result.html', {"vysledek": vysledek})
    except:
        return HttpResponse('Pouzivejte jen cislo! ')

def odcitat(request):
    try:
        cislo1 = float(request.POST["cislo1"])
        cislo2 = float(request.POST["cislo2"])
        vysledek = cislo1 - cislo2
        return render(request, 'result.html', {"vysledek": vysledek})
    except:
        return HttpResponse('Pouzivejte jen cislo! ')

def delit(request):
    try:
        cislo1 = float(request.POST["cislo1"])
        cislo2 = float(request.POST["cislo2"])
        vysledek = cislo1 / cislo2
        return render(request, 'result.html', {"vysledek": vysledek})
    except:
        return HttpResponse('Pouzivejte jen cislo! ')

def nasobit(request):
    try:
        cislo1 = float(request.POST["cislo1"])
        cislo2 = float(request.POST["cislo2"])
        vysledek = cislo1 * cislo2
        return render(request, 'result.html', {"vysledek": vysledek})
    except:
        return HttpResponse('Pouzivejte jen cislo! ')

def hlavni(request):
    if request.POST['co'] == "plus":
        return scitat(request)
    if request.POST['co'] == "minus":
        return odcitat(request)
    if request.POST['co'] == "deleno":
        return delit(request)
    if request.POST['co'] == "krat":
        return nasobit(request)

    return HttpResponse('Nevim co mam pocitat! ')
