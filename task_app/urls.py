from django.urls import path

from task_app import views

urlpatterns = [
   path('',views.study_list,name='study_list'),
   path('add/', views.add_study, name='add_study'),
    path('edit/<int:pk>/', views.edit_study, name='edit_study'),
    path('delete/<int:pk>/', views.delete_study, name='delete_study')
]