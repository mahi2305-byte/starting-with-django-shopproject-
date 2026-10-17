
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            redirect_authenticated_user=True,
        ), name='login'),
    
    path('welcome/',
        login_required(TemplateView.as_view(
            template_name='welcome.html',
        )), name='welcome'),
    
    path('api/', include('customer.urls')),
]
