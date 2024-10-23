from django.contrib import admin

from UserProfile.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "is_dosen"]
    list_filter = ["is_dosen"]
    search_fields = ["user__username", "is_dosen"]
    actions = ["make_dosen", "remove_dosen"]

    def make_dosen(self, request, queryset):
        queryset.update(is_dosen=True)
    make_dosen.short_description = "Set selected users as Dosen"

    def remove_dosen(self, request, queryset):
        queryset.update(is_dosen=False)
    remove_dosen.short_description = "Remove Dosen status from selected users"


admin.site.register(UserProfile, UserProfileAdmin)
