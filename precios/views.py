from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def BASE(request):
    return render(request, 'base.html')
