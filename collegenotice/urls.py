from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home'),
    path("fulldetails/<int:id>", views.fulldetails, name="details"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handlelogout, name="handlelogout"),
    path('signup', views.handlesignup, name="handlesignup"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

