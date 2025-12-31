from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tracker.models import Team, UserProfile, Activity, Workout, Leaderboard
from datetime import datetime, timedelta
import random

class Command(BaseCommand):
    help = 'Populate the database with test data featuring Marvel and DC superheroes'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Avengers assemble! Protecting the world one workout at a time.'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League united! Champions of fitness and justice.'
        )

        self.stdout.write('Creating Marvel heroes...')
        marvel_heroes = [
            ('ironman', 'Tony Stark', 'Iron Man'),
            ('spiderman', 'Peter Parker', 'Spider-Man'),
            ('captainamerica', 'Steve Rogers', 'Captain America'),
            ('blackwidow', 'Natasha Romanoff', 'Black Widow'),
            ('thor', 'Thor Odinson', 'Thor'),
        ]

        self.stdout.write('Creating DC heroes...')
        dc_heroes = [
            ('superman', 'Clark Kent', 'Superman'),
            ('batman', 'Bruce Wayne', 'Batman'),
            ('wonderwoman', 'Diana Prince', 'Wonder Woman'),
            ('flash', 'Barry Allen', 'The Flash'),
            ('aquaman', 'Arthur Curry', 'Aquaman'),
        ]

        users = []
        
        for username, full_name, hero_name in marvel_heroes:
            first_name, last_name = full_name.rsplit(' ', 1)
            user = User.objects.create_user(
                username=username,
                email=f'{username}@marvel.com',
                first_name=first_name,
                last_name=last_name,
                password='hero123'
            )
            profile = UserProfile.objects.create(
                user=user,
                team=team_marvel,
                hero_name=hero_name
            )
            users.append(user)
            self.stdout.write(f'  Created {hero_name}')

        for username, full_name, hero_name in dc_heroes:
            first_name, last_name = full_name.rsplit(' ', 1)
            user = User.objects.create_user(
                username=username,
                email=f'{username}@dc.com',
                first_name=first_name,
                last_name=last_name,
                password='hero123'
            )
            profile = UserProfile.objects.create(
                user=user,
                team=team_dc,
                hero_name=hero_name
            )
            users.append(user)
            self.stdout.write(f'  Created {hero_name}')

        self.stdout.write('Creating activities...')
        activity_types = ['running', 'walking', 'cycling', 'swimming', 'strength', 'yoga', 'sports']
        
        for user in users:
            num_activities = random.randint(3, 8)
            for i in range(num_activities):
                days_ago = random.randint(0, 30)
                activity_date = datetime.now() - timedelta(days=days_ago)
                activity_type = random.choice(activity_types)
                duration = random.randint(15, 120)
                
                activity = Activity.objects.create(
                    user=user,
                    activity_type=activity_type,
                    duration_minutes=duration,
                    distance_km=round(random.uniform(1, 15), 2) if activity_type in ['running', 'walking', 'cycling'] else None,
                    calories_burned=duration * random.randint(5, 12),
                    activity_date=activity_date,
                    notes=f'{user.profile.hero_name} crushing the {activity_type} workout!'
                )
        
        self.stdout.write(f'  Created {Activity.objects.count()} activities')

        self.stdout.write('Creating workout suggestions...')
        workouts_data = [
            {
                'title': 'Superhero Sprint Training',
                'description': 'High-intensity interval training for speed and agility',
                'activity_type': 'running',
                'difficulty': 'intermediate',
                'duration_minutes': 30,
                'instructions': '1. Warm up for 5 minutes\n2. Sprint for 1 minute\n3. Walk for 2 minutes\n4. Repeat 5 times\n5. Cool down for 5 minutes'
            },
            {
                'title': 'Beginner Hero Strength',
                'description': 'Build your foundation with basic strength exercises',
                'activity_type': 'strength',
                'difficulty': 'beginner',
                'duration_minutes': 25,
                'instructions': '1. 10 push-ups\n2. 15 squats\n3. 20-second plank\n4. Rest 1 minute\n5. Repeat 3 times'
            },
            {
                'title': 'Advanced Power Training',
                'description': 'Maximum strength and power development',
                'activity_type': 'strength',
                'difficulty': 'advanced',
                'duration_minutes': 60,
                'instructions': '1. Heavy squats 5x5\n2. Deadlifts 5x5\n3. Bench press 5x5\n4. Pull-ups to failure\n5. Core work 10 minutes'
            },
            {
                'title': 'Zen Warrior Yoga',
                'description': 'Balance, flexibility, and inner peace',
                'activity_type': 'yoga',
                'difficulty': 'beginner',
                'duration_minutes': 45,
                'instructions': '1. Sun salutation sequence\n2. Warrior poses\n3. Tree pose balance\n4. Seated forward fold\n5. Savasana relaxation'
            },
            {
                'title': 'Aquatic Hero Swimming',
                'description': 'Full-body cardio workout in the pool',
                'activity_type': 'swimming',
                'difficulty': 'intermediate',
                'duration_minutes': 40,
                'instructions': '1. Warm up 200m easy\n2. 8x50m freestyle (30s rest)\n3. 4x100m mixed strokes\n4. 200m cool down'
            },
        ]

        for workout_data in workouts_data:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(f'  Created {Workout.objects.count()} workouts')

        self.stdout.write('Creating leaderboard entries...')
        today = datetime.now().date()
        week_start = today - timedelta(days=today.weekday())
        month_start = today.replace(day=1)
        
        for user in users:
            total_points = user.profile.total_points
            
            # All-time leaderboard
            Leaderboard.objects.create(
                user=user,
                period='all_time',
                points=total_points,
                rank=0,
                period_start=today - timedelta(days=365),
                period_end=today
            )

        # Update ranks
        for period in ['all_time']:
            entries = Leaderboard.objects.filter(period=period).order_by('-points')
            for rank, entry in enumerate(entries, start=1):
                entry.rank = rank
                entry.save()
        
        self.stdout.write(f'  Created {Leaderboard.objects.count()} leaderboard entries')

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))
        self.stdout.write(f'Teams: {Team.objects.count()}')
        self.stdout.write(f'Users: {User.objects.filter(is_superuser=False).count()}')
        self.stdout.write(f'Activities: {Activity.objects.count()}')
        self.stdout.write(f'Workouts: {Workout.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
