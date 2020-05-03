
# ? config/urls.py と appごとのviewをつなげるurl.py module
from django.urls import path
from . import views

# ? ログイン機能を実装するために authのviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ? path(route, func, name='')
    path('', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'),
         name='logout'),
    path('profile/', views.AccountCreateView.as_view(), name='account-create')
]
