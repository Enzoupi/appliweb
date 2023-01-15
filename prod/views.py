from django.views.generic import (TemplateView, ListView, CreateView, DetailView, FormView)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin

from .models import Data, Prod
from .forms import ProdFormset, ProdFormSetHelper
#from .forms import DataForm


class HomeView(TemplateView):
    template_name = 'home.html'


class ProdListView(ListView):
    model = Prod
    template_name = 'prod_list.html'


class ProdDetailView(DetailView):
    model = Prod
    template_name = 'prod_detail.html'

class ProdCreateView(CreateView):
    model = Prod
    template_name = 'prod_create.html'
    fields = ['date','boulanger']



    
class ProdEditView(SingleObjectMixin, FormView):

    model = Prod
    template_name = 'prod_edit.html'
    extra_context={'helper': ProdFormSetHelper}

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Prod.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Prod.objects.all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        return ProdFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form):
        print("Form is valid !")
        form.save()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved.'
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('prod:prod_detail', kwargs={'pk': self.object.pk})
    
    def form_invalid(self, form):
        print(f"Form is invalid...")
        print(form.errors)
        # Whatever you wanna do. This example simply reloads the list
        self.object_list = self.get_queryset()
        context = self.get_context_data(task_form=form)
        return self.render_to_response(context)


    

