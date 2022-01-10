from django.contrib.auth.models import AbstractUser
from django.db import models


class ECGUser(AbstractUser):
    email = models.EmailField(unique=True, null=False)

    workplace = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    experience = models.TextField()

    info = models.TextField()

    def __str__(self):
        return f"ECGUser({self.email})"

    def __repr__(self):
        return f"ECGUser({self.email}, {self.id})"

