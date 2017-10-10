from django.contrib import admin
from .models import Category
from .models import Tovar
from .models import ScladTov

admin.site.register(Category)
admin.site.register(Tovar)
admin.site.register(ScladTov)