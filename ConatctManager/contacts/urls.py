from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('',views.contact_list, name='contact_list'),#Static Route
    path('add/',views.add_contact, name='add_contact'),
    path('<int:pk>/', views.contact_detail, name='contact_detail')
]
