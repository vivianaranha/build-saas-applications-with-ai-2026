def same_tenant(subject_tenant, resource_tenant, role="member"):
    return role == "platform_admin" or subject_tenant == resource_tenant

def can(role, action):
    matrix = {
        "viewer": {"read"},
        "member": {"read","create","update"},
        "admin": {"read","create","update","delete","manage"},
        "platform_admin": {"read","create","update","delete","manage","support"},
    }
    return action in matrix.get(role, set())
