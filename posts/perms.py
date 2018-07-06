from permission.logics import AuthorPermissionLogic
from permission.logics import CollaboratorsPermissionLogic

PERMISSION_LOGICS = (
    ('News_App', AuthorPermissionLogic()),
    ('News_App', CollaboratorsPermissionLogic()),
)


