from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    #Si no esta logueado igual anda el carro
    else:
        if "carrito" in request.session:
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    return {"total_carrito" : total}