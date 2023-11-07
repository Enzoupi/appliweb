from django import forms
from .models import Data, Prod
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Div


class ProdForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = (
            "prod_id",
            "T80",
            "BuchNat",
            "BuchNoix",
            "BuchMG",
            "BuchRN",
            "RizSar",
            "PetEp",
            "Brioche",
            "Cookies",
        )
        labels = {
            "T80": "T80",
            "BuchNat": "B. Nature",
            "BuchNoix": "B. Noix",
            "BuchMG": "B. Graines",
            "BuchRN": "B. R.N.",
        }
        widgets = {
            "T80": forms.TextInput(attrs={"class": "form-control w-100"}),
            "BuchNat": forms.TextInput(attrs={"class": "form-control w-100"}),
            "BuchNoix": forms.TextInput(attrs={"class": "form-control w-100"}),
            "BuchMG": forms.TextInput(attrs={"class": "form-control w-100"}),
            "BuchRN": forms.TextInput(attrs={"class": "form-control w-100"}),
            "RizSar": forms.TextInput(attrs={"class": "form-control w-100"}),
            "PetEp": forms.TextInput(attrs={"class": "form-control w-100"}),
            "Brioche": forms.TextInput(attrs={"class": "form-control w-100"}),
            "Cookies": forms.TextInput(attrs={"class": "form-control w-100"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        print("Cleaned Data:", cleaned_data)
        # Your custom validation logic here
        return cleaned_data


ProdFormset = inlineformset_factory(
    Prod,
    Data,
    form=ProdForm,
    fields=(
        "prod_id",
        "T80",
        "BuchNat",
        "BuchNoix",
        "BuchMG",
        "BuchRN",
        "RizSar",
        "PetEp",
        "Brioche",
        "Cookies",
    ),
)


class ProdFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ProdFormSetHelper, self).__init__(*args, **kwargs)

        self.layout = Layout(
            Field("prod_id", type="hidden"),
            Div(
                Field(
                    "T80",
                    fieldsstr="Semi complet T80",
                    wrapper_class="col-md-1 form-control",
                ),
                Field("RizSar", wrapper_class="col-md-1 form-control"),
                Field("PetEp", wrapper_class="col-md-1 form-control"),
                Field("BuchNat", wrapper_class="col-md-1 form-control"),
                Field("BuchRN", wrapper_class="col-md-1 form-control"),
                Field("BuchMG", wrapper_class="col-md-1 form-control"),
                Field("BuchNoix", wrapper_class="col-md-1 form-control"),
                Field("Brioche", wrapper_class="col-md-1 form-control"),
                Field("Cookies", wrapper_class="col-md-1 form-control"),
                css_class="row input-group mt-2 mb-2",
            ),
        )

        self.form_method = "POST"
        self.form_tag = True
