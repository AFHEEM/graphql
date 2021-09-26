import graphene
from graphene_django import DjangoObjectType

from .models import DcaIntegratedDataset, DcaIntegratedDataElement


# Step 1 - Attach model to a django object type
class IDSType(DjangoObjectType):
    class Meta:
        model = DcaIntegratedDataset
        fields = "__all__"


class IDEType(DjangoObjectType):
    class Meta:
        model = DcaIntegratedDataElement
        fields = "__all__"


# Step 2 - define a query with variables
class Query(graphene.ObjectType):
    # Step 2.1 - Add a parameter in query variable if needed
    all_ids = graphene.List(IDSType)
    get_ids = graphene.Field(IDSType, id=graphene.Int())

    all_ide = graphene.List(IDEType, id=graphene.Int())

    # Step 2.2 - use the parameter if needed for e.g. id
    def resolve_all_ids(self, info):
        return DcaIntegratedDataset.objects.all()

    def resolve_get_ids(self, info, id):
        return DcaIntegratedDataset.objects.get(integrated_dataset_id=id)

    def resolve_all_ide(self, info, id):
        return DcaIntegratedDataElement.objects.all()


class IDSCreateMutation(graphene.Mutation):
    class Arguments:
        ids_name = graphene.String(required=True)
        ids_version = graphene.Int(required=True)
        data_emp_nm = graphene.String(required=True)

    ids = graphene.Field(IDSType)

    @classmethod
    def mutate(cls, root, info, ids_name, ids_version, data_emp_nm):
        ids = DcaIntegratedDataset(integrated_dataset_name=ids_name,
                                   integrated_dataset_version=ids_version,
                                   data_user_employee_name=data_emp_nm)
        ids.save()
        return IDSCreateMutation(ids=ids)


class IDSUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        ids_name = graphene.String(required=True)
        ids_version = graphene.Int()
        data_emp_nm = graphene.String()

    ids = graphene.Field(IDSType)

    @classmethod
    def mutate(cls, root, info, id, ids_name, ids_version=1, data_emp_nm=None):
        ids = DcaIntegratedDataset.objects.get(pk=id)
        ids.integrated_dataset_name = ids_name
        ids.integrated_dataset_version = ids_version
        if data_emp_nm is not None:
            ids.data_user_employee_name = data_emp_nm
        ids.save()
        return IDSUpdateMutation(ids=ids)


class IDSDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    ids = graphene.Field(IDSType)

    @classmethod
    def mutate(cls, root, info, id):
        ids = DcaIntegratedDataset.objects.get(pk=id)
        ids.delete()
        return IDSDeleteMutation(ids=ids)


class Mutation(graphene.ObjectType):
    create_ids = IDSCreateMutation.Field()
    update_ids = IDSUpdateMutation.Field()
    delete_ids = IDSDeleteMutation.Field()


# Step 3 - add schema for query
schema = graphene.Schema(query=Query, mutation=Mutation)
