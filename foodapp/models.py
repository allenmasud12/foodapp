from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=200, default="")
    item_des = models.CharField(max_length=200, default="")
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://alllocal.ca/wp-content/uploads/2020/11/food-placeholder.png")

    def __str__(self):
        return self.item_name
