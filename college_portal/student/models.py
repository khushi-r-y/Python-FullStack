
from django.db import models

class Student_table(models.Model):
    reg_no = models.IntegerField()
    name = models.CharField(max_length=20)
    email = models.EmailField(default='example@gmail.com')
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateTimeField()

def __str__(self):
        return super().__str__()
