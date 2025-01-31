from django.urls import path # type: ignore
from . import views
from .views import contact_list, add_contact, contact_detail, edit_contact

urlpatterns = [
    path('',views.contact_list, name='contact_list'),#Static Route
    path('add/',views.add_contact, name='add_contact'),
    path('<int:pk>/', views.contact_detail, name='contact_detail'),
    path('<int:contact_id>/edit/', edit_contact, name='edit_contact'),
    path('<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
]
