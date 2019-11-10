import graphene
from graphene_django import DjangoObjectType

from .models import Item


class ItemType(DjangoObjectType):
    class Meta:
        model = Item


class Query(graphene.ObjectType):
    items = graphene.List(ItemType)

    def resolve_items(self, info, **kwargs):
        return Item.objects.all()

# class CreateItem(graphene.Mutation):
#     item_id = graphene.Int()
#     photo = graphene.String()
#     value_low = graphene.Int()
#     value_high = graphene.Int()
#     description = graphene.Int()
#     traded = graphene.Boolean()
#     date_time_created = graphene.types.datetime.DateTime()
#
#
#     #2
#     class Arguments:
#         url = graphene.String()
#         description = graphene.String()
#
#     #3
#     def mutate(self, info, url, description):
#         link = Link(url=url, description=description)
#         link.save()
#
#         return CreateLink(
#             id=link.id,
#             url=link.url,
#             description=link.description,
#         )
#
#
# #4
# class Mutation(graphene.ObjectType):
#     create_link = CreateLink.Field()
