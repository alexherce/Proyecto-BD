from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

 url(r'^$', coreviews.LandingView.as_view()),
 url(r'app/$', login_required(coreviews.LandingSelectView.as_view()), name='select_page'),
 
# -------------------------------------------------
# RESTAURANTS
# -------------------------------------------------

 url(r'app/restaurants/$', coreviews.LocationRestaurantListView.as_view(), name='res_page'),
 url(r'app/restaurants/detail/(?P<pk>\d+)/$', coreviews.LocationRestaurantDetailView.as_view(), name='locationres_list'),
 url(r'app/restaurants/search/$', coreviews.SearchRestaurantListView.as_view()),
 url(r'app/restaurants/search/price/$', coreviews.SearchRestaurantPrice.as_view()),
 url(r'app/restaurants/search/food/$', coreviews.SearchRestaurantType.as_view()),
 url(r'app/restaurants/search/creditcard/$', coreviews.SearchRestaurantCreditCard.as_view()),
 url(r'app/restaurants/search/outside/$', coreviews.SearchRestaurantOutside.as_view()),
 url(r'app/restaurants/search/wifi/$', coreviews.SearchRestaurantWifi.as_view()),
 url(r'app/restaurants/create/$', login_required(coreviews.LocationRestaurantCreateView.as_view())),
 url(r'app/restaurants/(?P<pk>\d+)/update/$', login_required(coreviews.LocationRestaurantUpdateView.as_view()), name='locationres_update'),
 url(r'app/restaurants/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewRestaurantCreateView.as_view()), name='reviewres_create'),
 url(r'app/restaurants/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewRestaurantUpdateView.as_view()), name='reviewres_update'),
 
 # -------------------------------------------------
 # BARS
 # -------------------------------------------------
 
 url(r'app/bars/$', coreviews.LocationBarListView.as_view(), name='bar_page'),
 url(r'app/bars/detail/(?P<pk>\d+)/$', coreviews.LocationBarDetailView.as_view(), name='locationbar_list'),
 url(r'app/bars/search/$', coreviews.SearchBarListView.as_view()),
 url(r'app/bars/search/price/$', coreviews.SearchBarPrice.as_view()),
 url(r'app/bars/search/food/$', coreviews.SearchBarFood.as_view()),
 url(r'app/bars/search/type/$', coreviews.SearchBarType.as_view()),
 url(r'app/bars/search/creditcard/$', coreviews.SearchBarCreditCard.as_view()),
 url(r'app/bars/search/outside/$', coreviews.SearchBarOutside.as_view()),
 url(r'app/bars/search/wifi/$', coreviews.SearchBarWifi.as_view()),
 url(r'app/bars/create/$', login_required(coreviews.LocationBarCreateView.as_view())),
 url(r'app/bars/(?P<pk>\d+)/update/$', login_required(coreviews.LocationBarUpdateView.as_view()), name='locationbar_update'),
 url(r'app/bars/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewBarCreateView.as_view()), name='reviewbar_create'),
 url(r'app/bars/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewBarUpdateView.as_view()), name='reviewbar_update'),
 
 
 # -------------------------------------------------
 # CLUBS
 # -------------------------------------------------
 
 url(r'app/clubs/$', coreviews.LocationClubListView.as_view(), name='clu_page'),
 url(r'app/clubs/detail/(?P<pk>\d+)/$', coreviews.LocationClubDetailView.as_view(), name='locationclub_list'),
 url(r'app/clubs/search/$', coreviews.SearchClubListView.as_view()),
 url(r'app/clubs/search/price/$', coreviews.SearchClubPrice.as_view()),
 url(r'app/clubs/search/fee/$', coreviews.SearchClubFee.as_view()),
 url(r'app/clubs/search/type/$', coreviews.SearchClubType.as_view()),
 url(r'app/clubs/search/creditcard/$', coreviews.SearchClubCreditCard.as_view()),
 url(r'app/clubs/search/outside/$', coreviews.SearchClubOutside.as_view()),
 url(r'app/clubs/search/freebar/$', coreviews.SearchClubFreeBar.as_view()),
 url(r'app/clubs/create/$', login_required(coreviews.LocationClubCreateView.as_view())),
 url(r'app/clubs/(?P<pk>\d+)/update/$', login_required(coreviews.LocationClubUpdateView.as_view()), name='locationclub_update'),
 url(r'app/clubs/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewClubCreateView.as_view()), name='reviewclub_create'),
 url(r'app/clubs/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewClubUpdateView.as_view()), name='reviewclub_update'),
 
 # -------------------------------------------------
 # LOGIN / LOGOUTs
 # -------------------------------------------------
 url(r'login/$', coreviews.login),
 url(r'signup/$', coreviews.register),
 url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/app/'}),
 
)