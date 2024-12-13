from django.shortcuts import render, redirect
from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, 'captcha_app/success.html')
        else:
            return redirect('failure')
    else:
        form = MyForm()

    return render(request, 'captcha_app/my_form.html', {'form': form})

def failure_view(request):
    return render(request, 'captcha_app/failure.html')
