from django.urls import path
from .views import list_pessoas, create_pessoas, update_pessoas, delete_pessoas

urlpatterns = [
    path('', list_pessoas, name='list_pessoas'),
    path('new', create_pessoas, name='create_pessoas'),
    path('update/<int:id>/', update_pessoas, name='update_pessoas'),
    path('delete/<int:id>', delete_pessoas, name='delete_pessoas')
]

#CRUD - CREATE, READ, UPDATE, DELETE