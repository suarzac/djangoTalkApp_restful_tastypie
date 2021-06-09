from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization

from Talk.models import Talk


class TalkResource(ModelResource):
    class Meta:
        queryset = Talk.objects.all()
        resource_name = 'talk'
        authorization = Authorization()
        filtering = {'name': ALL}
