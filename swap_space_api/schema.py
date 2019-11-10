import graphene

import items.schema


class Query(items.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
