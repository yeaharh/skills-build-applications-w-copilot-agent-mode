from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Team, UserProfile, Activity, Workout, Leaderboard
from .serializers import (
    TeamSerializer, UserProfileSerializer, ActivitySerializer,
    WorkoutSerializer, LeaderboardSerializer
)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.AllowAny]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        queryset = Activity.objects.all()
        user_id = self.request.query_params.get('user', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=False, methods=['get'])
    def recommended(self, request):
        difficulty = request.query_params.get('difficulty', 'beginner')
        workouts = Workout.objects.filter(difficulty=difficulty)[:5]
        serializer = self.get_serializer(workouts, many=True)
        return Response(serializer.data)

class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        queryset = Leaderboard.objects.all()
        period = self.request.query_params.get('period', 'all_time')
        queryset = queryset.filter(period=period)
        return queryset.order_by('rank')[:10]
