from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.IntegerField()
    id_num = models.IntegerField()
