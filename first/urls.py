from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from posts.views import posts_list,post_detail,post_create,post_update,post_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',posts_list),
    path('posts/create/',post_create),
    path('posts/<slug:slug>/',post_detail),
    path('posts/<slug:slug>/update/',post_update),
    path('posts/<slug:slug>/delete/',post_delete),
    path('notes/',include(('notepad.urls','notepad'), namespace="notes")),
    path('news/',include(('news.urls','news'), namespace="news")),
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

