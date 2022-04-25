from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='raj'),
path('details',views.details)
]