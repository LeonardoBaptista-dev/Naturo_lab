from django.contrib import admin
from django.urls import path, include
from autenticacao import views

urlpatterns = [
    path('', views.cadastro, name="cadastro"),
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    

]
