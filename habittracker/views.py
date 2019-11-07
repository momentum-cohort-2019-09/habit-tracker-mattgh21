from django.shortcuts import render, redirect, get_object_or_404
from habittracker.models import User, Habit, Record, Comment
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone


# Create views here
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.created_at = timezone.now()
            habit.save()
            return redirect('/') 
    else:
        form = HabitForm()
    return render(request, '', {
        'form': form
    })


@csrf_exempt
def home_page(request):
    user = request.user
    return render(request, 'habittracker/home.html', {
        'user': user
    })

@login_required(login_url='/accounts/login/')
@csrf_exempt
def home_logged_in(request):
    habits = Habit.objects.all()
    return render(request, 'habittracker/home_logged_in.html', {
        'habits': habits
    })