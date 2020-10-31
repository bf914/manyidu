from django.contrib import admin
from .models import Category,Paper,Topic,Options,Records,RecordDetails

admin.site.site_header = '满意度调查后台管理'
admin.site.site_title = '满意度调查后台管理'

admin.site.register(Category)

admin.site.register(Paper)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'paper', 'name', 'desc', 'owener', 'status', 'created_time')
    fields = ('paper', 'name', 'desc')
    search_fields = ('name', 'desc')
    list_display_links = ('name',)

    def save_model(self, request, obj, form, change):
        obj.owener = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Topic)


class OptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'name', 'desc', 'score', 'owener', 'status', 'created_time')
    fields = ('topic', 'name', 'desc', 'score')
    search_fields = ('name', 'desc')
    list_display_links = ('name',)
    save_as = True

    def save_model(self, request, obj, form, change):
        obj.owener = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Options, OptionsAdmin)


class RecordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'age', 'id_no', 'address', 'tel', 'types', 'hospital', 'dept', 'doctor', 'times', 'cost', 'pat_type', 'visit_time', 'created_time')
    fields = ('name', 'sex', 'age', 'id_no', 'address', 'tel', 'types', 'hospital', 'dept', 'doctor', 'times', 'cost', 'pat_type', 'visit_time')
    search_fields = ('name', 'id_no', 'dept', 'doctor')
    list_display_links = ('name',)
    save_as = True

    def save_model(self, request, obj, form, change):
        obj.owener = request.user
        return super().save_model(request, obj, form, change)

admin.site.register(Records, RecordsAdmin)
