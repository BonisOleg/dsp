from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_GET

from .forms import CallbackRequestForm, ContactMessageForm
from .models import GalleryImage, Product
from .utils import send_callback_notification, send_contact_notification


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "products": Product.objects.filter(is_visible=True).prefetch_related("specs"),
            "gallery_items": GalleryImage.objects.filter(is_visible=True),
        }
        return render(request, "core/index.html", context)


@require_GET
def healthz(request: HttpRequest) -> HttpResponse:
    return HttpResponse("OK", content_type="text/plain")


# ── Callback (заявка на дзвінок) ────────────────────────────────────────────

def callback_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CallbackRequestForm(request.POST)
        if form.is_valid():
            obj = form.save()
            send_callback_notification(obj.name, obj.phone, obj.message)
            return render(
                request,
                "core/partials/form_success.html",
                {"kind": "callback"},
            )
        return render(request, "core/partials/callback_form.html", {"form": form})

    form = CallbackRequestForm()
    return render(request, "core/partials/callback_form.html", {"form": form})


# ── Contact (написати) ───────────────────────────────────────────────────────

def contact_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            obj = form.save()
            send_contact_notification(obj.name, obj.email, obj.message)
            return render(
                request,
                "core/partials/form_success.html",
                {"kind": "contact"},
            )
        return render(request, "core/partials/contact_form.html", {"form": form})

    form = ContactMessageForm()
    return render(request, "core/partials/contact_form.html", {"form": form})
