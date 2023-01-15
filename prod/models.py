from django.db import models
from django.urls import reverse

class Prod(models.Model):
    date = models.DateField(unique=True)
    boulanger = models.CharField(max_length=100, default="", null="")
    
    def get_absolute_url(self):
        return reverse('prod:prod_detail', kwargs={'pk': self.pk})

class Data(models.Model):
    prod_id = models.ForeignKey(Prod, on_delete=models.CASCADE)
    T80 = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    BuchNat = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    BuchMG = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    BuchRN = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    BuchNoix = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    RizSar = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    PetEp = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    Brioche = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    Cookies = models.IntegerField(default=0)


