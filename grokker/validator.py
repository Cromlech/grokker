# -*- coding: utf-8 -*-


class GrokkerValidationError(Exception):
    pass


def str_validator(directive_name, value):
    if not isinstance(value, str):
        raise GrokkerValidationError(
            "The '%s' directive can only be called with a "
            "unicode or str argument." % directive_name)


def int_validator(directive_name, value):
    if not isinstance(value, int):
        raise GrokkerValidationError(
            "The '%s' directive can only be called with a "
            "integer argument." % directive_name)


def isclass(value):
    """We cannot use ``inspect.isclass`` because it will return True
    for interfaces (zope.interface)"""
    return isinstance(value, type)


def class_validator(directive_name, value):
    if not isclass(value):
        raise GrokkerValidationError(
            "The '%s' directive can only be called with a "
            "class argument." % (directive_name))
