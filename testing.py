import goslate

import urllib

gs= goslate.Goslate()
lang_id = gs.detect('hello , hi')

print(lang_id)
