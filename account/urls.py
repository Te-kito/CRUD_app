
# ? config/urls.py と appごとのviewをつなげるurl.py module
from django.urls import path
from . import views

urlpatterns = [
    # ? path(route, func, name='')
    path('', views.signup, name='signup'),
]
