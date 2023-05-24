from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("", views.base, name="home"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.log_out, name= "logout"),
    path("login/", views.log_in , name = "login"),
    path("profile/", views.profile, name = "profile"),
    path("profile/user/<id>", views.profileIndividual, name = "profileIndividual" ),
    path("user/edit/", views.edituser,  name = "edituser"),
    path("user/delete/<id>", views.deleteuser, name ="deleteuser"),
    path("profile/edit/", views.editprofile.as_view(), name = "editprofile"),
    path("about/", views.about, name = 'about')
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)