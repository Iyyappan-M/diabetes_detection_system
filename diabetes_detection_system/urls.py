from django.contrib import admin
from django.urls import path, include
from users.views import home, register_view, login_view, logout_view, admin_login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin_login/', admin_login_view, name='admin_login'),
    path('prediction/', include('prediction.urls')),
]
