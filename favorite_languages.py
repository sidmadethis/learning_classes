from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+ language.title())


# the OrderedDict keeps the order of key value pairs.  the call to OrderedDict() creates an empty ordered dictionary and stores it in favorite_languages

# when we run this it keeps the order in which we entered the keys/values.  this is part of the standard library
