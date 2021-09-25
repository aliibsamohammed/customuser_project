from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

from accounts.views import IndexPageView, AboutView, ChangeLanguageView, set_timezone

admin.site.site_header = 'CustomUser Administration'
admin.site.site_title = 'CustomUser Site Admin'
admin.site.index_title = 'CustomUser Site Admin Home'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexPageView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('accounts/', include('accounts.urls')),
    
    path('rest-auth/', include('rest_auth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),
    
    path('timezone/', set_timezone, name='set_timezone'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]