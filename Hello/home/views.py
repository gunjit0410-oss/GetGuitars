from django.shortcuts import render, redirect #,HttpResponse
from datetime import datetime
from home.models import Contact, Guitar
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login/")
    return render(request, 'index.html')
   # return HttpResponse("This is a home page")
def services(request):
    return render(request, 'services.html')
   
def about(request):
    return render(request, 'about.html')

def acoustic(request):
    return render(request, 'acoustic.html')

def electric(request):
    return render(request, 'electric.html')
    
def bass(request):
    return render(request, 'bass.html')

def ukulele(request):
    return render(request, 'ukulele.html')

def covers(request):
    return render(request, 'covers.html')

def straps(request):
    return render(request, 'straps.html')

def amplifiers(request):
    return render(request, 'amplifiers.html')

def picks(request):
    return render(request, 'picks.html')
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent !!')
    return render(request, 'contact.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)   # ✅ correct
            return redirect("/")
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutUser(request):
    auth_logout(request)
    return redirect("/login/")

def api_guitar_list(request):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    guitars = []
    for g in Guitar.objects.all():
        guitars.append({
            'id': g.id,
            'name': g.name,
            'brand': g.brand,
            'price': g.price,
            'image_url': g.image,
            'amazon_link': g.amazon_link,
            'flipkart_link': g.flipkart_link,
        })
    return JsonResponse(guitars, safe=False)

def api_guitar_detail(request, guitar_id):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        g = Guitar.objects.get(id=guitar_id)
        data = {
            'id': g.id,
            'name': g.name,
            'brand': g.brand,
            'price': g.price,
            'image_url': g.image,
            'amazon_link': g.amazon_link,
            'flipkart_link': g.flipkart_link,
        }
        return JsonResponse(data)
    except Guitar.DoesNotExist:
        return JsonResponse({'error': 'Guitar not found'}, status=404)

@csrf_exempt
def api_contact_submit(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    try:
        data = json.loads(request.body)
        name = data.get('name')
        phone = data.get('phone', '')
        email = data.get('email')
        desc = data.get('desc', '')
        
        if not name or not email:
            return JsonResponse({'error': 'Name and Email are required fields'}, status=400)
            
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        return JsonResponse({
            'success': True,
            'message': 'Contact entry created successfully',
            'id': contact.id
        }, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON body'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

def search(request):
    query = request.GET.get('query', '').strip()
    if query:
        products = Guitar.objects.filter(
            Q(name__icontains=query) | Q(brand__icontains=query)
        )
    else:
        products = Guitar.objects.none()
        
    context = {
        'products': products,
        'query': query
    }
    return render(request, 'search.html', context)
    
