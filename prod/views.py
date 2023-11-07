from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    FormView,
)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Sum

from .models import Data, Prod
from .forms import ProdFormset, ProdFormSetHelper
from .recettes import formatteur_de_recettes
from .filters import ProdFilter


class HomeView(TemplateView):
    template_name = "home.html"


class ProdListView(ListView):
    model = Prod
    template_name = "prod_list.html"

    def get_context_data(self, **kwargs):
        # Get original context
        context = super(ProdListView, self).get_context_data(**kwargs)
        # Add the filter
        prodFilter = ProdFilter(self.request.GET, queryset=context["prod_list"])
        prod_list = prodFilter.qs
        # rebuild context
        context["prodFilter"] = prodFilter
        context["prod_list"] = prod_list
        return context


class ProdDetailView(DetailView):
    model = Prod
    template_name = "prod_detail.html"


class ProdCreateView(CreateView):
    model = Prod
    template_name = "prod_create.html"
    fields = ["date", "boulanger"]


class ProdEditView(SingleObjectMixin, FormView):
    model = Prod
    template_name = "prod_edit.html"
    extra_context = {"helper": ProdFormSetHelper}
    data_entries = None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Prod.objects.all())

        # Retrieve the related Data entries for this Prod
        self.data_entries = self.object.data_set.all()

        # Calculate the sums of each element
        sums = [
            ("T80", self.data_entries.aggregate(Sum("T80"))["T80__sum"]),
            ("BuchNat", self.data_entries.aggregate(Sum("BuchNat"))["BuchNat__sum"]),
            ("BuchMG", self.data_entries.aggregate(Sum("BuchMG"))["BuchMG__sum"]),
            ("BuchRN", self.data_entries.aggregate(Sum("BuchRN"))["BuchRN__sum"]),
            ("BuchNoix", self.data_entries.aggregate(Sum("BuchNoix"))["BuchNoix__sum"]),
            # Add more elements as needed
        ]

        # Include sums in extra context
        self.extra_context["sums"] = sums
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Prod.objects.all())
        print("POST Called in ProdEditView")
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None):
        formset = ProdFormset(**self.get_form_kwargs(), instance=self.object)
        return formset

    def form_valid(self, form):
        if form.is_valid():
            print("Form is valid!")
            form.save()
            messages.add_message(self.request, messages.SUCCESS, "Changes were saved.")
            return HttpResponseRedirect(self.get_success_url())
        else:
            print("Form is invalid. Validation errors:")
            for field, errors in form.errors.items():
                print(f"{field}: {', '.join(errors)}")
            return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse("prod:prod_detail", kwargs={"pk": self.object.pk})

    def form_invalid(self, form):
        print("Form is invalid...")
        print("form.error =")
        print(form.errors)

        # You can skip the following lines if they are not needed:
        self.object_list = self.get_queryset()
        context = self.get_context_data(task_form=form)

        print("form context")
        print(context)

        return self.render_to_response(context)


class FicheProdView(DetailView):
    model = Prod
    template_name = "ficheprod.html"

    def get_context_data(self, **kwargs):
        # Get original context
        context = super(FicheProdView, self).get_context_data(**kwargs)

        # Make my custom context.
        ## First get the Fours related to that prod
        QS = Data.objects.filter(prod_id__pk=self.object.pk)

        ## Pour chaque four, obtenir les recettes
        recettes = []
        for four in QS:
            print("Four ", four)
            rcp = formatteur_de_recettes(four)
            recettes.append(rcp)
        context = {"prod": list(QS), "recettes": recettes}
        print(f"context = {context}")
        return context

    def get_success_url(self):
        return reverse(
            "prod:fiche_prod",
            kwargs={"pk": self.object.pk},
        )
