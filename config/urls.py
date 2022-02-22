import re

from django.conf import settings
from django.contrib import admin
from django.urls import re_path
from django.views.generic import RedirectView
from django.views.static import serve


admin.site.site_title = 'Заказы на кофе'
admin.site.site_header = 'Кофе в офис'
admin.site.index_title = 'Заказы на кофе в офис'

static_urls = re_path(
    r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')),
    serve,
    {'document_root': settings.STATIC_ROOT}
)


urlpatterns = [
    static_urls,
    re_path(r'^$', RedirectView.as_view(url='admin/orders/order/')),
    re_path(r'^admin/?', admin.site.urls),
    re_path(r'^admin/?', admin.site.urls),
]
