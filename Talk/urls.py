from django.conf.urls import url, include
from tastypie.api import Api
from Talk.api import TalkResource

api = Api(api_name='v1')
api.register(TalkResource())

urlpatterns = [
    url(r'', include(api.urls)),
]