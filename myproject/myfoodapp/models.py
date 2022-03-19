from django.db import models
from datetime import datetime

# Create your models here.
class Kid(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    age = models.IntegerField()
    parent_phone = models.CharField(max_length=122)
    parent_email = models.EmailField(max_length=122)

    def __str__(self):
        return self.name

class Image(models.Model):
    kid_id = models.ForeignKey(Kid, on_delete=models.DO_NOTHING)
    img_url = models.ImageField()
    created_on = models.DateTimeField()
    updated_on = datetime.now()
    is_approved = models.BooleanField()
    approved_by = models.CharField(max_length=122)
    food_group = models.CharField(max_length=122)

    def __str__(self):
        return str(self.kid_id)