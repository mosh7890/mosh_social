from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponse
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic.base import RedirectView

from .views import index

urlpatterns = [
    path('favicon.ico',
         RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'), permanent=False)),
    path('robots.txt',
         lambda x: HttpResponse('User-Agent: *\nDisallow:', content_type='text/plain'), name='robots_file'),
    path('', index, name='index'),
    path('admin/login/', admin.site.urls),
    path('api/', include('posts.urls')),
    path('api/', include('users.urls')),
    *static(settings.STATIC_URL, document_root=settings.STATIC_URL),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.DEBUG:
    urlpatterns += [
        path('400/', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}, ),
        path('403/', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}, ),
        path('404/', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}, ),
        path('500/', default_views.server_error),
    ]

    if getattr(settings, 'TOOLBAR', False):
        # noinspection PyPackageRequirements
        import debug_toolbar

        urlpatterns += [
            path('__debug__/', include(debug_toolbar.urls)),
        ]
