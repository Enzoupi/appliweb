from django.urls import path

from . import views

app_name = "prod"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("prodlist/", views.ProdListView.as_view(), name="list_prod"),
    path("prodlist/<int:pk>/", views.ProdDetailView.as_view(), name="prod_detail"),
    path("add/", views.ProdCreateView.as_view(), name="add_prod"),
    path(
        "prodlist/<int:pk>/prod/edit/", views.ProdEditView.as_view(), name="prod_edit"
    ),
    path(
        "prodlist/<int:pk>/ficheprod/", views.FicheProdView.as_view(), name="fiche_prod"
    ),
    path(
        "prodlist/<int:prod_id>/<int:compare_id>/compare/",
        views.ProdEditCompareView.as_view(),
        name="prod_edit_compare",
    ),
]
