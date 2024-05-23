from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.http.response import Http404

from ..models import MyUser

@receiver(post_save, sender=MyUser)
def add_user_to_group(sender, **kwargs):
    created = kwargs.get('created', False)
    user_model = kwargs.get('instance', None)

    try:
        group = get_object_or_404(Group, name="favorite_user")
    except Http404:
        group = Group.objects.create(
            name="favorite_user"
        )

    # Check if the instance is newly created
    if created:
        user_model.groups.add(group)
    else:
        pass