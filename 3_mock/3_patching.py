import urllib

import mock


# this is the function we are going to be patching
def uses_quote_plus(url):
    print 'uses_quote_plus'
    return urllib.quote_plus(url)

# use the function as normal
print 'no patching'
print uses_quote_plus('http://www.brett.is/')

# patch the urllib module
with mock.patch('urllib.quote_plus', mock.Mock(return_value='http://pythonbuffalo.org/')):
    print 'using patched quote_plus'
    print uses_quote_plus('http://www.brett.is/')

# exact same as the last one
with mock.patch('urllib.quote_plus') as mocked_quote_plus:
    mocked_quote_plus.return_value = 'http://www.github.com/'
    print 'using patched quote_plus'
    print uses_quote_plus('http://www.brett.is/')


print 'patching a dict'
data = {}
with mock.patch.dict(data, {'some': 'values'}):
    assert 'some' in data
    assert data['some'] == 'values'

# no longer patched, should be the {}
assert 'some' not in data


# use patch as a decorator to a function
@mock.patch('__main__.uses_quote_plus', mock.Mock(return_value='http://www.github.com'))
def test(url):
    print 'using patched version of uses_quote_plus'
    return uses_quote_plus(url)

print test('http://www.brett.is/')
