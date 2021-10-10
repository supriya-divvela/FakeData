from django.db import models


class employee(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField()
    job=models.CharField(max_length=30)
    salary=models.IntegerField()
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.firstname