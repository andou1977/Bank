from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from Bank1.models import Sogebanque, Unibanque


class SogebankSerializer(serializers.ModelSerializer):
    sogebanque_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Sogebanque
        fields=('nom','username','password','email','compte','active','Update_compte','sogebanque_user')

    def validate_username(self,username):
        b=Sogebanque.objects.filter(username=username)
        if b.exists():
            return ValidationError('Ce nom de compte existe déjà')
        else:
            return username


class UnibankSerializer(serializers.ModelSerializer):
    class Meta:
        model=Unibanque
        fields=('nom','username','password','compte','active','Update_compte')

    # def validate_username(self,username):
    #     b=Unibanque.objects.filter(username=username)
    #     if b.exists():
    #        raise serializers.ValidationError('already exists')
    #     else:
    #         return username

    def validate(self,data):

        if data['username']==data['nom']:
            raise serializers.ValidationError('same name and usernmae')
        else:
            return data
