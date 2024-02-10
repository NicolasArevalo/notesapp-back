from django.urls import path
from . import views

# U in links stands for UPDATE

urlpatterns = [
    #path('', views.getRoutes, name="routes"),
    path('notes/', views.notes, name="notes"),
    #path('notes/create', views.addNote, name="create-note"),
    #path('notes/u/<str:pk>', views.updateNote, name="update-note"),
    #path('notes/d/<str:pk>', views.deleteNote, name="delete-note"),
    path('notes/<str:pk>', views.note, name="note"),
]