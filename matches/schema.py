import graphene
from graphene_django import DjangoObjectType

from .models import Matches


class MatchesType(DjangoObjectType):
    class Meta:
        model = Matches


class Query(graphene.ObjectType):
    matches = graphene.List(MatchesType)

    def resolve_matches(self, info, **kwargs):
        return Matches.objects.all()