from django.urls import path

from . import views
app_name='FBEngagementPredict'
urlpatterns = [
    path('', views.home, name='home'),
    path('process/',views.process,name="process"),
    path('process/results/', views.results, name='results'),
    path('process/final',views.final,name="results")
]