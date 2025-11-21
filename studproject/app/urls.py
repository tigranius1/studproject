from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('student/<int:student_id>/session/', views.edit_session, name='edit_session'),
    path('create-test-data/', views.create_test_data_view, name='create_test_data'),
]