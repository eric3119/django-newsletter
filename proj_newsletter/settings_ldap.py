import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

MAIN_DN     = 'dc=example,dc=com'
GROUPS_DN   = 'ou=Groups,'+MAIN_DN
USERS_DN    = 'ou=Users,'+MAIN_DN

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://localhost:10389"
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,"+USERS_DN

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name":"cn",
    "last_name":"sn",
    "email": "mail",    
}

AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(GROUPS_DN, ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)")

AUTH_LDAP_USER_FLAGS_BY_GROUP = { 
   "is_active":    "cn=enabled,"+GROUPS_DN,
   "is_staff":     "cn=admin,"+GROUPS_DN,
   "is_superuser": "cn=dev,"+GROUPS_DN,
}

import logging
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)