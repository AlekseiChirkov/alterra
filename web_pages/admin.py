from django.contrib import admin

from web_pages.models import Recommendation


class RecommendationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Recommendation._meta.fields]

    class Meta:
        model = Recommendation


admin.site.register(Recommendation, RecommendationAdmin)
