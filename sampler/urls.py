from django.conf.urls.defaults import *

urlpatterns = patterns(''
    ,url(r'^experiments/(?P<slug>[A-Za-z0-9_]+)/add_target$',
        'sampler.views.add_target')
    ,url(r'^tropo$', 'sampler.views.tropo')
    ,url(r'^experiments/(?P<slug>[A-Za-z0-9_]+)/experiencesamples.csv$',
        'sampler.views.experiencesamples_csv')
    ,url(r'^experiments/(?P<slug>[A-Za-z0-9_]+)/hilowgames.csv$',
        'sampler.views.hilowgames_csv')
)
