from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Vin, Specs, Inspection, History

# Create your views here.
def home(request):
	return render(request, 'home.html', {})


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


def vehicles(request):
    idSpecs = Specs.objects.all()
    inspect = Inspection.objects.all()
    data = {
        'idSpecs': idSpecs,
         'Inspect': Inspect
    }
    return render(request, 'vehicles.html', {'idSpecs':idSpecs, 'inspect':inspect})

#def search(request):
#	#determine if they filled the form
#	if request.method == "POST":
#		searched = request.POST['searched']
#		#query the Specs DB model
#		searched = Specs.objects.filter(vin_number__vin_number__icontains=searched)
#		#Test for null
#		if not searched:
#			messages.success(request, "Sorry Vehcile not found, enetr VIN again")
#			return render(request, "search.html", {})
#		else: 
#			return render(request, 'search.html', {'searched':searched})
#	else:
#		return render(request, 'search.html', {})

