from django.urls import path
from App1 import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('gasto', login_required(views.gasto), name="Gasto"), # comando que requiere login para acceder a esta clase
    #path('gasto', views.gasto, name="Gasto"),
    path('ingreso', login_required(views.ingreso), name="Ingreso"), # comando que requiere login para acceder a esta clase
    #path('ingreso', views.ingreso, name="Ingreso"),
    path('trading', login_required(views.trading), name="Trading"), # comando que requiere login para acceder a esta clase
    #path('trading', views.trading, name="Trading"),

    path('gastoFormulario', views.gastoFormulario, name="GastoFormulario"),
    path('ingresoFormulario', views.ingresoFormulario, name="IngresoFormulario"),
    path('tradingFormulario', views.tradingFormulario, name="TradingFormulario"),
    
    path('busquedaGasto',views.busquedaGasto,name="BusquedaGasto"),
    path('buscarGasto/',views.buscarGasto),
    path('busquedaIngreso',views.busquedaIngreso,name="BusquedaIngreso"),
    path('buscarIngreso/',views.buscarIngreso),
    path('busquedaTrading',views.busquedaTrading,name="BusquedaTrading"), 
    path('buscar/',views.buscar),
    

    path('leerGastos',views.leerGastos,name='LeerGastos'),
    path('leerIngresos',views.leerIngresos,name='LeerIngresos'),
    path('leerTradings',views.leerTradings,name='LeerTradings'),

    path('eliminarGasto/<gasto_fecha>/', views.eliminarGasto, name="EliminarGasto"),
    path('eliminarIngreso/<ingreso_fecha>/', views.eliminarIngreso, name="EliminarIngreso"),
    path('eliminarTrading/<trading_fecha>/', views.eliminarTrading, name="EliminarTrading"),

    path('editarGasto/<gasto_fecha>/', views.editarGasto, name="EditarGasto"),
    path('editarIngreso/<ingreso_fecha>/', views.editarIngreso, name="EditarIngreso"),
    path('editarTrading/<trading_fecha>/', views.editarTrading, name="EditarTrading"),

    #path('gasto/list',views.GastoList.as_view(),name='List'),
    #path(r'^(?P<pk>\d+)$', views.GastoDetalle.as_view(),name='Detail'),
    #path(r'^nuevo$', views.GastoCreacion.as_view(),name='New'),
    #path(r'^editar/(?P<pk>\d+)$',views.GastoUpdate.as_view(),name='Edit'),
    #path(r'^borrar/(?P<pk>\d+)$',views.GastoDelete.as_view(),name='Delete'),

    #path('ingreso/list',views.IngresoList.as_view(),name='List'),
    #path(r'^(?P<pk>\d+)$', views.IngresoDetalle.as_view(),name='Detail'),
    #path(r'^nuevo$', views.IngresoCreacion.as_view(),name='New'),
    #path(r'^editar/(?P<pk>\d+)$',views.IngresoUpdate.as_view(),name='Edit'),
    #path(r'^borrar/(?P<pk>\d+)$',views.IngresoDelete.as_view(),name='Delete'),

    path('trading/list',views.TradingList.as_view(),name='List'),
    path(r'^(?P<pk>\d+)$', views.TradingDetalle.as_view(),name='Detail'),
    path(r'^nuevo$', views.TradingCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.TradingUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.TradingDelete.as_view(),name='Delete'),

    path('login',views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='App1/logout.html'), name='Logout'),

    path("my-page/", views.MyView.as_view(), name="my_page"),
    path("my-protected-page/", views.MyProtectedView.as_view(), name="my_protected_page"),

    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    path('aboutMe', views.aboutMe, name="AboutMe"),
    path('noEnviastesNada', views.noEnviastesNada, name="NoEnviastesNada"),

        

]


