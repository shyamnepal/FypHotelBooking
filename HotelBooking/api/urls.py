from django.urls import path
from .import views


urlpatterns = [
    path('person-details/', views.showall, name='person-details')
]