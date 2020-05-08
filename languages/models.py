from django.db import models

# Create your models here.

class paradigm(models.Model):
    name=models.CharField(max_length=40)

    def __str__(self):
       return self.name

class languages(models.Model):
    name = models.CharField(max_length=40)
    paradigm = models.ForeignKey(paradigm, on_delete=models.CASCADE)

    def __str__(self):
       return self.name

class programmer(models.Model):
    name = models.CharField(max_length=40)
    lang = models.ManyToManyField(languages)

    def __str__(self):
        return self.name
