from django.db import models

class Weather(models.Model):
    city = models.CharField(max_length=100)  # Nome da cidade
    temperature = models.CharField(max_length=10)  # Temperatura como string
    description = models.CharField(max_length=255)  # Descrição do clima
    date = models.DateTimeField(auto_now_add=True)  # Data de quando os dados foram registrados

    def __str__(self):
        return f"{self.city} - {self.temperature} - {self.description}"

