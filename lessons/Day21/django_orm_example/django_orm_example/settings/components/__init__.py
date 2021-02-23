# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from os.path import join, isfile, dirname
from fnmatch import fnmatch
import os

# Build paths inside the project like this: join(BASE_DIR, ...)
BASE_DIR = dirname(dirname(dirname(dirname(__file__))))


class GlobalIPList(list):
    """
    Extra class to access development server from any IP inside the network
    """
    def __contains__(self, key):
        if any([fnmatch(key, elt) for elt in self]):
            return True
        return False


class DevelopmentConfiguration(object):
    """
    This class reads the text file formatted as KEY=VALUE
    with possible line comments starting with #
    to a dictionary. This class is used to speed up the development process.
    """
    def __init__(self, base='', *path_parts):
        """
        Reads the file and prepares config.
        :param path_parts: Path to the configuration file,
         ensure that this file is excluded from VCS.
        """
        self._config = {}
        self.path = join(base, *path_parts)

        if not isfile(self.path):
            raise ImproperlyConfigured('Not a file')

        with open(self.path, 'r') as secret_file:
            content = secret_file.read()

        for line in content.splitlines():
            if line and not line.startswith('#'):
                line_parts = line.split('=', 1)
                self._config[line_parts[0]] = line_parts[1]

    def __getitem__(self, item):
        """
        This function is used to get a specific settings' value.
        Values defined in the secret file overrides values
        defined in the environment.
        :param item: Key to get the needed value.
        :return: Value from secret file if present or value from
            the environment. It will rise an exception if value is not found.
        """
        return self._config.get(item, '') or os.environ.get(item, '')

CONFIG = DevelopmentConfiguration(BASE_DIR, 'config', 'secret.cfg')
