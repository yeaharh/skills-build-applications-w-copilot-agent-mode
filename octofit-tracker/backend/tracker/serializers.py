from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Team, UserProfile, Activity, Workout, Leaderboard

class TeamSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'created_at', 'member_count']
    
    def get_member_count(self, obj):
        return obj.members.count()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    team_name = serializers.CharField(source='team.name', read_only=True)
    
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'team', 'team_name', 'hero_name', 'total_points', 'created_at']

class ActivitySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'user', 'username', 'activity_type', 'duration_minutes', 
                  'distance_km', 'calories_burned', 'points_earned', 'notes', 
                  'activity_date', 'created_at']
        read_only_fields = ['points_earned', 'created_at']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'title', 'description', 'activity_type', 'difficulty', 
                  'duration_minutes', 'instructions', 'created_at']

class LeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    hero_name = serializers.CharField(source='user.profile.hero_name', read_only=True)
    team_name = serializers.CharField(source='user.profile.team.name', read_only=True)
    
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'username', 'hero_name', 'team_name', 'period', 
                  'points', 'rank', 'period_start', 'period_end', 'updated_at']
