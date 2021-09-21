from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('create_a_native/', views.create_a_native),
    path('create_a_cohort/', views.create_a_cohort),
    path('fetch_a_native/', views.fetch_a_native)
]
