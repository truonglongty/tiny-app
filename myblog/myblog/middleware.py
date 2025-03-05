from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

class BlockedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.profile.is_blocked:
            if request.path.startswith(reverse('admin:index')):
                # Allow access to admin pages even if the user is blocked
                response = self.get_response(request)
                return response
            if request.path != reverse('login'):
                messages.error(request, 'Tài khoản của bạn đã bị khóa.')
                return redirect('login')
        response = self.get_response(request)
        return response