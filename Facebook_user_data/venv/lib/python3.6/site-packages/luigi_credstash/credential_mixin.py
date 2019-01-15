from luigi_credstash import get_credentials_from_config


class CredentialMixin(object):

    config_key = None
    _user = None
    _password = None

    def _load_credentials(self):
        credentials = get_credentials_from_config(self.config_key)
        self._user = credentials['user']
        self._password = credentials['password']

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
