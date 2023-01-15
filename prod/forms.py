from django import forms 
from .models import Data, Prod
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper, Layout 
from crispy_forms.layout import Submit, Field, Row, Column, Fieldset, Div, HTML

ProdFormset = inlineformset_factory(
    Prod, Data,
    fields=('prod_id','T80','BuchNat','BuchNoix','BuchMG','BuchRN','RizSar','PetEp','Brioche','Cookies'),
    labels={
        "T80":"T80",
        "BuchNat":"B. Nature",
        "BuchNoix":"B. Noix",
        "BuchMG":"B. Graines",
        "BuchRN":"B. R.N.",
    }
    )

class ProdFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ProdFormSetHelper, self).__init__(*args, **kwargs)
        
        
        self.layout = Layout(
            #HTML("<hr>"),
            Field('prod_id', type="hidden"),
            Div(
                Field('T80', fieldsstr="Semi complet T80",wrapper_class='col-md-1 form-control'),
                Field('RizSar', wrapper_class='col-md-1 form-control'),
                Field('PetEp', wrapper_class='col-md-1 form-control'),
                
                Field('BuchNat', wrapper_class='col-md-1 form-control'),
                Field('BuchRN', wrapper_class='col-md-1 form-control'),
                Field('BuchMG', wrapper_class='col-md-1 form-control'),  
                Field('BuchNoix', wrapper_class='col-md-1 form-control'), 
                
                
                Field('Brioche', wrapper_class='col-md-1 form-control'),
                Field('Cookies', wrapper_class='col-md-1 form-control'), 
            css_class='row input-group mt-2 mb-2'),
        )
        
        #self.template = 'bootstrap/table_inline_formset.html'
        #self.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.form_method = 'POST'
        self.form_tag = False #Otherwise HTML input button do not work !
        

