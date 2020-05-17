def html_tag(tag):
    #print('<{0}>'.format(tag))
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))

    return wrap_text

h1=html_tag('mjk')
print(h1.__name__)
print(html_tag.__name__)
h1('klm')
print(h1)
print(html_tag)
h1('head2')
print(h1)
