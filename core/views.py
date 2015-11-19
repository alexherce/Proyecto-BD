from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

# from sitegate.decorators import redirect_signedin, sitegate_view
from sitegate.signup_flows.classic import ClassicWithEmailSignup
from sitegate.decorators import signup_view
from sitegate.signin_flows.classic import ClassicSignin
from sitegate.decorators import signin_view

import core.models as coremodels

class LandingView(TemplateView):
    template_name = 'base/index.html'


class LandingSelectView(TemplateView):
    template_name = 'base/select.html'
# -------------------------------------------------
# RESTAURANTS
# -------------------------------------------------


class LocationRestaurantListView(ListView):
	model = coremodels.LocationRestaurant
	queryset = coremodels.LocationRestaurant.objects.order_by('-created_at')
	template_name = 'location/list.html'
	paginate_by = 5

class SearchRestaurantListView(LocationRestaurantListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationRestaurant.objects.filter(title__icontains=incoming_query_string)
    	
class SearchRestaurantPrice(LocationRestaurantListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationRestaurant.objects.filter(price=incoming_query_string)
    	
class SearchRestaurantType(LocationRestaurantListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationRestaurant.objects.filter(food=incoming_query_string)
    	
class SearchRestaurantCreditCard(LocationRestaurantListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationRestaurant.objects.filter(credit_card=incoming_query_string)
    	
class SearchRestaurantOutside(LocationRestaurantListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationRestaurant.objects.filter(outdoor=incoming_query_string)
    	
class SearchRestaurantWifi(LocationRestaurantListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationRestaurant.objects.filter(wifi=incoming_query_string)

class LocationRestaurantDetailView(DetailView):
	model = coremodels.LocationRestaurant
	template_name = 'location/detail.html'
	context_object_name ='location'

	def get_context_data(self, **kwargs):
		context = super(LocationRestaurantDetailView, self).get_context_data(**kwargs)
		location = coremodels.LocationRestaurant.objects.get(id=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews = coremodels.ReviewRestaurant.objects.filter(location=location)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews
			else:
				context['user_review'] = None
		return context

class LocationRestaurantCreateView(CreateView):
	model = coremodels.LocationRestaurant
	template_name = 'base/form.html'
	fields = "__all__"

class LocationRestaurantUpdateView(UpdateView):
    model = coremodels.LocationRestaurant
    template_name = 'base/form.html'
    fields = "__all__"

class ReviewRestaurantCreateView(CreateView):
    model = coremodels.ReviewRestaurant
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = coremodels.LocationRestaurant.objects.get(id=self.kwargs['pk'])
        return super(ReviewRestaurantCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.location.get_absolute_url()

class ReviewRestaurantUpdateView(UpdateView):
    model = coremodels.ReviewRestaurant
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def get_object(self):
        return coremodels.ReviewRestaurant.objects.get(location__id=self.kwargs['pk'], user=self.request.user)

    def get_success_url(self):
        return self.object.location.get_absolute_url()
       
# -------------------------------------------------
# BARS
# -------------------------------------------------

class LocationBarListView(ListView):
	model = coremodels.LocationBar
	queryset = coremodels.LocationBar.objects.order_by('-created_at')
	template_name = 'bar/list.html'
	paginate_by = 5

class SearchBarListView(LocationBarListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationBar.objects.filter(title__icontains=incoming_query_string)
    	
class SearchBarPrice(LocationBarListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationBar.objects.filter(price=incoming_query_string)
    	
class SearchBarFood(LocationBarListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationBar.objects.filter(food=incoming_query_string)
    	
class SearchBarType(LocationBarListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationBar.objects.filter(bar=incoming_query_string)
    	
class SearchBarCreditCard(LocationBarListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationBar.objects.filter(credit_card=incoming_query_string)
    	
class SearchBarOutside(LocationBarListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationBar.objects.filter(outdoor=incoming_query_string)
    	
class SearchBarWifi(LocationBarListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationBar.objects.filter(wifi=incoming_query_string)

class LocationBarDetailView(DetailView):
	model = coremodels.LocationBar
	template_name = 'bar/detail.html'
	context_object_name ='location'

	def get_context_data(self, **kwargs):
		context = super(LocationBarDetailView, self).get_context_data(**kwargs)
		location = coremodels.LocationBar.objects.get(id=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews = coremodels.ReviewBar.objects.filter(location=location)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews
			else:
				context['user_review'] = None
		return context

class LocationBarCreateView(CreateView):
	model = coremodels.LocationBar
	template_name = 'base/form.html'
	fields = "__all__"

class LocationBarUpdateView(UpdateView):
    model = coremodels.LocationBar
    template_name = 'base/form.html'
    fields = "__all__"

class ReviewBarCreateView(CreateView):
    model = coremodels.ReviewBar
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = coremodels.LocationBar.objects.get(id=self.kwargs['pk'])
        return super(ReviewBarCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.location.get_absolute_url()

class ReviewBarUpdateView(UpdateView):
    model = coremodels.ReviewBar
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def get_object(self):
        return coremodels.ReviewBar.objects.get(location__id=self.kwargs['pk'], user=self.request.user)

    def get_success_url(self):
        return self.object.location.get_absolute_url()

# -------------------------------------------------
# NIGH CLUBS
# -------------------------------------------------

class LocationClubListView(ListView):
	model = coremodels.LocationClub
	queryset = coremodels.LocationClub.objects.order_by('-created_at')
	template_name = 'club/list.html'
	paginate_by = 5

class SearchClubListView(LocationClubListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationClub.objects.filter(title__icontains=incoming_query_string)
    	
class SearchClubPrice(LocationClubListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationClub.objects.filter(price=incoming_query_string)
    	
class SearchClubFee(LocationClubListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationClub.objects.filter(entrance_fee=incoming_query_string)
    	
class SearchClubType(LocationClubListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationClub.objects.filter(club=incoming_query_string)
    	
class SearchClubCreditCard(LocationClubListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationClub.objects.filter(credit_card=incoming_query_string)
    	
class SearchClubOutside(LocationClubListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationClub.objects.filter(outdoor=incoming_query_string)
    	
class SearchClubFreeBar(LocationClubListView):
    def get_queryset(self):
    	incoming_query_string = self.request.GET.get('query', '')
    	return coremodels.LocationClub.objects.filter(free_bar=incoming_query_string)

class LocationClubDetailView(DetailView):
	model = coremodels.LocationClub
	template_name = 'club/detail.html'
	context_object_name ='location'

	def get_context_data(self, **kwargs):
		context = super(LocationClubDetailView, self).get_context_data(**kwargs)
		location = coremodels.LocationClub.objects.get(id=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews = coremodels.ReviewClub.objects.filter(location=location)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews
			else:
				context['user_review'] = None
		return context

class LocationClubCreateView(CreateView):
	model = coremodels.LocationClub
	template_name = 'base/form.html'
	fields = "__all__"

class LocationClubUpdateView(UpdateView):
    model = coremodels.LocationClub
    template_name = 'base/form.html'
    fields = "__all__"

class ReviewClubCreateView(CreateView):
    model = coremodels.ReviewClub
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.location = coremodels.LocationClub.objects.get(id=self.kwargs['pk'])
        return super(ReviewClubCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.location.get_absolute_url()

class ReviewClubUpdateView(UpdateView):
    model = coremodels.ReviewClub
    template_name = 'base/form.html'
    fields =['description', 'rating']

    def get_object(self):
        return coremodels.ReviewClub.objects.get(location__id=self.kwargs['pk'], user=self.request.user)

    def get_success_url(self):
        return self.object.location.get_absolute_url()

# -------------------------------------------------
# LOGIN / LOGOUTs
# -------------------------------------------------

@signup_view(flow=ClassicWithEmailSignup, widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3')
def register(request):
    return render(request, 'base/register.html', {'title': 'Sign up'})

@signin_view(flow=ClassicSignin, widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3')
def login(request):
    return render(request, 'base/login.html', {'title': 'Log in'})

# @sitegate_view(flow=ClassicSignup, widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
# def entrance(request):
#    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})
