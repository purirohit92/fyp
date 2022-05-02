import datetime

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import BadHeaderError, send_mail
from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import View
from .models import Cart, CartItem, Product, ProductImage
from django.db.models import Prefetch,Q
from .urls import *

# Create your views here.


def HomePage(request):
    queryset = Product.objects.prefetch_related(
        Prefetch("images", queryset=ProductImage.objects.all())).all()
    context = {
        'products': queryset,
        # 'photos':[product.images.first().image.url for product in queryset]
        'cart_item_count': CartItem.objects.filter(cart__user=request.user, cart__status=0).count() if request.user.is_authenticated else 0
    }
    return render(request, 'index.html', context=context)


def product(request):
    queryset = Product.objects.prefetch_related(
    Prefetch("images", queryset=ProductImage.objects.all())).all()
    context = {
        'products': queryset,
        'cart_item_count': CartItem.objects.filter(cart__user=request.user, cart__status=0).count() if request.user.is_authenticated else 0,
        'mens_count':queryset.filter(type__icontains='men').count(),
        'women_count':queryset.filter(type__icontains='women').count(),
        'children_count':queryset.filter(type__icontains='children').count(),
    }
    return render(request, 'shop.html', context=context)
#
#
# class AboutPage(View):
#     def get(self, request):
#         return render(request, 'about.html')
#
#


class Productdetails(View):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        photos = ProductImage.objects.all().filter(product=product)
        context = {'product': product, 'photos': photos}
        return render(request, 'shop-details.html', context=context)
#
#
# @method_decorator(login_required(login_url='/login'), name='dispatch')
# class BookingView(View):
#     def get(self, request):
#         return render(request, 'bookings.html')
#
#
# class ContactView(View):
#
#     def get(self, request):
#         return render(request, 'contact.html')
#
#     def post(self, request):
#         if request.method == "POST":
#             name = request.POST.get('name')
#             email = request.POST.get('email')
#             subject = request.POST.get('subject')
#             message = request.POST.get('message')
#             contact = Contact(name=name, email=email, message=message, subject=subject)
#             contact.save()
#             messages.success(request, 'Your Inquiry has been submitted. Thank you!')
#             return redirect("contact")
#         messages.error(request, 'There is problem with submission. Please Try Again')
#         return redirect("contact")


class RegisterView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            email = request.POST.get('email')

            password = request.POST.get('password')
            print(request.POST)
            password_cf = request.POST.get('confirm_pw')

            if password == password_cf:
                if User.objects.filter(username=username).exists():
                    message = "User already exists."
                    print(message)
                else:
                    user = User.objects.create_user(
                        first_name=first_name, last_name=last_name, username=username, password=password, email=email)  # type: ignore
                    user.save()
                    messages.success(request, 'Your Account has been created')
                    auth.login(request, user)
                    return redirect('index')
            else:
                message = "Passwords do not match"
                print(message)
            context = {
                'error_msg': 'message'
            }
            return render(request, 'index.html', context=context)
        else:
            return redirect('login')


# class ForgetPasswordView(View):
#     def get(self, request):
#         return render(request, 'forgetPassword.html')
#
#
# class GalleryView(View):
#     def get(self, request):
#         images = Gallery.objects.all()
#         context = {'images': images}
#         return render(request, 'Gallery.html', context=context)


class LoginView(View):
    def get(self, request):
        print(request.user)
        return render(request, 'signin.html')

    def post(self, request):
        if request.method == "POST":
            print(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
            user = auth.authenticate(username=username, password=password)
            print('fsa', user)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "User Success")
                return redirect("index")
            else:
                message = "Invalid login details."
                print(message)
                return redirect("login")
        else:
            return render(request, 'signin.html')

#
# @method_decorator(login_required(login_url='/login'), name='dispatch')
# class CancelBookingsView(View):
#     def get(self, request):
#         cancel_bookings = MyBooking.objects.get(name=request.user)
#         if cancel_bookings:
#             if cancel_bookings.name == request.user:
#                 cancel_bookings.delete()
#                 messages.success(request, "Bookings Cancelled")
#                 return redirect("my_bookings")
#         return redirect('home')
#
#
# @method_decorator(login_required(login_url='/login'), name='dispatch')
# class MyBookingsView(View):
#     def get(self, request):
#         try:
#             my_bookings = MyBooking.objects.get(name=request.user)
#         except:
#             my_bookings = ""
#         context = {'my_booking': my_bookings}
#         return render(request, 'myBookings.html', context=context)
#
#     def post(self, request):
#         if request.method == 'POST':
#             arrival_date = request.POST.get('arrival_date')
#             departure_date = request.POST.get('departure_date')
#             room = request.POST.get('room')
#             nights = request.POST.get('nights')
#             adults = request.POST.get('adults')
#             children = request.POST.get('children')
#             number = request.POST.get('number')
#             address = request.POST.get('address')
#             message = request.POST.get('message')
#             print(datetime.date.today())
#             print(arrival_date)
#             print(departure_date)
#             print(nights)
#
#             give = str(arrival_date)
#             give_time = give.split("-")
#
#             give1 = str(departure_date)
#             give_time1 = give.split("-")
#             print(int(give_time[0]))
#             print(int(give_time[1]))
#             print(int(give_time[2]))
#
#             times1 = datetime.date.today()
#             timess = datetime.date(int(give_time[0]),int(give_time[1]),int(give_time[2]))
#             timess1 = datetime.date(int(give_time1[0]),int(give_time1[1]),int(give_time1[2]))
#             if (timess>=times1 and timess1>=times1):
#                 has_made_booking = MyBooking.objects.all().filter(name=request.user)
#
#                 if has_made_booking:
#                     messages.error(request, 'Your have already made booking.')
#                     return redirect('booking')
#                 book = MyBooking(name=request.user, arrival_date=arrival_date, departure_date=departure_date,
#                                 room_select=room,
#                                 num_nights=nights, num_person=adults, num_children=children, phone_num=number,
#                                 address=address, des=message,)
#                 book.save()
#                 return redirect('my_bookings')
#             else:
#                 messages.info(request,"Date is not correct. Please change the date")
#                 print("go back home")
#             # has_made_booking = MyBooking.objects.all().filter(name=request.user)
#
#             # if has_made_booking:
#             #     messages.error(request, 'Your have already made booking.')
#             #     return redirect('booking')
#             # book = MyBooking(name=request.user, arrival_date=arrival_date, departure_date=departure_date,
#             #                  room_select=room,
#             #                  num_nights=nights, num_person=adults, num_children=children, phone_num=number,
#             #                  address=address, des=message,)
#             # book.save()
#             return redirect('booking')
#         return redirect('booking')
#
#


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect("login")

#
# def password_reset_request(request):
#     if request.method == "POST":
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             data = password_reset_form.cleaned_data['email']
#             print(data)
#             associated_users = User.objects.filter(Q(email=data))
#             print(associated_users)
#             if associated_users.exists():
#                 for user in associated_users:
#                     subject = "Password Reset Requested"
#                     email_template_name = "password_reset_email.txt"
#                     c = {
#                         "email": user.email,
#                         'domain': '127.0.0.1:8000',
#                         'site_name': 'Website',
#                         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                         "user": user,
#                         'token': default_token_generator.make_token(user),
#                         'protocol': 'http',
#                     }
#                     email = render_to_string(email_template_name, c)
#                     try:
#                         send_mail(subject, email, 'admin@gmail.com', [user.email], fail_silently=False)
#                     except BadHeaderError:
#                         return HttpResponse('Invalid header found.')
#                     return redirect("/password_reset/done/")
#     password_reset_form = PasswordResetForm()
#     return render(request=request, template_name="forgetPassword.html",
#                   context={"password_reset_form": password_reset_form})
#


@login_required(login_url='login')
def cart(request):
    # Product.objects.prefetch_related(Prefetch("images",queryset=ProductImage.objects.all())).all()
    if request.user.is_authenticated:
        cart_item_obj = CartItem.objects.filter(
            cart__user=request.user, cart__status=0)
        all_cart_total = 0
        for i in cart_item_obj:
            all_cart_total += i.cart_total()
        try:
            context = {
                "cart_items": cart_item_obj,
                'all_cart_total': all_cart_total,
                'cart_id': Cart.objects.filter(user=request.user, status=0).first().id
            }
        except Exception as e:
            print(e)
            context = {
                "cart_items": cart_item_obj,
                'all_cart_total': all_cart_total,
                'no_items':True
            }
            print(context)

    return render(request, "shopping-cart.html", context=context)


# def product(request):
#     return render(request, "product.html")
#
# def contactus(request):
#     return render(request, "contactus.html")
#
# def productdetails(request):
#     return render(request, "product-details.html")


@login_required(login_url='login')
def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        try:
            cart_obj = Cart.objects.get(user=request.user,status=0)
        except Cart.DoesNotExist:
            cart_obj = Cart.objects.create(user=request.user)
        cart_item_obj = CartItem.objects.filter(
            product=Product.objects.get(id=product_id), cart=cart_obj)
        if cart_item_obj.exists():
            cart_item_obj.update(quantity=cart_item_obj.first().quantity+1)
        else:
            cart_item_obj = CartItem.objects.create(
                product=Product.objects.get(id=product_id), cart=cart_obj)
        print(cart_item_obj)
        return redirect("index")
    return redirect("index")


def remove_from_cart(request, item_id):
    if request.user.is_authenticated:
        CartItem.objects.filter(id=item_id).delete()
    return redirect("cart")


def complete_payment(request, cart_id):
    if request.user.is_authenticated:
        Cart.objects.filter(id=cart_id).update(status=1)
    return redirect("cart")

def search(request):
    q_objects = Q()
    queryset = Product.objects.all()
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        q_objects.add(Q(description__icontains=keywords) | Q(name__icontains=keywords),Q.AND)
        queryset = queryset.filter(q_objects)
    context = {
        'products': queryset,
        'cart_item_count': CartItem.objects.filter(cart__user=request.user, cart__status=0).count() if request.user.is_authenticated else 0,
        'mens_count':queryset.filter(type__icontains='men').count(),
        'women_count':queryset.filter(type__icontains='women').count(),
        'children_count':queryset.filter(type__icontains='children').count(),
        'values': request.GET,
    }
    print(context)
    return render(request, 'search.html', context=context)
