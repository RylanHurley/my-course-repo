from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='index'),  # Home page showing course list
    path('registration/', views.registration_request, name='registration'),  # User registration page
    path('login/', views.login_request, name='login'),  # User login page
    path('logout/', views.logout_request, name='logout'),  # User logout page
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),  # Course detail page
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),  # Enroll in a course
    path('<int:course_id>/submit/', views.submit, name='submit'),  # Submit exam for a course
    path('<int:course_id>/show_exam_result/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),  # Show exam result for a course
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
