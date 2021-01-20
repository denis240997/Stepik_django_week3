from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from job_search.models import Company, Specialty, Vacancy


class MainView(TemplateView):
    template_name = 'job_search/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['specialty_list'] = Specialty.objects.all()
        context['company_list'] = Company.objects.all()
        return context


class ListVacancyView(ListView):
    model = Vacancy
    context_object_name = 'vacancy_list'

    def get_queryset(self):
        if 'code' not in self.kwargs:
            return Vacancy.objects.all()
        if self.kwargs['code'] in {s.code for s in Specialty.objects.all()}:
            return Vacancy.objects.filter(specialty__code=self.kwargs['code'])
        raise Http404(f'There are no such specialty: \"{self.kwargs["code"]}\" !')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if 'code' not in self.kwargs:
            context['specialty_name'] = 'Все вакансии'
        else:
            try:
                context['specialty_name'] = Specialty.objects.get(code=self.kwargs['code']).title
            except Specialty.MultipleObjectsReturned:   # Specialty.DoesNotExist обработано в методе get_queryset
                raise Http404(f'There are more than one specialty with code \"{self.kwargs["code"]}\" !')

        return context


class DetailVacancyView(DetailView):
    model = Vacancy
    context_object_name = 'vacancy'


class DetailCompanyView(DetailView):
    model = Company
    context_object_name = 'company'
