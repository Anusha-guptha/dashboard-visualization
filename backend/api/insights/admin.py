from django.contrib import admin
from .models import Insight

class InsightAdmin(admin.ModelAdmin):
    # Dynamically fetch all field names except for private attributes
    def get_list_display(self, request):
        return [field.name for field in Insight._meta.get_fields() if not field.name.startswith('_')]

admin.site.register(Insight, InsightAdmin)
