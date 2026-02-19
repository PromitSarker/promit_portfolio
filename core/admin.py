from django.contrib import admin
from .models import Project, BlogPost, ContactMessage, Experience, Education, Publication, PortfolioProfile, PhilosophyTrait, SkillCategory, Skill

@admin.register(PortfolioProfile)
class PortfolioProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Limit to only one profile
        return not PortfolioProfile.objects.exists()

@admin.register(PhilosophyTrait)
class PhilosophyTraitAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "imageUrl")
    search_fields = ("title", "tags")

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "date", "order")
    list_editable = ("category", "order")
    search_fields = ("title", "category")

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "company", "period", "order")
    list_editable = ("order",)
    search_fields = ("title", "company")

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("id", "degree", "institution", "period", "order")
    list_editable = ("order",)
    search_fields = ("degree", "institution")

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "venue", "order")
    list_editable = ("order",)
    search_fields = ("title", "venue", "authors")

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "order")
    list_editable = ("order",)
    list_filter = ("category",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "subject", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "subject")
