from django.contrib import admin
from .models import Record, RecordComment, RecordTask


admin.site.register(Record)
admin.site.register(RecordComment)
admin.site.register(RecordTask)
