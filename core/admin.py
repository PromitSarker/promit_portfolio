from django.contrib import admin
from .models import Project, BlogPost, ContactMessage, Experience, Education, Publication, PortfolioProfile, PhilosophyTrait, SkillCategory, Skill, SkillPillar

@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "hero_subtitle", "projects_title")
    list_editable = ("email", "hero_subtitle", "projects_title")
    
    def has_add_permission(self, request):
        # Limit to only one profile
        return not PortfolioProfile.objects.exists()

@admin.register(SkillPillar)
class SkillPillarAdmin(admin.ModelAdmin):
    list_display = ("name", "subtitle", "order")
    list_editable = ("subtitle", "order")

@admin.register(PhilosophyTrait)
class PhilosophyTraitAdmin(admin.ModelAdmin):
    list_display = ("title", "icon_class", "order")
    list_editable = ("icon_class", "order")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "imageUrl", "url")
    list_editable = ("image", "imageUrl", "url")
    search_fields = ("title", "tags")

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date", "order")
    list_editable = ("category", "order")
    search_fields = ("title", "category")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "period", "order")
    list_editable = ("company", "period", "order")
    search_fields = ("title", "company")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "period", "order")
    list_editable = ("institution", "period", "order")
    search_fields = ("degree", "institution")

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "venue", "volume", "order")
    list_editable = ("venue", "volume", "order")
    search_fields = ("title", "venue", "authors")

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "pillar", "order")
    list_editable = ("pillar", "order")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "order")
    list_editable = ("category", "order")
    list_filter = ("category",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "subject")
    readonly_fields = ("name", "email", "subject", "message", "created_at")
