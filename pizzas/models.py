from django.db import models
# Create your models here.

#u - admin p - John0118

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza_name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    toppings = models.TextField()

    def __str__(self):
        return self.toppings

class Image(models.Model):
    pizza_name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')



class Comments(models.Model):
    pizza_name = models.ForeignKey(Pizza, related_name='details', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.text