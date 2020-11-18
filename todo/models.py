from django.db import models

# Create your models here.

PRIORITY = (('danger','high'),('info','normal'),('success','low'))
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = PRIORITY
    )
    duedate = models.DateField()
    def __str__(self):
<<<<<<< HEAD
        return self.titlem
=======
        return self.titlem
>>>>>>> da6386698c765c6adc43569e0f1d9ab7088399e8
