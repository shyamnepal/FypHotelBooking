from django.db import models


class Signup(models.Model):
    firstName = models.CharField(max_length=200, null=False, blank=False)
    lastName = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    confirmPassword = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.firstName

