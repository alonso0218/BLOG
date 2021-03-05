from django.contrib import admin

# Register your models here.
from .models import Post,PostView,Comment,Like,DisLike,User


admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)