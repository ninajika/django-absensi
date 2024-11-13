from django.contrib import admin

from feedback.models import Feedback
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = ["isi_feedback", "tanggal"]
    list_filter = ["tanggal"]
    search_fields = ["isi_feedback", "tanggal"]


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
    
# Register your models here.
# admin.site.register(Feedback, FeedbackAdmin)
