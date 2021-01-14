from django.db import models

class APIKey(models.Model):
    email = models.EmailField()
    key = models.CharField(max_length=40, help_text="Enter your API Key")

    def __str__(self):
        return f"{self.key} | {self.email}"
