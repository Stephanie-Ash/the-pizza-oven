from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_confirmation_email(booking):
    customer_email = booking.email
    subject = render_to_string(
        'bookings/confirmation_emails/confirmation_email_subject.txt',
        {'booking': booking})
    body = render_to_string(
        'bookings/confirmation_emails/confirmation_email_body.txt',
        {'booking': booking})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email]
    )
