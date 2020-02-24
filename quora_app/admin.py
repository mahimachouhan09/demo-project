from django.contrib import admin

# Register your models here.
from .models import Activity, Answer,Follow,Profile,Question,Topic
#admin.site.register(DownVote)
#admin.site.register(UpVote)
admin.site.register(Activity)
admin.site.register(Topic)
admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Follow)

