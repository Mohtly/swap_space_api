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

class CreateItem(graphene.Mutation):
    # item_id = graphene.Int()
    photo = graphene.String()
    value_low = graphene.Int()
    value_high = graphene.Int()
    user_id = graphene.Int()
    description = graphene.Int()
    traded = graphene.Boolean()
    # date_time_created = graphene.types.datetime.DateTime()


    #2
    class Arguments:
        photo = graphene.String()
        value_low = graphene.Int()
        value_high = graphene.Int()
        user_id = graphene.Int()
        description = graphene.String()
        traded = graphene.Boolean()
        # date_time_created = graphene.types.datetime.DateTime()

    #3
    def mutate(self, info, photo, value_low, value_high, user_id, description, traded):
        item = Item(photo=photo, value_low=value_low, value_high=value_high, user_id=user_id, description=description,
                    traded=traded)
        item.save()

        return CreateItem(
            item_id=item.item_id,
            photo=item.photo,
            value_low=item.value_low,
            value_high=item.value_high,
            user_id=user_id,
            description=item.description,
            traded=item.traded,
            # date_time_created=item.date_time_created
        )


#4
class Mutation(graphene.ObjectType):
    create_item = CreateItem.Field()
