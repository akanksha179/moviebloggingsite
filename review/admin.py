from django.contrib import admin
from . import models



# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    fields = (('title', 'weekly_recommendation'),
              ('rating', 'poster'),
              ('single_line_description', 'content'),
              ('cast', 'genre'),
              'date_published', 'author')


admin.site.register(models.Review, ReviewAdmin)


class KnowledgeAdmin(admin.ModelAdmin):
    fields = ['paragraph']


admin.site.register(models.Knowledge, KnowledgeAdmin)


class GenreAdmin(admin.ModelAdmin):
    fields = ['genre']


admin.site.register(models.Genre, GenreAdmin)


class CastAdmin(admin.ModelAdmin):
    fields = (('name', 'cast_image'), 'birthdate', 'best_work', 'description', 'achievements')


admin.site.register(models.Cast, CastAdmin)
