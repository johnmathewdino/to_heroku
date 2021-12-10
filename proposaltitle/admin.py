from django.contrib import admin
from .models import ProposeTitle, TitleComment, CommentReply
# Register your models here.
admin.site.register(ProposeTitle)
admin.site.register(TitleComment)
admin.site.register(CommentReply)
