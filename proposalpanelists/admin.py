from django.contrib import admin
from .models import AdviserAndPanelist, Adviserrequest, Panel1request, Panel2request, Panel3request, Limitation

admin.site.register(AdviserAndPanelist)
admin.site.register(Adviserrequest)
admin.site.register(Panel1request)
admin.site.register(Panel2request)
admin.site.register(Panel3request)
admin.site.register(Limitation)


