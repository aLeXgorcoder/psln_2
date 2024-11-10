from django.contrib import admin
from transliterate import slugify
from psln.models import Concerts, MusicMenu, MusicMenuDetails, Songs


@admin.register(Concerts)
class ConcertsAdmin(admin.ModelAdmin):
    list_display = ['date', 'program', 'club', 'slug']
    prepopulated_fields = {'slug': ('program',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)

@admin.register(MusicMenu)
class MusicMenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not change:  # Создание нового объекта
            original_slug = slugify(obj.title)
            slug = original_slug
            counter = 1
            # Проверяем уникальность на уровне MusicMenuDetails, а не MusicMenu
            while MusicMenu.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            obj.slug = slug
        else:  # При изменении существующего объекта
            original_slug = slugify(obj.title)
            if obj.slug != original_slug:
                obj.slug = original_slug
                counter = 1
                # Проверяем уникальность на уровне MusicMenuDetails, а не MusicMenu
                while MusicMenuDetails.objects.filter(slug=obj.slug).exclude(pk=obj.pk).exists():
                    obj.slug = f"{original_slug}-{counter}"
                    counter += 1
        super().save_model(request, obj, form, change)

@admin.register(MusicMenuDetails)
class MusicMenuDetailsAdmin(admin.ModelAdmin):
    list_display = ['menu', 'slug', 'image', 'title', 'subtitle', 'date']
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not change:  # Создание нового объекта
            original_slug = slugify(obj.title)
            slug = original_slug
            counter = 1
            # Проверяем уникальность на уровне MusicMenuDetails, а не MusicMenu
            while MusicMenuDetails.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            obj.slug = slug
        else:  # При изменении существующего объекта
            original_slug = slugify(obj.title)
            if obj.slug != original_slug:
                obj.slug = original_slug
                counter = 1
                # Проверяем уникальность на уровне MusicMenuDetails, а не MusicMenu
                while MusicMenuDetails.objects.filter(slug=obj.slug).exclude(pk=obj.pk).exists():
                    obj.slug = f"{original_slug}-{counter}"
                    counter += 1
        super().save_model(request, obj, form, change)



@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ['menu_details', 'title', 'duration', 'slug']
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        if not change:  # Создание нового объекта
            original_slug = slugify(obj.title)
            slug = original_slug
            counter = 1
            # Проверяем уникальность на уровне MusicMenuDetails, а не MusicMenu
            while MusicMenuDetails.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1
            obj.slug = slug
        else:  # При изменении существующего объекта
            original_slug = slugify(obj.title)
            if obj.slug != original_slug:
                obj.slug = original_slug
                counter = 1
                # Проверяем уникальность на уровне MusicMenuDetails, а не MusicMenu
                while MusicMenuDetails.objects.filter(slug=obj.slug).exclude(pk=obj.pk).exists():
                    obj.slug = f"{original_slug}-{counter}"
                    counter += 1
        super().save_model(request, obj, form, change)