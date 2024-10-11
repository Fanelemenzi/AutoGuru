from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Vin, Specs, Inspection, History

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def index(request):
	return render(request, 'index.html', {})



def search(request):
	vin = request.GET.get('vin_number')
	vehicle = None
	specs = None
	inspections = []
	history_records = []

	if vin:
		vehicle = get_object_or_404(Vin, vin_number=vin)
		specs = vehicle.specs
		inspections = vehicle.inspections.all()
		history_records = vehicle.history.all()

	return render(request, 'search.html', {
		'vehicle':vehicle,
		'specs':specs,
		'inspections':inspections,
		'history_records':history_records
	})

