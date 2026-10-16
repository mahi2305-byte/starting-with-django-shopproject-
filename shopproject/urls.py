
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/',
         auth_views.LoginView.as_view(             #predefined(show krta hai template ko )
             template_name = 'registration/login.html',
             redirect_authenticated_user = True,
            ), name = 'login')
]
