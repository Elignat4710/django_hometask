from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=200)
    com_name = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Worker(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=200)
    com_name = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WorkPlace(models.Model):
    name = models.CharField(max_length=200)
    worker_name = models.OneToOneField(Worker, on_delete=models.CASCADE, primary_key=True)
    work_name = models.ForeignKey(Work, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
