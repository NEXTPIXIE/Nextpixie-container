from django.contrib.auth.models import Group

group = Group.objects.create(name='my_group')
