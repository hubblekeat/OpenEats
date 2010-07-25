from django.contrib import admin
from models import Recipe
from ingredient.models import Ingredient
from reversion.admin import VersionAdmin

class RecipeInline(admin.TabularInline):
    model = Ingredient

class RecipeAdmin(VersionAdmin):
    prepopulated_fields = { 'slug' : ['title']}
    inlines = [RecipeInline,]
    list_display = ['title','admin_thumbnail_view']
    search_fields = ['author__username', 'title']
    class Media:
        js = ['/site_media/admin/tinymce/jscripts/tiny_mce/tiny_mce.js', '/site_media/js/tinymce_setup.js',]

admin.site.register(Recipe, RecipeAdmin)
