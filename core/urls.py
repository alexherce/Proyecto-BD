from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

urlpatterns = patterns('',

 url(r'^$', coreviews.LandingView.as_view()),
 url(r'app/$', login_required(coreviews.LandingSelectView.as_view()), name='select_page'),
 
# -------------------------------------------------
# RESTAURANTS
# -------------------------------------------------

 url(r'app/restaurants/$', coreviews.LocationRestaurantListView.as_view(), name='res_page'),
 url(r'app/restaurants/detail/(?P<pk>\d+)/$', coreviews.LocationRestaurantDetailView.as_view(), name='locationres_list'),
 url(r'app/restaurants/search/$', coreviews.SearchRestaurantListView.as_view()),
 url(r'app/restaurants/search/(?P<slug>[a-zA-Z0-9-_]+)/$', coreviews.SearchRestaurantVariable.as_view()),
 url(r'app/restaurants/create/$', permission_required('core.clients')(coreviews.LocationRestaurantCreateView.as_view())),
 url(r'app/restaurants/(?P<pk>\d+)/update/$', permission_required('core.clients')(coreviews.LocationRestaurantUpdateView.as_view()), name='locationres_update'),
 url(r'app/restaurants/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewRestaurantCreateView.as_view()), name='reviewres_create'),
 url(r'app/restaurants/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewRestaurantUpdateView.as_view()), name='reviewres_update'),
 
 # -------------------------------------------------
 # BARS
 # -------------------------------------------------
 
 url(r'app/bars/$', coreviews.LocationBarListView.as_view(), name='bar_page'),
 url(r'app/bars/detail/(?P<pk>\d+)/$', coreviews.LocationBarDetailView.as_view(), name='locationbar_list'),
 url(r'app/bars/search/$', coreviews.SearchBarListView.as_view()),
 url(r'app/bars/search/(?P<slug>[a-zA-Z0-9-_]+)/$', coreviews.SearchBarVariable.as_view()),
 url(r'app/bars/create/$', permission_required('core.clients')(coreviews.LocationBarCreateView.as_view())),
 url(r'app/bars/(?P<pk>\d+)/update/$', permission_required('core.clients')(coreviews.LocationBarUpdateView.as_view()), name='locationbar_update'),
 url(r'app/bars/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewBarCreateView.as_view()), name='reviewbar_create'),
 url(r'app/bars/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewBarUpdateView.as_view()), name='reviewbar_update'),
 
 
 # -------------------------------------------------
 # CLUBS
 # -------------------------------------------------
 
 url(r'app/clubs/$', coreviews.LocationClubListView.as_view(), name='clu_page'),
 url(r'app/clubs/detail/(?P<pk>\d+)/$', coreviews.LocationClubDetailView.as_view(), name='locationclub_list'),
 url(r'app/clubs/search/$', coreviews.SearchClubListView.as_view()),
 url(r'app/clubs/search/(?P<slug>[a-zA-Z0-9-_]+)/$', coreviews.SearchClubVariable.as_view()),
 url(r'app/clubs/create/$', permission_required('core.clients')(coreviews.LocationClubCreateView.as_view())),
 url(r'app/clubs/(?P<pk>\d+)/update/$', permission_required('core.clients')(coreviews.LocationClubUpdateView.as_view()), name='locationclub_update'),
 url(r'app/clubs/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewClubCreateView.as_view()), name='reviewclub_create'),
 url(r'app/clubs/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewClubUpdateView.as_view()), name='reviewclub_update'),
 
 # -------------------------------------------------
 # LOGIN / LOGOUTs
 # -------------------------------------------------
 url(r'login/$', coreviews.login),
 url(r'signup/$', coreviews.register),
 url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/app/'}),
 
)