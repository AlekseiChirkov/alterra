from django.contrib import admin

from web_pages.models import Recommendation, Request


class RecommendationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recommendation._meta.fields]

    class Meta:
        model = Recommendation


class RequestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Request._meta.fields]

    class Meta:
        model = Request


admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(Request, RequestAdmin)
