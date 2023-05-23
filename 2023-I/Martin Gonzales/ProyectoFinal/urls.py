from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.urls import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/",include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="inicio.html"), name="inicio"),
    path('App1/',include('App1.urls'))
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
   


