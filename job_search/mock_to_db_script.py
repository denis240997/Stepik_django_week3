# (venv) hamit@Precision-5510:~/Desktop/PycharmProjects/jumanji$ python manage.py shell
# Далее все содержимое копируем в интерактивную оболочку

import job_search.mock_data as md
from job_search.models import Company, Specialty, Vacancy

for company in md.companies:
    Company.objects.create(**company)

for specialty in md.specialties:
    Specialty.objects.create(**specialty)

for job in md.jobs:
    job['specialty'] = Specialty.objects.get(code=job['specialty'])
    job['company'] = Company.objects.get(id=job['company'])
    Vacancy.objects.create(**job)
