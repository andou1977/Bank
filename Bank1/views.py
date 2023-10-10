import decimal

from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, status, authentication, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from Bank1.models import Sogebanque, Unibanque
from Bank1.serializers import SogebankSerializer, UnibankSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse



def index(request):
    return render(request, 'index.html')

#create et lister
class SogebankList(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Sogebanque.objects.all()
    serializer_class=SogebankSerializer
    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

#Modifier, supprimer, lister by id
class SogebaankDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Sogebanque.objects.all()
    serializer_class=SogebankSerializer

    def get(self,request,*args,**kwargs):
        try:
          return self.retrieve(request,*args,**kwargs)
        except:
            raise ValidationError('id compte non trouvé')

    def put(self,request,*args, **kwargs):
        id=self.kwargs.get('pk')
        compteid=Sogebanque.objects.get(pk=id)
        if compteid.compte < 20:
            raise ValidationError('compte insuffisant')
        else:
         return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        id=self.kwargs.get('pk')
        compteid=Sogebanque.objects.get(pk=id)

        if compteid.active==False:
            return self.destroy(request,*args, **kwargs)
        else:
            raise ValidationError('vous ne pouvez pas suppeimer un compte active')

#depot
class depotsogebank(mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Sogebanque.objects.all()
    serializer_class=SogebankSerializer

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def update(self,request,montant,*args, **kwargs):
        id=self.kwargs.get('pk')
        compteid=Sogebanque.objects.get(pk=id)
        compteid.compte += decimal.Decimal(float(montant))
        compteid.save()
        return Response("depot ajouter")

#retrait
class retraitSogebank(mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = Sogebanque.objects.all()
    serializer_class = SogebankSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def update(self,request,montant,*args,**kwargs):
        id=self.kwargs.get('pk')
        comptedid=Sogebanque.objects.get(pk=id)
        if decimal.Decimal(float(montant)) <20:
            raise ValidationError("montant ne doit pas etre inferieur a 20")
        else:
            comptedid.compte -=decimal.Decimal(float(montant))
            comptedid.save()
            return Response("retrait effectuer")


#Virement
class Virement(mixins.UpdateModelMixin,generics.GenericAPIView):
    queryset = [Sogebanque.objects.all(),Unibanque.objects.all()]
    serializer_class = [SogebankSerializer,UnibankSerializer]

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def update(self,request,*args,**kwargs):
        idsogebanque=self.kwargs.get('id_sogebanque')#sase la ou recuperer valeur kew pase nan url la
        idunibanque=self.kwargs.get('id_unibanque')#sase la ou recuperer valeur kew pase nan url la
        montant=self.kwargs.get('montant')#sase la ou recuperer valeur kew pase nan url la
        compteidsogebanque=Sogebanque.objects.get(pk=idsogebanque)
        compteidunibanque=Unibanque.objects.get(pk=idunibanque)

        compteidunibanque.compte -= decimal.Decimal(float(montant))
        compteidunibanque.save()
        compteidsogebanque.compte += decimal.Decimal(float(montant))
        compteidsogebanque.save()
        return Response("virement effectuer")




class UnibanqueList(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
    queryset=Unibanque.objects.all()
    serializer_class= UnibankSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



