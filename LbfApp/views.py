from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from . models import CustomUser, Item
from . forms import RegisterForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def dashboard(request):
    if request.method == "GET":
        q = request.GET.get('q')

        if q is not None:
            q = q
        else:
            q = ''

    items = Item.objects.filter(
        Q(status='missing') & (Q(name__icontains=q) | Q(location_found__icontains=q) | Q(description__icontains=q))
    )
    retrieved_items = Item.objects.filter(status='retrieved')
    laptop = 'laptop'
    context = {'items':items, 'laptop':laptop,'retrieved_items':retrieved_items}
    return render(request,"LbfApp/dashboard.html",context)

@login_required(login_url='/login')
def report(request):
    if request.method == "POST":
        item = Item.objects.create(
            user =request.user,
            name = request.POST.get('name'),
            description = request.POST.get('description'),
            location_found = request.POST.get('location_found'),
            contact = request.user.phone_number,
            image = request.FILES.get('image'),
            status = 'missing',

        )
        return redirect('dashboard')
    return render(request,"LbfApp/report.html")

def update_status(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    # Update the status (toggle between 'missing' and 'retrieved' for example)
    item.status = 'retrieved' if item.status == 'missing' else 'missing'
    item.save()

    # Redirect back to the item's detail page or any other desired destination
    return redirect('dashboard')

@login_required(login_url='/login')
def profile(request):
    user = request.user
    form = UpdateUserForm(instance=user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST,request.FILES,instance=user)
        if form.is_valid():
            
            form.save()
            return redirect('profile')    
    return render(request,"LbfApp/profile.html",{'form':form})
        
def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:    
        if request.method == "POST":
            email = request.POST["email" ]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                error_message = "Invalid Email Or Password"
                return render(request,"LbfApp/login.html",{"error_message":error_message})

    return render(request,"LbfApp/login.html")


def register(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            form = RegisterForm()
            if request.method == "POST":
                form = RegisterForm(request.POST,request.FILES)
                if form.is_valid():
                    user = form.save(commit=False)
                    user.username = user.username.lower()
                    user.save()
                    messages.info(request, "Account was create for " + form.cleaned_data.get('username'))
                    login(request, user)
                    return redirect('dashboard')
                else:
                    error_message = "Invalid Credentials or Format" 
                    context = {"error_message":error_message}   

            context = {"form":form}  
            return render(request,"LbfApp/register.html",context)

def logout_user(request):
    logout(request)

    return redirect('dashboard')


@login_required(login_url='/login')
def edit_profile(request):
    return render(request,"LbfApp/edit_profile.html")

@login_required(login_url='/login')
def settings(request):
    return render(request,"LbfApp/settings.html")

