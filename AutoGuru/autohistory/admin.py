from django.contrib import admin
from .models import Vin, Specs, Inspection, History

# Register your models here.
admin.site.register(Vin)
admin.site.register(Specs)
admin.site.register(Inspection)
admin.site.register(History)
