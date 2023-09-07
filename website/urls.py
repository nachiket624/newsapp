from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:category>', views.showcat, name='showcat'),
    path('read/<int:id>', views.read, name='read'),
    path('hread/<int:id>', views.heroread, name='hread'),
   

]