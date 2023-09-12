from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import PersonCreationForm
from django.shortcuts import render, redirect,get_object_or_404

from .models import Person, Branch, District


# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('person_add')
        else:
            messages.info(request,"invalid login")
            return redirect('login')
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
            user.save();
            return redirect('login')
        else:
            return redirect('register')
        return redirect('/')

    return render(request,"register.html")


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted!')
            return redirect('person_add')
    return render(request, 'requa.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted!')
            return redirect('person_change', pk=pk)
    return render(request, 'requa.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'district.html', {'branches': branches})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def logout(request):
      auth.logout(request)
      return render(request,'login.html')
