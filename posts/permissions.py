from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView



def test_get_all_permissions_user(self):
    permissions = Permission.objects.filter (content_type__app_label='auth',
                                             codename__in=[
                                                 'add_user', 'change_user',
                                                 'add_group', 'change_group'
                                             ])
    user = User.objects.create_user (username='testuser', password='test123.')
    group = Group.objects.create (name='group')
    user.user_permissions.add (*permissions)

    backend = PermissionsBackend ()

    self.assertEqual (
        set (permissions.filter (content_type__model='group').values_list ('codename', flat=True)),
        set (backend.get_all_permissions (user, group))
    )
    self.assertEqual (
        set (permissions.filter (content_type__model='user').values_list ('codename', flat=True)),
        set (backend.get_all_permissions (user, user))
    )









