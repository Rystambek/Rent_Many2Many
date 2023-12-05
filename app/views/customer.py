from django.views import View
from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from app.models import Customer
import json

def to_dict(customer:Customer) -> dict:

    return {
        "id":customer.pk,
        "first_name":customer.first_name,
        "last_name":customer.last_name,
        "phone_number":customer.phone_number,
        "email":customer.email,
        "address":customer.address,
        "birtday_day":customer.birtday_day,
        "gender":customer.gender,
        "age":customer.age,
        "username":customer.username

    }

class CustomerView(View):
    def get(self,request:HttpRequest,id = None) -> JsonResponse:
        if id is not None:
            try:
                customer = Customer.objects.get(id = id)
                return JsonResponse(to_dict(customer))
            except ObjectDoesNotExist:
                return JsonResponse({'result':'object does not exist!'})
            
        else:
            query_params = request.GET
            age = query_params.get('age')
            if age is not None:
                customers_all = Customer.objects.filter(age = age)
            else:
                customers_all = Customer.objects.all()
            result = [to_dict(customer) for customer in customers_all]
            return JsonResponse({'result':result})
    
    def post(self, request:HttpRequest) -> JsonResponse:
        data_json = request.body.decode()
        data = json.loads(data_json)

        if not data.get('first_name'):
            return JsonResponse({'status': 'first_name is required!'})
        elif not data.get('phone_number'):
            return JsonResponse({'status': 'phone_number is required!'})
        elif not data.get('email'):
            return JsonResponse({'status': 'email is required!'})
        elif not data.get('birtday_day'):
            return JsonResponse({'status': 'birtday_day is required!'})
        elif not data.get('gender'):
            return JsonResponse({'status': 'gender is required!'})
        elif not data.get('age'):
            return JsonResponse({'status': 'age is required!'})
        elif not data.get('username'):
            return JsonResponse({'status': 'username is required!'})
        
        customer = Customer.objects.create(
            first_name = data['first_name'],
            last_name = data.get('last_name',''),
            phone_number  = data['phone_number'],
            email = data['email'],
            address = data.get('address',''),
            birtday_day = data['birtday_day'],
            gender = data['gender'],
            age = data['age'],
            username = data['username']
        )

        customer.save()

        return JsonResponse(to_dict(customer))
    def put(self, request:HttpRequest,id = None) -> JsonResponse:
        try:
            customer = Customer.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        data_json = request.body.decode()
        data = json.loads(data_json)

        if data.get('first_name'):
            customer.first_name = data['first_name']
        if data.get('last_name'):
            customer.last_name = data['last_name']
        if data.get('phone_number'):
            customer.phone_number = data['phone_number']
        if data.get('email'):
            customer.email = data['email']
        if data.get('address'):
            customer.address = data['address']
        if data.get('birtday_day'):
            customer.birtday_day = data['birtday_day']
        if data.get('gender'):
            customer.gender = data['gender']
        if data.get('age'):
            customer.age = data['age']
        if data.get('username'):
            customer.username = data['username']

        customer.save()

        return JsonResponse(to_dict(customer=customer))
    
    def delete(self, request:HttpRequest,id = None) -> JsonResponse:
        try:
            customer = Customer.objects.get(id = id)

        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        customer.delete()

        return JsonResponse({'status':'ok'})