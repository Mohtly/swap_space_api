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

class CreateMatches(graphene.Mutation):
    item_id_1 = graphene.Int()
    item_id_2 = graphene.Int()

    class Arguments:
    	item_id_1 = graphene.Int()
    	item_id_2 = graphene.Int()

    def mutate(self, info, item_id_1, item_id_2):
        matches = Matches(item_id_1=item_id_1, item_id_2=item_id_2)
        matches.save()

        return CreateMatches(
            item_id_1=matches.item_id_1,
            item_id_2=matches.item_id_2
        )

#4
class Mutation(graphene.ObjectType):
    create_matches = CreateMatches.Field()
