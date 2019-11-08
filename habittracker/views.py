from django.shortcuts import render, redirect, get_object_or_404
from habittracker.models import User, Habit, Record, Comment
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .forms import HabitForm


# Create views here
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = user
            habit = form.save()
            return redirect(to='profile') 
    else:
        form = HabitForm()
        user_habits = Habit.objects.filter(user=request.user)
    return render(request, 'habittracker/profile.html', {'user':user, 'form':form, 'habits': user_habits})


 

@csrf_exempt
@login_required
def home_page(request):
    user = request.user
    all_habits = Habit.objects.all()
    return render(request, 'habittracker/home.html', {
        'user': user, 'all_habits': all_habits
    })

# @login_required
# def profile_page(request, pk):
#     habits = Habit.objects.filter(user=User.objects.get(pk=pk))
#     return render(request, 'habittracker/profile.html', {'habits': habits})
