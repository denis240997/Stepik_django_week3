from django.db import models


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()

    def __str__(self):
        return f'Company {self.id} : {self.title}'


class Specialty(models.Model):
    code = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return f'Specialty {self.code} : {self.title}'


class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, related_name='vacancies', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)
    skills = models.CharField(max_length=1024)
    description = models.TextField()
    salary_from = models.IntegerField()
    salary_to = models.IntegerField()
    posted = models.DateField()

    def __str__(self):
        return f'Vacancy {self.id} : {self.title}'
