from operator import contains
from django.contrib import admin

# Register your models here.
from .models import blognew
from .models import contactform
from .models import portfolio_photos
from .models import experience
from .models import about
from .models import education


admin.site.register(blognew)
admin.site.register(contactform)
admin.site.register(portfolio_photos)
admin.site.register(experience)
admin.site.register(about)
admin.site.register(education)