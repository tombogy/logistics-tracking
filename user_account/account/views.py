from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Item, Driver,Trip
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DriverRegistrationForm
from django.contrib import messages




def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


def home(request):
    return render(request, "home.html")

def vehicle(request):
    return render(request,"vehicle.html")   

def category(request):
    return render(request,"category.html")   

def trip(request):
    return render(request,"trip.html")   

def point(request):
    return render(request,"creditpoint.html")   

def password(request):
    return render(request,"password.html")  

def home2(request):
   items = Item.objects.all()
   return render(request, "home2.html", {"items": items}) 



def edit_item(request):
    items = Item.objects.filter(created_by=request.user)
    return render(request, "edit.html", {"items": items})


def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id, created_by=request.user)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.description = request.POST.get("description")
        item.price = request.POST.get("price")
        item.save()
        return redirect("home2")
    return render(request, "update.html", {"item": item})

def add_item(request):
    user = request.user.username
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]
        created_by = User.objects.get(username=user)
        if Item.objects.filter(name=name).exists():
            messages.error(request, "Item already exists")
        else:
            item = Item.objects.create(name=name, description=description, price=price, created_by=created_by)
            item.save()
            return redirect("home2")
    return render(request, "add.html")

def delete_item(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return redirect("edit")


   
# List all drivers
def add_d(request):
    drivers = Driver.objects.all()
    # return render(request, "edit.html", {"items": items})
    return render(request,"driver_table.html",{"drivers":drivers})


def add_driver(request):
    if request.method == "POST":
        name = request.POST["name"]
        mobile= request.POST["mobile"]
        license = request.POST["license"]
        email = request.POST["email"]
        did = request.POST["did"]
        password = request.POST["password"]
        photo = request.POST["photo"]
        obj = Driver(name=name,
                     mobile=mobile,
                     license=license,
                     email=email,
                     did=did,
                     password=password,
                     photo=photo)
        obj.save()
        return redirect('add_d')
    return render(request,"driver2.html")   


def edit_driver(request):
    drivers = Driver.objects.all()
    return render(request, "edit01.html",{"drivers":drivers })


def update_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)

    if request.method == "POST":
        driver.name = request.POST["name"]
        driver.mobile = request.POST["mobile"]
        driver.license = request.POST["license"]
        driver.email = request.POST["email"]
        driver.did = request.POST["did"]
        driver.password = request.POST["password"]
        driver.photo=request.POST["photo"]
        if "photo" in request.FILES:
            driver.photo = request.FILES["photo"]

        # Save the updated driver object
        driver.save()
        messages.success(request, " Driver Deatiles add successfully")
        return redirect('add_d')
    return render(request, "edit_driver.html", {"driver": driver})

def delete_driver(request, id):
    driver = Driver.objects.get( id=id)
    driver.delete()
    return redirect("edit_driver")



#trip
# View for adding a new trip
def add_trip(request):
    if request.method == "POST":
        trip = Trip(
            trip_from=request.POST["trip_from"],
            trip_to=request.POST["trip_to"],
            meter_reading_before=request.POST["meter_reading_before"],
            meter_reading_after=request.POST["meter_reading_after"],
            filled_fuel=request.POST["filled_fuel"],
            credit_point=request.POST["credit_point"],
            trip_mode=request.POST["trip_mode"],
            invoice_document=request.FILES["invoice_document"],
            note=request.POST["note"],
            status_update=request.POST["status_update"],
            location=request.POST["location"],
            report_date=request.POST["report_date"],
            report_time=request.POST["report_time"],
            trip_start_date=request.POST["trip_start_date"],
            trip_end_date=request.POST["trip_end_date"],
            category_name=request.POST["category_name"],
            truck_weight_before=request.FILES["truck_weight_before"],
            truck_weight_after_load=request.FILES["truck_weight_after_load"],
            truck_weight_after_godown=request.FILES["truck_weight_after_godown"]
        )
        trip.save()
        return redirect('trip_list')  # Redirect to the trip list page
    return render(request, "add_trip.html")

# View for editing an existing trip
def edit_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    if request.method == "POST":
        trip.trip_from = request.POST["trip_from"]
        trip.trip_to = request.POST["trip_to"]
        trip.meter_reading_before = request.POST["meter_reading_before"]
        trip.meter_reading_after = request.POST["meter_reading_after"]
        trip.filled_fuel = request.POST["filled_fuel"]
        trip.credit_point = request.POST["credit_point"]
        trip.trip_mode = request.POST["trip_mode"]
        if "invoice_document" in request.FILES:
            trip.invoice_document = request.FILES["invoice_document"]
        trip.note = request.POST["note"]
        trip.status_update = request.POST["status_update"]
        trip.location = request.POST["location"]
        trip.report_date = request.POST["report_date"]
        trip.report_time = request.POST["report_time"]
        trip.trip_start_date = request.POST["trip_start_date"]
        trip.trip_end_date = request.POST["trip_end_date"]
        trip.category_name = request.POST["category_name"]
        if "truck_weight_before" in request.FILES:
            trip.truck_weight_before = request.FILES["truck_weight_before"]
        if "truck_weight_after_load" in request.FILES:
            trip.truck_weight_after_load = request.FILES["truck_weight_after_load"]
        if "truck_weight_after_godown" in request.FILES:
            trip.truck_weight_after_godown = request.FILES["truck_weight_after_godown"]
        trip.save()
        return redirect('trip_list')
    return render(request, "edit_trip.html", {"trip": trip})

# View for deleting a trip
def delete_trip(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    trip.delete()
    return redirect('trip_list')

# View for listing all trips
def trip_list(request):
    trips = Trip.objects.all()
    return render(request, "trip_list.html", {"trips": trips})


