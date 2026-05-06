"""Utility helpers for the core app."""
from django.conf import settings
from django.core.mail import send_mail


def send_callback_notification(name: str, phone: str, message: str) -> None:
    """Send an email notification when a new callback request arrives."""
    subject = f"[Заявка на дзвінок] {name}"
    body = (
        f"Нова заявка на зворотний дзвінок:\n\n"
        f"Ім'я:      {name}\n"
        f"Телефон:   {phone}\n"
        f"Повідомлення:\n{message or '—'}\n"
    )
    _send(subject, body)


def send_contact_notification(name: str, email: str, message: str) -> None:
    """Send an email notification when a new contact message arrives."""
    subject = f"[Повідомлення] {name}"
    body = (
        f"Нове повідомлення з сайту:\n\n"
        f"Ім'я:   {name}\n"
        f"E-mail: {email}\n"
        f"Повідомлення:\n{message}\n"
    )
    _send(subject, body)


def _send(subject: str, body: str) -> None:
    recipient = getattr(settings, "NOTIFICATION_EMAIL", settings.DEFAULT_FROM_EMAIL)
    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )
    except Exception:
        # Log but don't raise — form data is already saved to DB
        import logging
        logging.getLogger(__name__).exception("Failed to send notification email")
