from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.contrib.auth.models import Permission, Group

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
  roles = [
    [
      "Super Admin",
      Permission.objects.all()
    ],
    [
      "Admin",
      Permission.objects.filter(
        codename__in=[
          # INFO: user information
          "add_user",
          "change_user",
          "view_user",
        ]
      )
    ], [
      "Student",
      Permission.objects.filter(
        codename__in=[
          "change_user",
          "view_user"
        ]
      )
    ]
  ]

  for gp in roles:
    mg = Group.objects.get_or_create(name=gp[0])
    mg[0].permissions.set(gp[1])


def add_user_to_default_group(sender, instance, created, **kwargs):
  if created:
    group = Group.objects.get(name="Student")
    instance.groups.add(group)