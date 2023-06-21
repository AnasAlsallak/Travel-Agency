from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from tagency.views import Home # new

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")), # new
    path("", include("pages.urls")), # new
    path('', include('tagency.urls')), # new
    path("", Home.as_view(), name="home"), # new

]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
