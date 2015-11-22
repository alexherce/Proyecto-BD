from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User

# from sitegate.decorators import redirect_signedin, sitegate_view
from sitegate.signup_flows.classic import ClassicWithEmailSignup
from sitegate.decorators import signup_view
from sitegate.signin_flows.classic import ClassicSignin
from sitegate.decorators import signin_view
from django.contrib.admin.views.decorators import staff_member_required
from graphos.sources.model import ModelDataSource
from graphos.renderers import gchart

import urllib, urllib2
import djqscsv

from django.shortcuts import get_object_or_404
import core.models as coremodels

# -------------------------------------------------
# LANDING PAGE
# -------------------------------------------------

class LandingView(TemplateView):
    template_name = 'base/index.html'

# -------------------------------------------------
# APP SELECTOR
# -------------------------------------------------

class LandingSelectView(TemplateView):
    template_name = 'base/select.html'
    
# -------------------------------------------------
# RESTAURANTS
# -------------------------------------------------

#Restaurant List View.
class LocationRestaurantListView(ListView):
	model = coremodels.LocationRestaurant
	queryset = coremodels.LocationRestaurant.objects.filter(verified='True').order_by('-created_at')
	template_name = 'restaurant/list.html'
	paginate_by = 5

#Restaurant Search View. Only search by title.
class SearchRestaurantListView(LocationRestaurantListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationRestaurant.objects.filter(verified='True', title__icontains=incoming_query_string)

#Restaurant Variable Search View. Search by any model field.    	
class SearchRestaurantVariable(LocationRestaurantListView):
    def get_queryset(self):
        incoming_query_string = self.request.GET.get('query', '')
        variable_column = self.kwargs['slug']
        filter = variable_column
        return coremodels.LocationRestaurant.objects.filter(verified='True', **{ filter: incoming_query_string })

#Restaurant Detailed View.    	
class LocationRestaurantDetailView(DetailView):
	template_name = 'restaurant/detail.html'
	context_object_name ='location'
	
	def get_object(self):
		model = get_object_or_404(coremodels.LocationRestaurant, pk=self.kwargs['pk'])
		return model

	def get_context_data(self, **kwargs):
		context = super(LocationRestaurantDetailView, self).get_context_data(**kwargs)
		location = coremodels.LocationRestaurant.objects.get(pk=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews = coremodels.ReviewRestaurant.objects.filter(location=location)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews
			else:
				context['user_review'] = None
		return context

#Restaurant Create View.		
class LocationRestaurantCreateView(CreateView):
    model = coremodels.LocationRestaurant
    template_name = 'base/form.html'
    fields = ['title', 'description', 'address', 'position', 'hours', 'image_file', 'food', 'wifi', 'outlets', 'bathrooms', 'coffee', 'alcohol', 'outdoor', 'price', 'credit_card']
    
    def form_valid(self, form):
        form.instance.company_id = self.request.user.client.company
        return super(LocationRestaurantCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

#Restaurant Update View.
class LocationRestaurantUpdateView(UpdateView):
    template_name = 'base/form.html'
    fields = ['title', 'description', 'address', 'position', 'hours', 'image_file', 'food', 'wifi', 'outlets', 'bathrooms', 'coffee', 'alcohol', 'outdoor', 'price', 'credit_card']
    
    def get_object(self):
		model = get_object_or_404(coremodels.LocationRestaurant, pk=self.kwargs['pk'])
		return model
		
#Restaurant Create Review View.
class ReviewRestaurantCreateView(CreateView):
    model = coremodels.ReviewRestaurant
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = coremodels.LocationRestaurant.objects.get(pk=self.kwargs['pk'])
        form.instance.company_id = coremodels.LocationRestaurant.objects.get(pk=self.kwargs['pk']).company_id
        form.instance.location_name = coremodels.LocationRestaurant.objects.get(pk=self.kwargs['pk']).title
        return super(ReviewRestaurantCreateView, self).form_valid(form)

    def get_success_url(self):
        obj = coremodels.LocationRestaurant.objects.get(pk=self.kwargs['pk'])
        coremodels.LocationRestaurant.objects.filter(pk=self.kwargs['pk']).update(average=coremodels.LocationRestaurant.objects.get(pk=self.kwargs['pk']).get_average_rating())
        obj.refresh_from_db()
        return self.object.location.get_absolute_url()
       
# -------------------------------------------------
# BARS
# -------------------------------------------------

#Bar List View.
class LocationBarListView(ListView):
	model = coremodels.LocationBar
	queryset = coremodels.LocationBar.objects.filter(verified='True').order_by('-created_at')
	template_name = 'bar/list.html'
	paginate_by = 5

#Bar Search View. Only search by title.
class SearchBarListView(LocationBarListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationBar.objects.filter(verified='True', title__icontains=incoming_query_string)

#Bar Variable Search View. Search by any model field.    	
class SearchBarVariable(LocationBarListView):
    def get_queryset(self):
        incoming_query_string = self.request.GET.get('query', '')
        variable_column = self.kwargs['slug']
        filter = variable_column
        return coremodels.LocationBar.objects.filter(verified='True', **{ filter: incoming_query_string })

#Bar Detailed View.
class LocationBarDetailView(DetailView):
	template_name = 'bar/detail.html'
	context_object_name ='location'
	
	def get_object(self):
		model = get_object_or_404(coremodels.LocationBar, pk=self.kwargs['pk'])
		return model

	def get_context_data(self, **kwargs):
		context = super(LocationBarDetailView, self).get_context_data(**kwargs)
		location = coremodels.LocationBar.objects.get(pk=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews = coremodels.ReviewBar.objects.filter(location=location)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews
			else:
				context['user_review'] = None
		return context

#Bar Create View.
class LocationBarCreateView(CreateView):
    model = coremodels.LocationBar
    template_name = 'base/form.html'
    fields = ['title', 'description', 'address', 'position', 'hours', 'image_file', 'bar', 'food', 'wifi', 'bathrooms', 'outdoor', 'price', 'credit_card']
    
    def form_valid(self, form):
        form.instance.company_id = self.request.user.client.company
        return super(LocationBarCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

#Bar Update View.
class LocationBarUpdateView(UpdateView):
    template_name = 'base/form.html'
    fields = ['title', 'description', 'address', 'position', 'hours', 'image_file', 'bar', 'food', 'wifi', 'bathrooms', 'outdoor', 'price', 'credit_card']
    
    def get_object(self):
		model = get_object_or_404(coremodels.LocationBar, pk=self.kwargs['pk'])
		return model

#Bar Create Review View.
class ReviewBarCreateView(CreateView):
    model = coremodels.ReviewBar
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = coremodels.LocationBar.objects.get(pk=self.kwargs['pk'])
        form.instance.company_id = coremodels.LocationBar.objects.get(pk=self.kwargs['pk']).company_id
        form.instance.location_name = coremodels.LocationBar.objects.get(pk=self.kwargs['pk']).title
        return super(ReviewBarCreateView, self).form_valid(form)

    def get_success_url(self):
        obj = coremodels.LocationBar.objects.get(pk=self.kwargs['pk'])
        coremodels.LocationBar.objects.filter(pk=self.kwargs['pk']).update(average=coremodels.LocationBar.objects.get(pk=self.kwargs['pk']).get_average_rating())
        obj.refresh_from_db()
        return self.object.location.get_absolute_url()

# -------------------------------------------------
# NIGH CLUBS
# -------------------------------------------------

#Night Club List View.
class LocationClubListView(ListView):
	model = coremodels.LocationClub
	queryset = coremodels.LocationClub.objects.filter(verified='True').order_by('-created_at')
	template_name = 'club/list.html'
	paginate_by = 5

#Night Club Search View. Only search by title.
class SearchClubListView(LocationClubListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationClub.objects.filter(verified='True', title__icontains=incoming_query_string)
 
#Night Club Variable Search View. Search by any model field.    	
class SearchClubVariable(LocationClubListView):
    def get_queryset(self):
        incoming_query_string = self.request.GET.get('query', '')
        variable_column = self.kwargs['slug']
        filter = variable_column
        return coremodels.LocationClub.objects.filter(verified='True', **{ filter: incoming_query_string })
  
#Night Club Detailed View.
class LocationClubDetailView(DetailView):
	template_name = 'club/detail.html'
	context_object_name ='location'
	
	def get_object(self):
		model = get_object_or_404(coremodels.LocationClub, pk=self.kwargs['pk'])
		return model

	def get_context_data(self, **kwargs):
		context = super(LocationClubDetailView, self).get_context_data(**kwargs)
		location = coremodels.LocationClub.objects.get(pk=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews = coremodels.ReviewClub.objects.filter(location=location)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews
			else:
				context['user_review'] = None
		return context

#Night Club Create View.
class LocationClubCreateView(CreateView):
    model = coremodels.LocationClub
    template_name = 'base/form.html'
    fields = ['title', 'description', 'address', 'position', 'hours', 'image_file', 'club', 'music', 'bathrooms', 'outdoor', 'free_bar', 'price', 'entrance_fee', 'credit_card']
    
    def form_valid(self, form):
	    form.instance.company_id = self.request.user.client.company
	    form.instance.user = self.request.user
	    return super(LocationClubCreateView, self).form_valid(form)
    
    def get_success_url(self):
	    return self.object.get_absolute_url()

#Night Club Update View.
class LocationClubUpdateView(UpdateView):
    template_name = 'base/form.html'
    fields = ['title', 'description', 'address', 'position', 'hours', 'image_file', 'club', 'music', 'bathrooms', 'outdoor', 'free_bar', 'price', 'entrance_fee', 'credit_card']
    
    def get_object(self):
		model = get_object_or_404(coremodels.LocationClub, pk=self.kwargs['pk'])
		return model

#Night Club Create Review View.
class ReviewClubCreateView(CreateView):
    model = coremodels.ReviewClub
    template_name = 'base/form.html'
    fields = ['description', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = coremodels.LocationClub.objects.get(pk=self.kwargs['pk'])
        form.instance.company_id = coremodels.LocationClub.objects.get(pk=self.kwargs['pk']).company_id
        form.instance.location_name = coremodels.LocationClub.objects.get(pk=self.kwargs['pk']).title
        return super(ReviewClubCreateView, self).form_valid(form)

    def get_success_url(self):
        obj = coremodels.LocationClub.objects.get(pk=self.kwargs['pk'])
        coremodels.LocationClub.objects.filter(pk=self.kwargs['pk']).update(average=coremodels.LocationClub.objects.get(pk=self.kwargs['pk']).get_average_rating())
        obj.refresh_from_db()
        return self.object.location.get_absolute_url()
        
# -------------------------------------------------
# ADMIN DASHBOARD
# -------------------------------------------------

class DashboardView(TemplateView):
    template_name = 'dashboard/index.html'

# -------------------------------------------------
# LOGIN / LOGOUT VIEWS
# -------------------------------------------------

#Sign up form.
@signup_view(flow=ClassicWithEmailSignup, widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3')
def register(request):
    return render(request, 'base/register.html', {'title': 'Sign up'})

#Log in form.
@signin_view(flow=ClassicSignin, widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3')
def login(request):
    return render(request, 'base/login.html', {'title': 'Log in'})

# -------------------------------------------------
# CLIENT EXPORT TO DOCUMENTS
# Exports clients locations based on Company ID
# associated with their profiles. Members from a
# company cannot access other companies locations.
# Normal users cannot download any files.
# -------------------------------------------------

def get_restaurants_csv(request):
    restaurants_qs = coremodels.LocationRestaurant.objects.filter(company_id = request.user.client.company)
    return djqscsv.render_to_csv_response(restaurants_qs, append_datestamp=True)
    
def get_bars_csv(request):
    qs = coremodels.LocationBar.objects.filter(company_id = request.user.client.company)
    return djqscsv.render_to_csv_response(qs, append_datestamp=True)
    
def get_clubs_csv(request):
    qs = coremodels.LocationClub.objects.filter(company_id = request.user.client.company)
    return djqscsv.render_to_csv_response(qs, append_datestamp=True)

def get_restaurants_reviews_csv(request):
    restaurants_qs = coremodels.ReviewRestaurant.objects.filter(company_id = request.user.client.company)
    return djqscsv.render_to_csv_response(restaurants_qs, append_datestamp=True)
    
def get_bars_reviews_csv(request):
    qs = coremodels.ReviewBar.objects.filter(company_id = request.user.client.company)
    return djqscsv.render_to_csv_response(qs, append_datestamp=True)
    
def get_clubs_reviews_csv(request):
    qs = coremodels.ReviewClub.objects.filter(company_id = request.user.client.company)
    return djqscsv.render_to_csv_response(qs, append_datestamp=True)
    
# -------------------------------------------------
# ADMIN EXPORT TO DOCUMENTS
# Exports all locations. Only accessible to staff
# members and admins.
# -------------------------------------------------

def get_restaurants_admin_csv(request):
    restaurants_qs = coremodels.LocationRestaurant.objects.all()
    return djqscsv.render_to_csv_response(restaurants_qs, append_datestamp=True)
    
def get_bars_admin_csv(request):
    qs = coremodels.LocationBar.objects.all()
    return djqscsv.render_to_csv_response(qs, append_datestamp=True)
    
def get_clubs_admin_csv(request):
    qs = coremodels.LocationClub.objects.all()
    return djqscsv.render_to_csv_response(qs, append_datestamp=True)

def get_restaurants_reviews_admin_csv(request):
    restaurants_qs = coremodels.ReviewRestaurant.objects.all()
    return djqscsv.render_to_csv_response(restaurants_qs, append_datestamp=True)
    
def get_bars_reviews_admin_csv(request):
    qs = coremodels.ReviewBar.objects.all()
    return djqscsv.render_to_csv_response(qs, append_datestamp=True)
    
def get_clubs_reviews_admin_csv(request):
    qs = coremodels.ReviewClub.objects.all()
    return djqscsv.render_to_csv_response(qs, append_datestamp=True)
    
    
def chart_view(request):
    queryset = coremodels.LocationRestaurant.objects.all()
    data_source = ModelDataSource(queryset,
                                      fields=['title', 'wifi'])
    chart = gchart.LineChart(data_source, html_id="chart")

    context = {
                "chart": chart,
                }
    return context

class Charts(TemplateView):
    renderer = None

    def get_context_data(self, **kwargs):
        super_context = super(Charts, self).get_context_data(**kwargs)
        queryset = coremodels.LocationRestaurant.objects.all()
        data_source = ModelDataSource(queryset,
                                      fields=['title', 'average'])
        line_chart_res = gchart.LineChart(data_source, options={'title': "Average Restaurant Ratings"})
        queryset = coremodels.LocationBar.objects.all()
        data_source = ModelDataSource(queryset,
                                      fields=['title', 'average'])
        line_chart_bar = gchart.LineChart(data_source, options={'title': "Average Bar Ratings"})
        queryset = coremodels.LocationClub.objects.all()
        data_source = ModelDataSource(queryset,
                                      fields=['title', 'average'])
        line_chart_club = gchart.LineChart(data_source, options={'title': "Average Night Club Ratings"}) 

        context = {
                "line_chart_res": line_chart_res,
                "line_chart_bar": line_chart_bar,
                "line_chart_club": line_chart_club,
                }
        context.update(super_context)
        return context
        
class GChartDemo(Charts):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super(GChartDemo, self).get_context_data(**kwargs)
        return context
        
gchart_demo = GChartDemo.as_view(renderer=gchart)