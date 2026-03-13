from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
import datetime


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Deleted existing data.')

        # Create superhero users - Marvel heroes
        tony = User.objects.create(
            username='ironman',
            email='tony@avengers.com',
            password='pbkdf2_sha256$placeholder'
        )
        peter = User.objects.create(
            username='spiderman',
            email='peter@avengers.com',
            password='pbkdf2_sha256$placeholder'
        )
        natasha = User.objects.create(
            username='blackwidow',
            email='natasha@avengers.com',
            password='pbkdf2_sha256$placeholder'
        )

        # DC heroes
        bruce = User.objects.create(
            username='batman',
            email='bruce@justice.com',
            password='pbkdf2_sha256$placeholder'
        )
        diana = User.objects.create(
            username='wonderwoman',
            email='diana@justice.com',
            password='pbkdf2_sha256$placeholder'
        )
        clark = User.objects.create(
            username='superman',
            email='clark@justice.com',
            password='pbkdf2_sha256$placeholder'
        )

        self.stdout.write('Created users.')

        # Create teams
        team_marvel = Team.objects.create(name='Team Marvel')
        team_marvel.members.set([tony, peter, natasha])

        team_dc = Team.objects.create(name='Team DC')
        team_dc.members.set([bruce, diana, clark])

        self.stdout.write('Created teams.')

        # Create activities
        Activity.objects.create(
            user=tony, activity_type='Running', duration=45.0,
            date=datetime.date(2024, 1, 15)
        )
        Activity.objects.create(
            user=peter, activity_type='Cycling', duration=60.0,
            date=datetime.date(2024, 1, 16)
        )
        Activity.objects.create(
            user=natasha, activity_type='Strength Training', duration=30.0,
            date=datetime.date(2024, 1, 17)
        )
        Activity.objects.create(
            user=bruce, activity_type='Martial Arts', duration=90.0,
            date=datetime.date(2024, 1, 15)
        )
        Activity.objects.create(
            user=diana, activity_type='Sword Training', duration=75.0,
            date=datetime.date(2024, 1, 16)
        )
        Activity.objects.create(
            user=clark, activity_type='Flying', duration=120.0,
            date=datetime.date(2024, 1, 17)
        )

        self.stdout.write('Created activities.')

        # Create leaderboard entries
        Leaderboard.objects.create(user=tony, score=1500)
        Leaderboard.objects.create(user=peter, score=1800)
        Leaderboard.objects.create(user=natasha, score=2000)
        Leaderboard.objects.create(user=bruce, score=2200)
        Leaderboard.objects.create(user=diana, score=1900)
        Leaderboard.objects.create(user=clark, score=2500)

        self.stdout.write('Created leaderboard entries.')

        # Create workouts
        Workout.objects.create(
            name='Superhero Endurance',
            description='Build endurance like a superhero with this intense cardio workout.',
            exercises=['Running 5km', 'Jumping Jacks 3x50', 'Burpees 3x20']
        )
        Workout.objects.create(
            name='Iron Strength',
            description='Iron Man inspired strength training routine.',
            exercises=['Bench Press 4x10', 'Deadlift 4x8', 'Pull-ups 4x12', 'Shoulder Press 3x10']
        )
        Workout.objects.create(
            name='Spider Agility',
            description='Improve agility and flexibility like Spider-Man.',
            exercises=['Box Jumps 3x15', 'Lateral Shuffles 3x20', 'Balance Drills 3x10', 'Core Rotations 3x15']
        )
        Workout.objects.create(
            name='Dark Knight Training',
            description='Batman\'s intense full-body martial arts conditioning.',
            exercises=['Shadow Boxing 5 rounds', 'Jump Rope 3x3min', 'Push-ups 5x20', 'Plank 3x60sec']
        )
        Workout.objects.create(
            name='Amazonian Warrior',
            description='Wonder Woman\'s warrior conditioning program.',
            exercises=['Sword Lunges 3x12', 'Shield Press 4x10', 'Warrior Squat 4x15', 'Sprint Intervals 5x200m']
        )

        self.stdout.write('Created workouts.')
        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db database with superhero test data!'))
