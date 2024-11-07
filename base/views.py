from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


@login_required
def homeView(request):
    return render(request, 'home.html')


def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {"form": form})