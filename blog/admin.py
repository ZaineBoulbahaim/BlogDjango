from django.contrib import admin
from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}  # Genera automàticament el slug
    # readonly_fields = ("slug",) # Només mostrar, no permetre escriure
    
# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)