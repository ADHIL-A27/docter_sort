from django.db import models

from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    experiences = models.JSONField()
    areas_of_expertise = models.JSONField()
    opd_timings = models.JSONField()
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)  # Store images in 'doctors/' directory


    def __str__(self):
        return self.name
