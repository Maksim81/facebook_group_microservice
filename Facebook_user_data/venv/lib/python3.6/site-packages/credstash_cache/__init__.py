from __future__ import print_function
import credstash
import hashlib
import logging


logger = logging.getLogger(__file__)


__local_stash__ = {}


def _hash_it(key, table, region):
    h = hashlib.new('ripemd160')
    h.update(key.encode('utf-8'))
    h.update(table.encode('utf-8'))
    h.update(region.encode('utf-8'))
    return h.hexdigest()


def _check_local(key, table, region):
    hashed_key = _hash_it(key, table, region)
    secret = None

    if hashed_key in __local_stash__:
        secret = __local_stash__[hashed_key]
        logger.debug('Successfully loaded secret %s from memory' % key)
    else:
        logger.debug('Could not read secret %s from local memory' % key)
    return secret


def _put_local(secret, key, table, region):
    hashed_key = _hash_it(key, table, region)

    try:
        __local_stash__[hashed_key] = secret
        logger.debug('Successfully wrote secret %s to local memory' % key)
    except Exception:
        logger.debug('Could not write secret %s to local memory' % key)


def get_secret(key, table=None, region='us-east-1'):
    if table is None:
        table = 'credential-store'

    secret = _check_local(key, table, region)
    if not secret:
        secret = credstash.getSecret(key, table=table, region=region)
        _put_local(secret, key, table, region)
    return secret
