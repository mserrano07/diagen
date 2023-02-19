from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class KitInformation(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    sumary = models.CharField(max_length=150)
    file = models.FileField(upload_to='upload/', null=True, blank=True)
    public = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Consumables(models.Model):
    name = models.CharField(max_length=150)
    size = models.CharField(max_length=80)
    location = models.CharField(max_length=250)
    stock = models.IntegerField(default=0)
    batch_code = models.CharField(max_length=150)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Reagent(models.Model):

    name = models.CharField(max_length=150)
    exp_date = models.DateTimeField()
    size = models.CharField(max_length=80)
    weight = models.CharField(max_length=80)
    location = models.CharField(max_length=250)
    type_ac = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    batch_code = models.CharField(max_length=150)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LoteKit(models.Model):
    code = models.CharField(max_length=150)
    stock = models.IntegerField(default=0)
    reactives = models.ManyToManyField(Reagent)
    kit_information = models.ForeignKey(KitInformation, on_delete=models.CASCADE)
    consumables = models.ManyToManyField(Consumables)
    exp_date = models.DateTimeField()

    def __str__(self):
        return self.code
