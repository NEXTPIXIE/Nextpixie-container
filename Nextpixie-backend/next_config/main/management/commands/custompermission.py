from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Helps Automatically create a user group and add permissions to it'

    def handle(self, *args, **options):
        user = Group.objects.create(name='User')
        group = Group.objects.get(name=user)
        permission_codenames = ['can_create_album', 'can_view_album', 'can_publish_album']

        for codename in permission_codenames:
            permission = Permission.objects.get(codename=codename)
            group.permissions.add(permission)




        self.stdout.write('Group and permissions created')


