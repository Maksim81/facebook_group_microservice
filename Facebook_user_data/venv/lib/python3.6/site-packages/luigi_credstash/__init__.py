from __future__ import print_function
from luigi import configuration
from credstash_cache import get_secret
import logging


logger = logging.getLogger(__file__)


def get_credentials_from_config(config,
                                table_key='credstash_table',
                                username_key='credstash_user_key',
                                password_key='credstash_password_key'):
    credstash_table = configuration.get_config().get(config, table_key, None)
    user_key = configuration.get_config().get(config, username_key, None)
    pass_key = configuration.get_config().get(config, password_key, None)

    try:
        user = get_secret(user_key, credstash_table)
        password = get_secret(pass_key, credstash_table)
    except:
        logger.error("ERROR Loading credentials from config: '{0}' table: '{1}' user key: '{2}' pass key: '{3}'".format(
            config,
            credstash_table,
            user_key,
            pass_key
        ))

    return {'user': user, 'password': password}


class CredentialMixin(object):

    config_key = None
    _user = None
    _password = None

    def _load_credentials(self):
        creds = get_credentials_from_config(self.config_key)
        self._user = creds['user']
        self._password = creds['password']

    @property
    def user(self):
        if not self._user:
            self._load_credentials()
        return self._user

    @property
    def password(self):
        if not self._password:
            self._load_credentials()
        return self._password