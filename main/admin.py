from django.contrib import admin
from .models import (
    User,
    Topic,
    Subject,
    Question,
    Answer,
)

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)