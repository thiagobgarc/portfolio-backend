from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    def __str__(self):
        model_name = self.__class__.__name__
        fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
        return f"{model_name}({fields_str})"
