from django.contrib import admin
from .models import Pearl, Oyster, Comment

admin.site.register(Oyster)
admin.site.register(Pearl)
admin.site.register(Comment)