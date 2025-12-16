from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('Haircut', 'Haircut'),
        ('Shave', 'Shave'),
        ('Haircut + Shave', 'Haircut + Shave'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, default="0000000000") 
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.service} on {self.date}"
