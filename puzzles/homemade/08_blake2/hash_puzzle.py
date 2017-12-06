import csv

# read in the files
# real_words.txt store them off >>> ?

# hashes.txt

# salt.csv >>> account for semicolons
# maybe  use the split function


# keys.txt
# as we read, split by spaces


# personalizations:



# rw1, s1, k1, p1
# rw2, s1, k1, p1
#


# for word in words:
#     for salt in salts:
#         for key in keys:
#             for personalization in personalizations

import itertools
itertools.product(words, salts, keys, personalizations)


import hashlib
hsh = hashlib.blake2b(b'pythonrocks07', digest_size=10, key=b'guido', salt=b'pandas', person=b'bokeh')
hsh.hexdigest()
# '47dbf8bd8e4e860ee810'

# change one character - see completely different hexdigest:
hsh = hashlib.blake2b(b'Pythonrocks07', digest_size=10, key=b'guido', salt=b'pandas', person=b'bokeh')
hsh.hexdigest()
# '7c750f5a40f1bf0f2208'
