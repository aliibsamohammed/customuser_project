from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from dateutil.relativedelta import relativedelta
from django.core.validators import FileExtensionValidator
from django.conf import settings
from .utils.misc import validate_age, user_directory_path, validate_file_size, validate_phone_number

class CustomUser(AbstractUser):
    # These are the fields we want on top of the fields included
    #  with the built-in Django User Model that come with:
    #  username, first_name, last_name, email, password, ....
    gender = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Gender'))
    dob = models.DateField(null=True, blank=True, validators=[validate_age], verbose_name=_('Date of birth'))
    role = models.CharField(max_length=10, blank=True, null=True, default="", verbose_name=_('Role'))  
    mobile_phone = models.CharField(max_length=15, blank=True, null=True, verbose_name=_('Mobile Phone'),
                                        validators=[validate_phone_number],)

    profile_photo = models.ImageField(default='avatar.png', upload_to=user_directory_path, 
                                    verbose_name=_('Profile Photo'), validators=[validate_file_size, 
                                    FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg', 'gif',])])

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Joined'))
    date_mod = models.DateField(default=timezone.now, verbose_name=_('Date Modified'))

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    def __str__(self):
        return self.username

    def age(self):
        if self.dob == None:
            return None
        age = relativedelta(date.today(), self.dob)
        return age.years


class Activation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)