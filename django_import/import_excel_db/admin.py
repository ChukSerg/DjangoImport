from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Boards, Cities, Surfaces, Materials
from .resources import BoardsResource


class BoardsAdmin(ImportExportModelAdmin):
    resource_class = BoardsResource
    list_filter = ('city', 'surface')
    search_fields = ('address',)


class CitiesAdmin(admin.ModelAdmin):
    class Meta:
        model = Cities


class SurfacesAdmin(admin.ModelAdmin):
    class Meta:
        model = Surfaces


class MaterialsAdmin(admin.ModelAdmin):
    class Meta:
        model = Materials


admin.site.register(Boards, BoardsAdmin)
admin.site.register(Cities, CitiesAdmin)
admin.site.register(Surfaces, SurfacesAdmin)
admin.site.register(Materials, MaterialsAdmin)
