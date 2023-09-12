from django.contrib import admin
from .models import District,Person,Branch,Materials,user


# Register your models here.
admin.site.register(Person)
admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Materials)
admin.site.register(user)




