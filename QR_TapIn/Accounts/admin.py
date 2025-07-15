from django.contrib import admin
from Accounts.models import User, Department, Student
from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.urls import path
from django.shortcuts import redirect

# Register your models here.


class CustomUserConfig(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                    "email",
                    # "birthday",
                    "sex",
                    "department",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    # "groups",
                    # "user_permissions",
                )
            },
        ),
    )

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        # "birthday",
        "is_staff",
    )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "<id>/reset-password",
                self.admin_site.admin_view(self.reset_user_password),
                name="reset_user_password",
            ),
            path(
                "<id>/set-group",
                self.admin_site.admin_view(self.set_group),
                name="set_group",
            ),
        ]
        return custom_urls + urls

    def reset_user_password(self, req, id):
        user = User.objects.get(id=id)
        user.save()
        messages.success(req, f"Password changed successfully: {user.username}")
        return redirect(f"../../{id}")

    def set_group(self, req, id):
        user = User.objects.get(id=id)
        user.save()
        messages.success(req, f"Password changed successfully: {user.username}")
        return redirect(f"../../{id}")


admin.site.register(Department)
admin.site.register(Student)
admin.site.register(User, CustomUserConfig)

