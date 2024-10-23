from django.contrib import admin

from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["isi_feedback", "tanggal"]
    list_filter = ["tanggal"]
    search_fields = ["isi_feedback", "tanggal"]
    
# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)
