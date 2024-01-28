from django.views.generic import TemplateView

class FriendView(TemplateView):
    template_name = "friends/friend.html"
    
class FriendlistView(TemplateView):
    template_name = "friends/friendlist.html"