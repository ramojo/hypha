from django.core.exceptions import PermissionDenied

from .models.project import CONTRACTING


def has_permission(action, user, object=None, raise_exception=True):
    value, reason = permissions_map[action](user, object)

    # :todo: cache the permissions based on key action:user_id:object:id
    if raise_exception and not value:
        raise PermissionDenied(reason)

    return value, reason


def can_approve_contract(user, project):
    if project.status != CONTRACTING:
        return False, 'Project is not in Contracting State'

    if not user.is_authenticated:
        return False, 'Login Required'

    if user.is_apply_staff:
        return True, 'Staff can approve the contract'

    return False, 'Forbidden Error'


def can_upload_contract(user, project):
    if project.status != CONTRACTING:
        return False, 'Project is not in Contracting State'

    if not user.is_authenticated:
        return False, 'Login Required'

    if user.is_apply_staff or user.is_contracting or user == project.user:
        return True, 'Staff and Project owner can upload the contract'

    return False, 'Forbidden Error'


permissions_map = {
    'contract_approve': can_approve_contract,
    'contract_upload': can_upload_contract,
}