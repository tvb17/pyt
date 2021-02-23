from django.contrib import admin

from auth_app.models import CustomUser

# Register your models here.


def make_black_listed(model_admin, request, queryset):
    queryset.update(our_note="Don't deliver pizza to this user.")
make_black_listed.short_description = 'Makes a black-listed note for a user'


class CustomAdminModel(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'favourite_pizza',
        'our_note',
    )
    list_editable = ('favourite_pizza', )
    list_filter = ('favourite_pizza__name', )
    # list_select_related = ('favourite_pizza', )
    search_fields = (
        'first_name',
        'last_name',
        'favourite_pizza__name',
        'our_note',
    )
    actions = (make_black_listed, )

admin.site.register(CustomUser, CustomAdminModel)
