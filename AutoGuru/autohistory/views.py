from django.shortcuts import render
from django.contrib import messages
from .models import Vin, Specs, Inspection

# Create your views here.
def home(request):
	return render(request, 'home.html', {})

def vehicles(request):
    idSpecs = Specs.objects.all()
    Inspect = Inspection.objects.all()
    data = {
         'idSpecs': idSpecs,
         'Inspect': Inspect
    }
    return render(request, 'vehicles.html', data)

def search(request):
	#determine if they filled the form
	if request.method == "POST":
		searched = request.POST['searched']
		#query the Specs DB model
		searched = Specs.objects.filter(vin_number__vin_number__icontains=searched)
		#Test for null
		if not searched:
			messages.success(request, "Sorry Vehcile not found, enetr VIN again")
			return render(request, "search.html", {})
		else: 
			return render(request, 'search.html', {'searched':searched})
	else:
		return render(request, 'search.html', {})

