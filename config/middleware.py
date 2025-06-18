from django.utils.deprecation import MiddlewareMixin
from account.models import BlockIpAdress

class GetUserIpMiddleware(MiddlewareMixin):

    def process_request(self, request):

        ip = request.META.get('REMOTE_ADDR')
        
        if request.user.is_authenticated:
            request.user.ips = []
            if ip not in request.user.ips:
                request.user.ips.append(ip)
                request.user.save()


class BlockUserIpMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        user = BlockIpAdress.objects.filter(ip_address = ip)
        if user:
            raise PermissionError