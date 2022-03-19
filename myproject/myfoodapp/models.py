from django.db import models
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Kid(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    age = models.IntegerField()
    parent_phone = models.CharField(max_length=122)
    parent_email = models.EmailField(max_length=122)

    def __str__(self):
        return str(self.id) + '-' + self.name

class Image(models.Model):
    kid_id = models.ForeignKey(Kid, on_delete=models.DO_NOTHING)
    img_url = models.ImageField()
    created_on = models.DateTimeField()
    updated_on = datetime.now()
    is_approved = models.BooleanField()
    approved_by = models.CharField(max_length=122)

    FRUIT = 'FRUIT'
    VEGETABLE = 'VEGETABLE'
    GRAIN = 'GRAIN'
    PROTEIN = 'PROTEIN'
    DAIRY = 'DAIRY'
    UNKNOWN = 'UNKNOWN'
    FOOD_CHOICES = [
        (FRUIT, 'Fruit'),
        (VEGETABLE, 'Vegetable'),
        (GRAIN, 'Grain'),
        (PROTEIN, 'Protein'),
        (DAIRY, 'Dairy'),
        (UNKNOWN, 'Unknown')
    ]

    food_group = models.CharField(max_length=20, choices=FOOD_CHOICES, default=UNKNOWN)

    def __str__(self):
        return str(self.kid_id) + ' - ' +str(self.img_url)

@receiver(post_save, sender=Image)
def send_mail_on_unknown(sender, instance, **kwargs):
        if instance.food_group == 'UNKNOWN':
            subject = "Image uploaded doesn't contain food"
            message = f"The image uploaded for {instance.kid_id.name} doesn't contain food. Please verify with your child."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [instance.kid_id.parent_email, ]
            send_mail(subject, message, email_from, recipient_list)