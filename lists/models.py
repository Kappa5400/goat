from django.db import models

<<<<<<< HEAD

class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
=======
# Create your models here.
class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)


>>>>>>> 7f777d47fb42514aeab1dc28db82375ee44209e0
