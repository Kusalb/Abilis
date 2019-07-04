from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Documentation)
admin.site.register(user)
admin.site.register(Category)
admin.site.register(DocumentCategory)
admin.site.register(Form_question)
admin.site.register(Form_answer)


