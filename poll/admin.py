from django.contrib import admin
from poll.models import (
    Poll,
    PollOptions,
)


class PollOptionInline(admin.TabularInline):
    model = PollOptions


class PollAdmin(admin.ModelAdmin):
    inlines = (PollOptionInline,)


admin.site.register(Poll, PollAdmin)


class PollOptionsAdmin(admin.ModelAdmin):
    readonly_fields = ('option_count',)


admin.site.register(PollOptions, PollOptionsAdmin)
