from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([Blog,Tags])
# in the admin pannel we have access of the registered models only 
# what is admin 
# what is site.register 