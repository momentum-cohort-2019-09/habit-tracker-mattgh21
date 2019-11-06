from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from django.views.generic.edit import FormView
from django.utils import timezone

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