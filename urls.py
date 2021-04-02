from django.contrib import admin
from django.urls import path
from hi.views import hiView
from calculator.views import calculatorView
from calculator.views import hlavni
from views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('hi/', hiView),
    path('calc/', calculatorView),
    path('calc/pocitej', hlavni),
]