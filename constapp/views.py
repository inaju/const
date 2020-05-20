from django.shortcuts import render, HttpResponseRedirect
from .models import GoalModel, GoalsList    
from .forms import GoalFormGoal,GoalFormDate, GoalFormCheck

# Create your views here.
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GoalFormGoal.Goal(request.POST or None)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/show')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GoalFormGoal()
        
    return render(request, 'index.html', {'form': form})



def Show(request):
    show=GoalModel.objects.all()

    return render(request, 'show.html', {'show': show})



def goals(request):

    show_goals=GoalsList.objects.all()
    
    return render(request, 'goals.html', {'show_goals': show_goals})
