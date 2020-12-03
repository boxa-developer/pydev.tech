from django.http.response import HttpResponse
from django.conf import settings
import jwt

JWT_KEY = 'LPVakeE9hhgNdJfQO4owQD2RFFOzw5BU'


def jwt_decode(token):
    obj = jwt.decode(token, JWT_KEY, algorithms='HS256', verify=True)
    return obj


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.SAFE_URLS = settings.SAFE_URLS

    def __call__(self, request):
        print()
        # if request.path not in self.SAFE_URLS:
        #     try:
        #         jwt.decode(request.META["HTTP_TOKEN"], JWT_KEY, algorithms=['HS256'])
        #     except Exception:
        #         return HttpResponse(
        #             f' You should Login <a href={request.build_absolute_uri("/account/check")}> Login </a> ')

        response = self.get_response(request)

        return response
