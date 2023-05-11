import Functions as fct
from .models import Scooter
from .forms import LoginForm, RegisterFormCompany, RegisterFormUser
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from scooter_app.models import User as User_data
from scooter_app.models import Company, Charging_station


def start(request):
    return render(request, 'index.html')


def login_view(request):
    if request.user.is_authenticated:
        user_mode = fct.user_mode(request.user.id)
        if user_mode == 'setup':
            return redirect('setup-mode')
        elif user_mode == 'operative':
            return redirect('operative-mode')

    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)

                user_mode = fct.user_mode(request.user.id)
                if user_mode == 'setup':
                    return redirect('setup-mode')
                elif user_mode == 'operative':
                    return redirect('operative-mode')
                
    return render(request, 'login.html', {'login_form': login_form})


# Setup Mode
def register_view_user(request):
    if request.user.is_authenticated:
        user_mode = fct.user_mode(request.user.id)
        if user_mode == 'setup':
            return redirect('setup-mode')
        elif user_mode == 'operative':
            return redirect('operative-mode')

    register_form = RegisterFormUser()

    if request.method == 'POST':
        register_form = RegisterFormUser(request.POST)
        if register_form.is_valid():
            
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            street = register_form.cleaned_data['street']
            postalcode = register_form.cleaned_data['postalcode']
            city = register_form.cleaned_data['city']
            email = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']

            User.objects.create_user(username=email, password=password, email=email, first_name=first_name, last_name=last_name)
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)

                # User in zusätzlicher Tabelle anlegen
                User_data.objects.create(mode='operative', company_id=0, street=street, postalcode=postalcode, city=city, user=request.user)

                return redirect('operative-mode')

    return render(request, 'register.html', {'register_form': register_form})


# Operative Mode
def register_view_company(request):
    if request.user.is_authenticated:
        user_mode = fct.user_mode(request.user.id)
        if user_mode == 'setup':
            return redirect('setup-mode')
        elif user_mode == 'operative':
            return redirect('operative-mode')

    register_form = RegisterFormCompany()

    if request.method == 'POST':
        register_form = RegisterFormCompany(request.POST)
        if register_form.is_valid():
            
            company_name = register_form.cleaned_data['name']
            street = register_form.cleaned_data['street']
            postalcode = register_form.cleaned_data['postalcode']
            city = register_form.cleaned_data['city']
            email = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']

            User.objects.create_user(username=email, password=password, email=email, first_name=company_name)
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                company_id = fct.create_id()

                # Company in zusätzlicher Tabelle anlegen
                User_data.objects.create(company_id=company_id, mode='setup', street=street, postalcode=postalcode, city=city, user=request.user)
                Company.objects.create(company_id=company_id, name=company_name, street=street, postalcode=postalcode, city=city)
                
                return redirect('setup-mode')

    return render(request, 'register.html', {'register_form': register_form})


def lougout_view(request):
    logout(request)
    return redirect('start')


@login_required
def mode_operative(request):

    # Prüfe ob Nutzer im Setup oder Operative Mode ist
    user_mode = fct.user_mode(request.user.id)
    if user_mode == 'setup':
        return redirect('setup-mode')


    scooter_items = Scooter.objects.all()
    station_items = Charging_station.objects.all()

    return render(request, 'mode-operative.html', {'scooter_items': scooter_items, 'station_items': station_items})


@login_required
def mode_setup(request):

    # Prüfe ob Nutzer im Setup oder Operative Mode ist
    user_mode = fct.user_mode(request.user.id)
    if user_mode == 'operative':
        return redirect('operative-mode')

    if request.method == 'POST':

        if request.POST['typ'] == 'add':

            # get user
            user = User_data.objects.get(user__exact=request.user.id)
            # get company
            company = Company.objects.get(company_id__exact=user.company_id)

            if request.POST['itemName'] == 'scooter':    
                fct.create_scooter(name=company.name, company_id=company.company_id, latitude=request.POST['latitude'], longitude=request.POST['longitude'])
            elif request.POST['itemName'] == 'station':
                fct.create_chargingStation(name=company.name, company_id=company.company_id, latitude=request.POST['latitude'], longitude=request.POST['longitude'])

        elif request.POST['typ'] == 'delete':
            
            if request.POST['itemName'] == 'scooter':
                fct.delete_scooter(request.POST['id'])
            elif request.POST['itemName'] == 'station':
                fct.delete_chargingStation(request.POST['id'])


    scooter_items = Scooter.objects.all()
    station_items = Charging_station.objects.all()

    data = {'scooter_items': scooter_items, 'station_items': station_items}

    return render(request, 'mode-setup.html', data)


@login_required
def settings(request):

    if request.method == 'POST':
        if request.POST['action'] == 'company-change':
            company_id = request.POST['company']
            user = User_data.objects.get(user_id__exact=request.user.id)
            user.company_id = company_id
            user.save()

    company_items = Company.objects.all()
    data = {'company_items': company_items}

    user_mode = fct.user_mode(request.user.id)
    if user_mode == 'operative':
        user = User_data.objects.get(user__exact=request.user.id)
        adress = {'street': user.street, 'postalcode': user.postalcode, 'city': user.city}
        data.update(adress)
        
    elif user_mode == 'setup':
        user = User_data.objects.get(user__exact=request.user.id)

        if Company.objects.filter(company_id__exact=user.company_id).exists():
            company = Company.objects.get(company_id__exact=user.company_id)
            adress = {'street': company.street, 'postalcode': company.postalcode, 'city': company.city}
            data.update(adress)

    return render(request, 'settings.html', data)


@login_required
def dashboard(request):
    
    return render(request, 'dashboard.html')
