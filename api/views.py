import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import usuarios
# Create your views here.
class usuariosview(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0 ):
        if (id>0):
            usuariosGET = list(usuarios.objects.filter(id=id).values())
            if len(usuariosGET)>0:
                users = usuariosGET[0]
                datos={'message':"success",'usuarios':users}
            else:
                datos={'message':"no data found..."}
            return JsonResponse(datos)
        else:
            usuariosGET = list(usuarios.objects.values()) 
            if len(usuariosGET)>0:
                datos={'message':"success",'usuarios':usuariosGET}
            else:
                datos={'message':"not response..."} 
            return JsonResponse(datos)
        

    def post(self, request ):
        dataUser = json.loads(request.body)
        usuarios.objects.create(name=dataUser['name'],last_name=dataUser['last_name'],contactmail = dataUser['contactmail'], cellphone = dataUser['cellphone'])
        datos={'message':"success"}
        return JsonResponse(datos)

    def put(self, request, id):
        dataUser = json.loads(request.body)
        usuariosGET = list(usuarios.objects.filter(id=id).values())
        if len(usuariosGET) > 0:
            Usuariosput = usuarios.objects.get(id=id)
            Usuariosput.name = dataUser['name']
            Usuariosput.last_name = dataUser['last_name']
            Usuariosput.cellphone = dataUser['cellphone']
            Usuariosput.contactmail = dataUser['contactmail']
            Usuariosput.save()
            datos = {'message': "success!!!"}
        else:
            datos={'message':"not found..."}
        return JsonResponse(datos)

    def delete(self, request,id ):
        usuariosGET = list(usuarios.objects.filter(id=id).values())
        if len(usuariosGET)>0:
            usuarios.objects.filter(id=id).delete()
            datos = {'message': "success!!!"}
        else:
            datos = {'message': "not found!!!"}
        return JsonResponse(datos)