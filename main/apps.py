from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_save

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save
        import main.signals 
        def add_to_default_group(sender,**Kwargs):
            user=Kwargs['instance']
            if Kwargs['created']:
                group, ok=Group.objects.get_or_create(name='default')
                group.user_set.add(user)
        post_save.connect(add_to_default_group,sender=settings.AUTH_USER_MODEL)

   
       