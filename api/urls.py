
from django.urls import path

from .import views

urlpatterns = [
    path('', views.apiOverview),
    path('emplist/',views.empList, name='emplist'),
    path('empdetail/<str:pk>/', views.empDetail),
    path('empcreate/',views.empCreate),
    path('empupdate/<str:pk>/', views.empUpdate),
    path('empdelete/<str:pk>/', views.empDelete)
    
]
