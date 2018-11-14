from django.contrib import admin
from .models import (
		Faculty, Degree, Module, 
		StudetlyTag, TaggedItem
	)

admin.site.register(Faculty)
admin.site.register(Degree)
admin.site.register(Module)

# class StudentlyTagAdmin(admin.ModelAdmin):
# 	list_display = ('tag_list',)

# 	def get_queryset(self, request):
# 		return super(StudentlyTagAdmin, self).get_queryset(request).prefetch_related('tags')

# 	def tag_list(self, obj):
# 		return u", ".join(t.name for t in obj.tags.all())

# admin.site.register(StudentlyTag, StudentlyTagAdmin)

admin.site.register(StudetlyTag)