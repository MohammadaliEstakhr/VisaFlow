"""
This is a Python module in the VisaFlow project.
"""

from django.db import models

class VisaApplication(models.Model):
    applicant_name = models.CharField(max_length=100)
    visa_type = models.CharField(max_length=50)
    submission_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.applicant_name
