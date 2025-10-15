from django.contrib import admin

from .models import Article, ArticleScope, Tag

from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class ArticleScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main'):
                    main_count += 1
        if main_count == 0:
            raise ValidationError('Необходимо выбрать один основной раздел.')
        if main_count > 1:
            raise ValidationError('Только один раздел может быть основным.')
        return super().clean()


class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    formset = ArticleScopeInlineFormSet
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    # inlines = [ArticleScopeInline]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'published_at', 'image')
    inlines = [ArticleScopeInline]
