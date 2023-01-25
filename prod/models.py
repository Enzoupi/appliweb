from django.db import models
from django.urls import reverse

class Prod(models.Model):
    date = models.DateField(unique=True)
    boulanger = models.CharField(max_length=100, default="", null="")
    
    def get_absolute_url(self):
        return reverse('prod:prod_detail', kwargs={'pk': self.pk})

class Data(models.Model):
    prod_id = models.ForeignKey(Prod, on_delete=models.CASCADE)
    T80 = models.FloatField(default=0)
    BuchNat = models.FloatField(default=0)
    BuchMG = models.FloatField(default=0)
    BuchRN = models.FloatField(default=0)
    BuchNoix = models.FloatField(default=0,)
    RizSar = models.FloatField(default=0,)
    PetEp = models.FloatField(default=0,)
    Brioche = models.FloatField(default=0,)
    Cookies = models.IntegerField(default=0)


