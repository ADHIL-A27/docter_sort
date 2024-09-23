from django.urls import path
from .views import DoctoresView

urlpatterns = [
    path('doctores', DoctoresView.as_view(), name='hello_world'),
]
