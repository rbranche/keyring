"""
Compatibility support for Python 2.7. Remove when Python 2.7 support is
no longer required.
"""
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
