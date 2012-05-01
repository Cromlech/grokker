import venusian

def test_grokker_directive():
    from .fixtures import grokker_directive
    
    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(grokker_directive)

    assert grokked == [
        ('SomeClass', grokker_directive.SomeClass, 'the bar value')]
    
def test_list_storage():
    from .fixtures import list_storage

    grokked = []
    scanner = venusian.Scanner(grokked=grokked)
    scanner.scan(list_storage)
    assert grokked == [
        ('Alpha', list_storage.Alpha, ['second bar', 'first bar']),
        ('Beta', list_storage.Beta, ['second bar', 'first bar']),
        ('Gamma', list_storage.Gamma, ['third bar', 'second bar', 'first bar']),
        ]
    
