import graphene
from graphene_django import DjangoObjectType

from .models import Item

class ItemType(DjangoObjectType):
    class meta:
        model = Item

