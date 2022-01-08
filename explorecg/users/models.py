from django.contrib.auth.models import AbstractUser
from django.db import models


class ECGUser(AbstractUser):
    login = models.CharField(unique=True, null=False, max_length=50)
    email = models.EmailField(unique=True, null=False)

    workplace = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    experience = models.TextField()

    info = models.TextField()

    def __str__(self):
        return f"ECGUser({self.login}, {self.email})"

    def __repr__(self):
        return f"ECGUser({self.login}, {self.id})"

