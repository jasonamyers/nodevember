from django.conf.urls.defaults import patterns, url


urlpatterns = patterns("nodevember.api.views",
    url(r"^schedule_json/$", "schedule_json", name="schedule_json"),
)
