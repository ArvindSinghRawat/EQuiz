from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),   
    url(r'^$', include('EQuiz.urls')),
    url(r'^Users/', include('Users.urls')),
    url(r'^QuizAdmin/', include('QuizAdmin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
