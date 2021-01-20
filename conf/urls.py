from django.contrib import admin
from django.urls import path

from job_search.views import MainView, ListVacancyView, DetailVacancyView, DetailCompanyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', ListVacancyView.as_view()),
    path('vacancies/cat/<str:code>/', ListVacancyView.as_view()),  # join with previous by re_path
    path('vacancies/<int:pk>/', DetailVacancyView.as_view()),
    path('companies/<int:pk>/', DetailCompanyView.as_view()),
]
