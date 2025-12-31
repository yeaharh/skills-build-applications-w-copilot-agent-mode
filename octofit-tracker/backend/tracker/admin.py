from django.contrib import admin
from .models import Team, UserProfile, Activity, Workout, Leaderboard

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'hero_name', 'team', 'total_points', 'created_at']
    list_filter = ['team']
    search_fields = ['user__username', 'hero_name']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'duration_minutes', 'points_earned', 'activity_date']
    list_filter = ['activity_type', 'activity_date']
    search_fields = ['user__username']

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'activity_type', 'difficulty', 'duration_minutes']
    list_filter = ['difficulty', 'activity_type']
    search_fields = ['title']

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['user', 'period', 'points', 'rank', 'period_start', 'period_end']
    list_filter = ['period']
    search_fields = ['user__username']
