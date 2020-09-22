import array
import os


def unicode_symbol():
    symbols = '$%^&$#%'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    codes = [ord(symbol) for symbol in symbols]
    print(codes)


def local_variable():
    x = 'my precious'
    dummy = [x for x in 'ABC']
    print(x)
    print(dummy)


def map_filter():
    symbols = '$%^&$#%'
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 35]
    print(beyond_ascii)
    beyond_ascii = list(filter(lambda c: c > 35, map(ord, symbols)))
    print(beyond_ascii)


def cartesian_product():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    tshirts = [(color, size) for color in colors for size in sizes]
    print(tshirts)
    for color in colors:
        for size in sizes:
            print((color, size))
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)


def tuple_list():
    symbols = '$%^&$#%'
    print(tuple(ord(symbol) for symbol in symbols))
    print(array.array('I', (ord(symbol) for symbol in symbols)))


def tuple_record():
    lax_coordinate = (33.9425, -118.408056)
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
    traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
    for passport in sorted(traveler_ids):
        print('%s/%s' % passport)

    for country, _ in traveler_ids:
        print(country)

    latitude, longitude = lax_coordinate
    print(latitude)
    print(longitude)


def elegant_change():
    a = 1
    b = 2
    b, a = a, b
    print(a)
    print(b)


def divmod_number():
    print(divmod(20, 8))
    t = (20, 8)
    print(divmod(*t))
    quotient, remainder = divmod(*t)
    print(quotient)
    print(remainder)


def get_filename():
    _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
    print(filename)


def asterisk_function():
    a, b, *rest = range(5)
    print(a, b, rest)
    a, b, *rest = range(3)
    print(a, b, rest)
    a, b, *rest = range(2)
    print(a, b, rest)
    a, *body, c, d = range(5)
    print(a, body, c, d)
    *head, b, c, d = range(5)
    print(head, b, c, d)


def nesting_tuple():
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.43333, -99.13333)),
        ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
        ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'lang.'))
    fmt = '{:15} | {:9.4f} | {:9.4f}'
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude <= 0:
            print(fmt.format(name, latitude, longitude))


if __name__ == '__main__':
    unicode_symbol()
    local_variable()
    map_filter()
    cartesian_product()
    tuple_list()
    tuple_record()
    elegant_change()
    divmod_number()
    get_filename()
    asterisk_function()
    nesting_tuple()
