from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('rest_framework.urls')),
    path('poll/', include("surveys.urls")),
    path('question/', include("questions.urls")),
    path('vote/', include("vote.urls")),
]

urlpatterns += docs_urls
