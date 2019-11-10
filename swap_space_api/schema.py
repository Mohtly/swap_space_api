import graphene

import users.schema, items.schema


class Query(items.schema.Query, users.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
