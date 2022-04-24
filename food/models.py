from django.db import models


# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://jeffs-burger.ch/wp-content/uploads/2020/12/gst-default-placeholder-4-1024x1024.jpg")
    def __str__(self):
        return self.item_name
