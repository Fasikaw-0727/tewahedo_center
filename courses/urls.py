from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # List all courses
    path('<int:pk>/', views.course_detail, name='course_detail'),  # Course detail
    path('register/', views.register, name='register'),  # User registration
    path('counseling/', views.counseling_form, name='counseling_form'),  # Counseling form
    path('counseling/success/', views.counseling_success, name='counseling_success'),  # Success page
    path('counseling/admin/', views.counseling_requests_list, name='counseling_requests_list'),  # Admin view
    path('enrolled/', views.enrolled_courses, name='enrolled_courses'),  # Add this line
]
