from statistics import mode
from django.db import models

# Create your models here.
class Kid(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    age = models.IntegerField()
    parent_phone = models.CharField(max_length=122)
    parent_email = models.EmailField(max_length=122)

    def __str__(self):
        return self.id + self.name

class Image(models.Model):
    kid_id = models.ForeignKey(Kid, on_delete=models.DO_NOTHING)
    img_url = models.CharField(max_length=255)
    created_on = models.DateField()
    updated_on = models.DateField()
    is_approved = models.BooleanField()
    approved_by = models.CharField(max_length=122)
    food_group = models.CharField(max_length=122)