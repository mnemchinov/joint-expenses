from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

admin.site.site_title = 'Заказы на кофе'
admin.site.site_header = 'Кофе в офис'
admin.site.index_title = 'Заказы на кофе в офис'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='admin/')),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(
            settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT
        )
        urlpatterns += staticfiles_urlpatterns()
