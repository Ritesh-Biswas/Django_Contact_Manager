from django.urls import path # type: ignore
from . import views
from .views import contact_list, add_contact, contact_detail, edit_contact

urlpatterns = [
     path('', views.home, name='home'),  # Home Page
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contacts/<int:contact_id>/edit/', views.edit_contact, name='edit_contact'),
    path('contacts/<int:contact_id>/delete/', views.delete_contact, name='delete_contact'),
]
