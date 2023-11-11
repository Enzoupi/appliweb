from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save


boulanger_list = [
    ("Enzo", "Enzo"),
    ("Julien", "Julien"),
    ("Simon", "Simon"),
    ("Abi", "Abi"),
    ("Afouane", "Afouane"),
    ("Marianne", "Marianne"),
    ("Hugo", "Hugo"),
    ("Estelle", "Estelle"),
    ("Martin", "Martin"),
    ("Bastien", "Bastien"),
]


class Prod(models.Model):
    date = models.DateField(unique=True)
    boulanger = models.CharField(
        max_length=100, default="", null="", choices=boulanger_list
    )

    def get_absolute_url(self):
        return reverse("prod:prod_detail", kwargs={"pk": self.pk})

    @property
    def total_sum(self):
        childs = Data.objects.filter(prod_id=self)
        total = sum([c.total for c in childs])
        return total

    def get_data_sums(self):
        # Get all Data instances related to this Prod
        data_instances = Data.objects.filter(prod_id=self)

        # Initialize a dictionary to store the sums
        sums_dict = {
            "T80": 0,
            "BuchNat": 0,
            "BuchMG": 0,
            "BuchRN": 0,
            "BuchNoix": 0,
            "RizSar": 0,
            "PetEp": 0,
            "Brioche": 0,
            "Cookies": 0,
        }

        # Calculate the sums for each field
        for data_instance in data_instances:
            for field in sums_dict:
                sums_dict[field] += getattr(data_instance, field, 0)

        return sums_dict


class Data(models.Model):
    prod_id = models.ForeignKey(Prod, on_delete=models.CASCADE)
    T80 = models.FloatField(default=0)
    BuchNat = models.FloatField(default=0)
    BuchMG = models.FloatField(default=0)
    BuchRN = models.FloatField(default=0)
    BuchNoix = models.FloatField(
        default=0,
    )
    RizSar = models.FloatField(
        default=0,
    )
    PetEp = models.FloatField(
        default=0,
    )
    Brioche = models.FloatField(
        default=0,
    )
    Cookies = models.IntegerField(default=0)

    @property
    def total(self):
        return (
            self.T80
            + self.BuchNat
            + self.BuchMG
            + self.BuchRN
            + self.BuchNoix
            + self.RizSar
            + self.PetEp
            + self.Brioche
        )

    def non_zero(self):
        non_zero_items = []
        for pain, qtt in self.__dict__.items():
            if qtt != 0:
                non_zero_items.append(pain)

        to_remove = ["_state", "id", "prod_id_id", "prod_id"]
        non_zero_items = [
            element for element in non_zero_items if element not in to_remove
        ]
        return non_zero_items

    def types_de_pains(self):
        return [
            "T80",
            "BuchNat",
            "BuchMG",
            "BuchRN",
            "BuchNoix",
            "RizSar",
            "PetEp",
            "Brioche",
            "Cookies",
        ]


class Recipe(models.Model):
    # On le lie avec un four et un type de pain
    four_id = models.ForeignKey(Data, on_delete=models.CASCADE)
    four_pain = models.CharField(max_length=50, default="Brioche")
    # Farines
    FT80 = models.FloatField(default=0)
    ST170 = models.FloatField(default=0)
    PET80 = models.FloatField(default=0)
    RT80 = models.FloatField(default=0)
    SarT80 = models.FloatField(default=0)
    FPDT = models.FloatField(default=0)
    # Basiques
    eau = models.FloatField(default=0)
    sel = models.FloatField(default=0)
    oeufs = models.FloatField(default=0)
    sucre = models.FloatField(default=0)
    beurre = models.FloatField(default=0)
    levain = models.FloatField(default=0)
    # Graines et fruits
    raisin = models.FloatField(default=0)
    noisettes = models.FloatField(default=0)
    noix = models.FloatField(default=0)
    graines = models.FloatField(default=0)
    # divers
    levure = models.FloatField(default=0)

    def total_ingr(self):
        total = 0
        for ingr in self.non_zero():
            total += getattr(self, ingr)
        return total

    def non_zero(self):
        non_zero_items = []
        for pain, qtt in self.__dict__.items():
            if qtt != 0:
                non_zero_items.append(pain)

        to_remove = ["_state", "id", "four_id", "four_id_id", "four_pain"]
        non_zero_items = [
            element for element in non_zero_items if element not in to_remove
        ]
        return non_zero_items

    def __str__(self):
        string_init = f"{self.four_pain} [four {self.four_id}]("
        counter = 0
        for elem in self.non_zero():
            str_add = ""
            if counter > 0:
                str_add += ";"
            str_add += f"{elem}:{round(getattr(self,elem),2)}"
            string_init += str_add
            counter += 1
        string_init += ")"
        return string_init

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.four_id:
            # self.field_to_update = self.related_model.related_field
            kg = getattr(self.four_id, self.four_pain)

            if self.four_pain == "T80":
                self.FT80 = 0.6 * kg
                self.sel = 0.05 * kg
                self.eau = 0.4 * kg
                self.levain = 0.2 * kg

            elif self.four_pain == "BuchNat":
                self.FT80 = 0.6 * kg
                self.ST170 = 0.3 * kg
                self.sel = 0.05 * kg
                self.eau = 0.4 * kg
                self.levain = 0.2 * kg

            elif self.four_pain == "BuchMG":
                self.FT80 = 0.6 * kg
                self.ST170 = 0.3 * kg
                self.sel = 0.05 * kg
                self.eau = 0.4 * kg
                self.levain = 0.2 * kg
                self.graines = 0.07 * kg

            elif self.four_pain == "BuchRN":
                self.FT80 = 0.6 * kg
                self.ST170 = 0.3 * kg
                self.sel = 0.05 * kg
                self.eau = 0.4 * kg
                self.levain = 0.2 * kg
                self.noisettes = 0.1 * kg
                self.raisin = 0.1 * kg

            elif self.four_pain == "BuchNoix":
                self.FT80 = 0.6 * kg
                self.ST170 = 0.3 * kg
                self.sel = 0.05 * kg
                self.eau = 0.4 * kg
                self.levain = 0.2 * kg
                self.noix = 0.1 * kg

            elif self.four_pain == "RizSar":
                self.FT80 = 0.6 * kg
                self.sel = 0.05 * kg
                self.eau = 0.4 * kg
                self.levain = 0.2 * kg

            elif self.four_pain == "PetEp":
                self.FT80 = 0.6 * kg
                self.sel = 0.05 * kg
                self.eau = 0.4 * kg
                self.levain = 0.2 * kg

            elif self.four_pain == "Brioche":
                self.FT80 = 0.6 * kg
                self.sel = 0.05 * kg
                self.eau = 0.4 * kg
                self.levain = 0.2 * kg

            elif self.four_pain == "Cookies":
                self.FT80 = 0.6 * kg
                self.sel = 0.05 * kg
                self.eau = 0.4 * kg
                self.levain = 0.2 * kg

            else:
                raise ValueError(f"{self.four_pain} n'est pas une recette valide !")


# Signals for the relationship between Recipe and Data
def create_recipe(sender, instance, created, *args, **kwargs):
    if created:
        non_zero_items = instance.non_zero()

        for elem in non_zero_items:
            new_recipe = Recipe(four_id=instance, four_pain=elem)
            print(new_recipe.non_zero())
            new_recipe.save()
            print(new_recipe)
            print(f"Recipe for {elem} created")


post_save.connect(create_recipe, sender=Data)


def update_recipe(sender, instance, created, *args, **kwargs):
    if created == False:
        # First get all previous recipes and delete them
        previous = instance.recipe_set.all()
        previous.delete()
        # call create recipe
        create_recipe(sender, instance, True, *args, **kwargs)


post_save.connect(update_recipe, sender=Data)
