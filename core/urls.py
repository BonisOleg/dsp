from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("healthz/", views.healthz, name="healthz"),
    path("callback/", views.callback_view, name="callback"),
    path("contact/", views.contact_view, name="contact"),
]
