from django.contrib import admin
from .models import Candidate, Language, SoftSkills, SocialNetworks, Experience, Studies

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1

class SoftSkillsInline(admin.TabularInline):
    model = SoftSkills
    extra = 1

class SocialNetworksInline(admin.TabularInline):
    model = SocialNetworks
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class StudiesInline(admin.TabularInline):
    model = Studies
    extra = 1

class CandidateAdmin(admin.ModelAdmin):
    inlines = [LanguageInline, SoftSkillsInline, SocialNetworksInline, ExperienceInline, StudiesInline]
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Language)
admin.site.register(SoftSkills)
admin.site.register(SocialNetworks)
admin.site.register(Experience)
admin.site.register(Studies)
