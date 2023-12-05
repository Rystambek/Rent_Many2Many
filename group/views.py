from django.http import HttpRequest, JsonResponse
from .models import Group
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from app.models import Car, Customer
from app.views.customer import to_dict
import json

def to_dict_group(group:Group) -> dict:
    return {
        'id':group.id,
        'name':group.name,
        'students':[to_dict(student) for student in group.student.all()]
    }

class Get_GroupsView(View):
    def get(self,request:HttpRequest, id = None) -> JsonResponse:
        if id is not None:
            try:
                group = Group.objects.get(id = id)
                return JsonResponse(to_dict_group(group))
            except ObjectDoesNotExist:
                return JsonResponse({'result':'object does not exist!'})
            
        else:
            groups = Group.objects.all()
            result = [to_dict_group(group) for group in groups]
            return JsonResponse({'result':result})
        
    def post(self,request:HttpRequest) -> JsonResponse:
        data_json = request.body.decode()
        data = json.loads(data_json)

        if not data['name']:
            return JsonResponse({'status':"name yo'q"})
        
        group = Group.objects.create(
            name = data['name']
        )

        return JsonResponse(to_dict_group(group))
    
    def put(self,request:HttpRequest, id = None) -> JsonResponse:
        try:
            group = Group.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        data_json = request.body.decode()
        data = json.loads(data_json)

        if data.get('name'):
            group.name = data['name']

        group.save()

        return JsonResponse(to_dict_group(group))

    def delete(self,request:HttpRequest, id = None) -> JsonResponse:
    
        try:
            group = Group.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})

        group.delete()

        return JsonResponse({'status': 'ok'})

class GruopId_All_Students(View):
    def get(self,request:HttpRequest, id = None) -> JsonResponse:
        try:
            group = Group.objects.get(id = id)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 'object does not exist!'})
        
        students = to_dict_group(group)['students']
        return JsonResponse(students,safe=False)
    
class remove(View):
    def delete(self,request:HttpRequest,gr_id,id) -> JsonResponse:
            try:
                student = Customer.objects.get(id = id)
                group = Group.objects.filter(id = gr_id,student=student)
                
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'object does not exist!'})
                
            group.delete()
            return JsonResponse({"status":200})