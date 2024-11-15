from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Habit, Progress
from .forms import HabitForm, ProgressForm
from django.contrib.auth.decorators import login_required
import datetime

# Home page displaying all habits
def home(request):
    habits = Habit.objects.all()
    progress_data = {}
    
    for habit in habits:
        progress_data[habit] = Progress.objects.filter(habit=habit).order_by('date')

    return render(request, 'home.html', {'habits': habits, 'progress_data': progress_data})

# Add a new habit
@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HabitForm()
    return render(request, 'add_habit.html', {'form': form})

# Track progress for a specific habit
@login_required
def track_progress(request, habit_id):
    habit = Habit.objects.get(id=habit_id)
    
    # Handle form submission for marking habit as completed or skipped
    if request.method == 'POST':
        date = datetime.date.today()
        completed = 'completed' in request.POST
        
        # Create or update progress for today
        progress, created = Progress.objects.get_or_create(habit=habit, date=date)
        progress.completed = completed
        progress.save()
        
        return redirect('home')

    return render(request, 'track_progress.html', {'habit': habit})
