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
 url(r'app/restaurants/(?P<pk>[^~,]+)/detail/$', coreviews.LocationRestaurantDetailView.as_view(), name='locationres_list'),
 url(r'app/restaurants/search/$', coreviews.SearchRestaurantListView.as_view()),
 url(r'app/restaurants/search/(?P<slug>[a-zA-Z0-9-_]+)/$', coreviews.SearchRestaurantVariable.as_view()),
 url(r'app/restaurants/create/$', permission_required('core.can_publish')(coreviews.LocationRestaurantCreateView.as_view())),
 url(r'app/restaurants/(?P<pk>[^~,]+)/update/$', permission_required('core.can_publish')(coreviews.LocationRestaurantUpdateView.as_view()), name='locationres_update'),
 url(r'app/restaurants/(?P<pk>[^~,]+)/review/create/$', login_required(coreviews.ReviewRestaurantCreateView.as_view()), name='reviewres_create'),

 # -------------------------------------------------
 # BARS
 # -------------------------------------------------
 
 url(r'app/bars/$', coreviews.LocationBarListView.as_view(), name='bar_page'),
 url(r'app/bars/(?P<pk>[^~,]+)/detail/$', coreviews.LocationBarDetailView.as_view(), name='locationbar_list'),
 url(r'app/bars/search/$', coreviews.SearchBarListView.as_view()),
 url(r'app/bars/search/(?P<slug>[a-zA-Z0-9-_]+)/$', coreviews.SearchBarVariable.as_view()),
 url(r'app/bars/create/$', permission_required('core.can_publish')(coreviews.LocationBarCreateView.as_view())),
 url(r'app/bars/(?P<pk>[^~,]+)/update/$', permission_required('core.can_publish')(coreviews.LocationBarUpdateView.as_view()), name='locationbar_update'),
 url(r'app/bars/(?P<pk>[^~,]+)/review/create/$', login_required(coreviews.ReviewBarCreateView.as_view()), name='reviewbar_create'),

 
 # -------------------------------------------------
 # CLUBS
 # -------------------------------------------------
 
 url(r'app/clubs/$', coreviews.LocationClubListView.as_view(), name='clu_page'),
 url(r'app/clubs/(?P<pk>[^~,]+)/detail/$', coreviews.LocationClubDetailView.as_view(), name='locationclub_list'),
 url(r'app/clubs/search/$', coreviews.SearchClubListView.as_view()),
 url(r'app/clubs/search/(?P<slug>[a-zA-Z0-9-_]+)/$', coreviews.SearchClubVariable.as_view()),
 url(r'app/clubs/create/$', permission_required('core.can_publish')(coreviews.LocationClubCreateView.as_view())),
 url(r'app/clubs/(?P<pk>[^~,]+)/update/$', permission_required('core.can_publish')(coreviews.LocationClubUpdateView.as_view()), name='locationclub_update'),
 url(r'app/clubs/(?P<pk>[^~,]+)/review/create/$', login_required(coreviews.ReviewClubCreateView.as_view()), name='reviewclub_create'),

 # -------------------------------------------------
 # LOGIN / LOGOUTs
 # -------------------------------------------------
 url(r'login/$', coreviews.login),
 url(r'signup/$', coreviews.register),
 url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/app/'}),
 
# -------------------------------------------------
# CLIENT EXPORT TO DOCUMENTS
# Exports clients locations based on Company ID
# associated with their profiles. Members from a
# company cannot access other companies locations.
# Normal users cannot download any files.
# -------------------------------------------------
 
 url(r'app/dashboard/download_restaurants/csv/$', permission_required('core.can_publish')(coreviews.get_restaurants_csv)),
 url(r'app/dashboard/download_bars/csv/$', permission_required('core.can_publish')(coreviews.get_bars_csv)),
 url(r'app/dashboard/download_clubs/csv/$', permission_required('core.can_publish')(coreviews.get_clubs_csv)),
 
 url(r'app/dashboard/download_restaurants_reviews/csv/$', permission_required('core.can_publish')(coreviews.get_restaurants_reviews_csv)),
 url(r'app/dashboard/download_bars_reviews/csv/$', permission_required('core.can_publish')(coreviews.get_bars_reviews_csv)),
 url(r'app/dashboard/download_clubs_reviews/csv/$', permission_required('core.can_publish')(coreviews.get_clubs_reviews_csv)),
 
)