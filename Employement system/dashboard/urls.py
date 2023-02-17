from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name="dashboard-index"),
    path('staff/', views.staff, name="dashboard-staff"),
    path('roles/', views.roles, name="dashboard-roles"),
    path('hired/', views.hired, name="dashboard-hired"),
    path('roles/delete/<int:pk>', views.roles_delete, name="dashboard-roles-delete"),
    path('roles/update/<int:pk>', views.roles_update, name="dashboard-roles-update"),
    path('staff/detail/<int:pk>/', views.staff_detail, name="dashboard-staff-detail"),
]