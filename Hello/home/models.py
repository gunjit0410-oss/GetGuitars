from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()

class Guitar(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=500, blank=True, null=True)
    amazon_link = models.URLField()
    flipkart_link = models.URLField(blank=True)

    def __str__(self):
        return self.name  


    


