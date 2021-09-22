from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import os
import string
import random
import uuid
from datetime import date
from django.core.exceptions import ValidationError
from dateutil.relativedelta import relativedelta


def get_random_secret_key():
    """
    Return a 50 character random string usable as a SECRET_KEY setting value.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)


 # The function for finding a key in the list
def linearSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def validate_file_size(value):
    filesize = value.size

    if filesize > 1048576:
        raise ValidationError(
            _("The maximum file size that can be uploaded is 1MB"))
    else:
        return value

def validate_age(date):
    if date == None:
        return None
    age = relativedelta(date.today(), date)
    if age.years < 18:
        raise ValidationError(
            _("Age limit restricted, the minimum age limit is 18 years"))
    else:
        return date

def validate_phone_number(numchar):
    plus_char = numchar[0]
    pos_int = int(numchar[1:])

    if plus_char[0] != '+':
        raise ValidationError(
            _("The phone number must start with area_code preceded by + sign"))
    if not pos_int:
        raise ValidationError(
            _("The phone number must be + sign followed by positiveinteger with out spaces"))
    else:
        return numchar

def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "png", "gif"]:
        sub_folder = "profile/"
    if ext.lower() in ["pdf", "docx"]:
        sub_folder = "document/"
    return os.path.join(sub_folder, str(instance.id), filename)


def send_mail(to, template, context):
    html_content = render_to_string(f'accounts/emails/{template}.html', context)
    text_content = render_to_string(f'accounts/emails/{template}.txt', context)

    msg = EmailMultiAlternatives(context['subject'], text_content, settings.DEFAULT_FROM_EMAIL, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_activation_email(request, email, code):
    context = {
        'subject': _('Profile activation'),
        'uri': request.build_absolute_uri(reverse('accounts:activate', kwargs={'code': code})),
    }

    send_mail(email, 'activate_profile', context)


def send_activation_change_email(request, email, code):
    context = {
        'subject': _('Change email'),
        'uri': request.build_absolute_uri(reverse('accounts:change_email_activation', kwargs={'code': code})),
    }

    send_mail(email, 'change_email', context)


def send_reset_password_email(request, email, token, uid):
    context = {
        'subject': _('Restore password'),
        'uri': request.build_absolute_uri(
            reverse('accounts:restore_password_confirm', kwargs={'uidb64': uid, 'token': token})),
    }

    send_mail(email, 'restore_password_email', context)


def send_forgotten_username_email(email, username):
    context = {
        'subject': _('Your username'),
        'username': username,
    }

    send_mail(email, 'forgotten_username', context)