from django.shortcuts import render, redirect, get_object_or_404
from habittracker.models import User, Habit, Record, Comment
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .forms import HabitForm, RecordForm


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

@login_required
def add_record(request, pk):
    habit = Habit.objects.get(pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.habit = habit
            record.save()
            return redirect(to='record', pk=pk)
    else:
        form = RecordForm()
        records = Record.objects.filter(habit=habit)
        return render(request, 'habittracker/record.html',{'form':form, 'habit':habit, 'records': records})

# def edit_habit(request, pk):
#     habit = get_object_or_404(Habit, pk=pk)
#     if request.method == 'POST':
#         habit = request.data

def edit_habit(request, pk):
    habit = get_object_or_404(Habit, id=pk)
    if request.method == "POST":
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.updated_at = timezone.now()
            habit.save()
            return redirect(to='profile')
    else:
        form = HabitForm()
    return render(request, 'habittracker/edit_habit.html',{
        'form': form
    })

def delete_habit(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect(to='profile')

def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    record.delete()
    return redirect(to='record')
    
