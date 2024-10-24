from .models import Profile, Notifications

class HasProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.user.has_created_profile = Profile.objects.filter(owner=request.user).exists()
        else:
            request.user.has_created_profile = False
        
        response = self.get_response(request)
        return response

class NotificationsMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if request.user.is_authenticated:
			request.user.notifications = Notifications.objects.filter(receiver=request.user).order_by('-created_at')
            
			request.user.has_unread_notifications = request.user.notifications.filter(is_read=False).exists()
                  
		response = self.get_response(request)
		return response
