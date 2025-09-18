from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename="employees")

urlpatterns = [
    path('students/', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),
    # path('employees/', views.Employees.as_view()), # class based view hoy atle 
    # path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('', include(router.urls)),
    path('blogs/', views.BlogView.as_view()),
    path('blogs/<int:pk>/', views.BlogDetailsView.as_view()),
    path('comments/', views.CommentsView.as_view()),
     path('comments/<int:pk>/', views.CommentsDetailsView.as_view()),
]
