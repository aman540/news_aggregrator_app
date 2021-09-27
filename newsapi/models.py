from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
      DOCTOR = 1
      NURSE = 2
      SURGEN =3
      
      ROLE_CHOICES = (
          (DOCTOR, 'Doctor'),
          (NURSE, 'Nurse'),
          (SURGEN, 'Surgen'),
      )
      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)