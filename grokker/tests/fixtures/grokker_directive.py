from grokker import Directive, directive, grokker

bar = Directive('bar')

@grokker
@directive(bar)
def foo(scanner, name, ob, bar):
    scanner.grokked.append((name, ob, bar))
    
@foo
@bar("the bar value")
class SomeClass(object):
    pass

