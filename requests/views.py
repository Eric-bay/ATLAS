from django.shortcuts import render, redirect
from .models import Request, Requester, Buyer
from .forms import RequestForm
from django.contrib.auth.decorators import login_required

@login_required
def request_list(request):
    requests = Request.objects.all()
    return render(request, 'requests/request_list.html', {'requests': requests})

@login_required
def request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_obj = form.save(commit=False)
            request_obj.save()
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'requests/request_form.html', {'form': form})
