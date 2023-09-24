from django.db import models

class Interests(models.Model):
    interest = models.CharField(max_length=50)
    def __str__(self):
        return self.interest