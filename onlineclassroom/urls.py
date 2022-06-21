## @brief urls for the website.
from django.urls import include, re_path, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header = "I.T. Department Admin"
admin.site.site_title = "Department of I.T."
admin.site.index_title = "Welcome to I.T. Department Portal"


## @brief url patterns for the website.
urlpatterns = [
    path("", views.main_page, name='main_page'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^login/', views.login_user, name='login_user'),
    re_path(r'^register_user/$', views.register_user, name='register_user'),
    re_path(r'^register_instructor/$', views.register_instructor, name='register_instructor'),
    re_path(r'^logout/$', views.logout_user, name='logout_user'),
    re_path(r'^course/', include(('course.urls', 'course'), namespace='course')),
    re_path(r'^instructor/', include(('instructor.urls', 'instructor'), namespace='instructor')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)