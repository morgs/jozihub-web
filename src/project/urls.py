from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    (r'^', include('%s.urls' % settings.PROJECT_NAME)),
    
    (r'^', include('tunobase.corporate.company_info.contact.urls')),
    (r'^eula/', include('tunobase.eula.urls')),
    (r'^bulk-loading/', include('tunobase.bulk_loading.urls')),
    (r'^newsletter/', include('tunobase.corporate.company_info.newsletter.urls')),
    (r'^corporate/media/', include('tunobase.corporate.media.urls')),
    (r'^age-gate/', include('tunobase.age_gate.urls')),
    (r'^blog/', include('tunobase.blog.urls')),
    (r'^commenting/', include('tunobase.commenting.urls')),
    (r'^tagging/', include('tunobase.tagging.urls')),
    (r'^poll/', include('tunobase.poll.urls')),
    (r'^tunosocial/', include('tunobase.social_media.tunosocial.urls')),
    (r'^facebook/', include('tunobase.social_media.facebook.urls')),
    (r'^twitter/', include('tunobase.social_media.twitter.urls')),
    (r'^google-plus/', include('tunobase.social_media.google_plus.urls')),
    (r'^console/', include('tunobase.console.urls')),
    (r'^console/media/', include('tunobase.corporate.media.console.urls')),
    
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^secure/ckeditor/', include('ckeditor.urls')),
)

#------------------------------------------------------------------------------
# Django serves media
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve', 
         {'document_root' : settings.MEDIA_ROOT, 
          'show_indexes': True}
         ),
    )
