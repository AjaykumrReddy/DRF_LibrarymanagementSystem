from django.shortcuts import render
from admins.models import AdminRegistration, Library


def index(request):
    return render(request, 'index.html')


def admin_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            model = AdminRegistration(
                name=name, email=email, password=password)
            model.save()
            return render(request, 'admin_register.html', {'success': 'Success'})
        except Exception as e:
            print(e)
            return render(request, 'admin_register.html', {'error': e})
    else:
        return render(request, 'admin_register.html')


def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            admin = AdminRegistration.objects.get(
                email=email, password=password)
            return render(request, 'admin/admin_home.html', {'admin': admin})
        except Exception as e:
            return render(request, 'admin_login.html', {'error': e})
    else:
        return render(request, 'admin_login.html')


def view_all_books(request):
    books = Library.objects.all()
    return render(request, 'view_all_books.html', {'books': books})
