# -*- coding: utf-8 -*-

import venusian
from grokker import Directive, directive, grokker, validator
import pytest


def test_grokker_directive():
    from .fixtures import grokker_directive as module
    
    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(module)

    assert grokked == [
        ('SomeClass', module.SomeClass, 'the bar value')]


def test_mangled_name():
    from .fixtures import grokker_directive as module

    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(module)
    
    assert (getattr(module.SomeClass,
                    'grokker.tests.fixtures.grokker_directive.bar') ==
            'the bar value')


def test_list_storage():
    from .fixtures import list_storage as module

    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(module)

    assert grokked == [
        ('Alpha', module.Alpha, ['second bar', 'first bar']),
        ('Beta', module.Beta, ['second bar', 'first bar']),
        ('Delta', module.Delta, []),
        ('Gamma', module.Gamma, ['third bar', 'second bar', 'first bar']),
        ]


def test_directive_name_and_dotted_name():
    from .fixtures import grokker_directive as module

    assert module.bar.name == 'bar'
    assert (module.bar.dotted_name ==
            'grokker.tests.fixtures.grokker_directive.bar')


def test_validator():

    bar = Directive('bar', __name__, validator=validator.str_validator)

    @grokker
    @directive(bar)
    def foo(scanner, name, ob, bar):
        scanner.grokked.append((name, ob, bar))


    with pytest.raises(validator.GrokkerValidationError) as e:

        @foo
        @bar(5) # this will fail
        class SomeClass(object):
            pass

    assert str(e.value) == (
        "The 'grokker.tests.test_grokker.bar' "
        "directive can only be called with a unicode or str argument.")


def test_argsdirective():
    from .fixtures import argsdirective as module

    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(module)

    assert grokked == [
        ('SomeClass', module.SomeClass, ('one', 'two')),
    ]

# XXX try argsdirective with converter and validator
    
def test_default():
    from .fixtures import default as module
    
    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(module)

    assert grokked == [
        ('SomeClass', module.SomeClass, "default"),
        ]


def test_default_no_args_default():
    from .fixtures import no_args_default as module
    
    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    with pytest.raises(TypeError):
        scanner.scan(module)


def test_directive_converted_based_default():
    from .fixtures import converter_default as module

    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(module)

    a, b = grokked

    name, obj, bar = a
    assert bar == 'default'
    name, obj, bar = b
    assert bar == 'not default'


def test_converter():
    from .fixtures import converter as module

    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(module)

    grokked = sorted(grokked)

    a, b = grokked

    name, obj, bar = a
    assert bar == 6
    name, obj, bar = b
    assert bar == 6


def test_convert_based_default_depending_on_initialization():
    from .fixtures import default_depends_on_init as module

    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(module)

    a = grokked[0]

    name, obj, bar = a
    assert bar == "not initialized"

    module.initialize()

    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(module)

    a = grokked[0]

    name, obj, bar = a
    assert bar == "initialized"

    
# converter for default depending on a global being initialized
# during configuration time, import order issue


# XXX need a test for default policy on grokker too
# and interactions with default arg versus default policy
