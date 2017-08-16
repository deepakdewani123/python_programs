import json
from collections import OrderedDict

# data = {}
# data['verses'] = []

values = []
number = 1

for i in range(0, 77):
    values.append(OrderedDict([
        ("name", "%d" % (i+1)),
        ("text", ""),
        ("synonyms", ""),
        ("translation", ""),
        ("purport", "")
    ]))


f = open('data.txt', 'w')
f.write(json.dumps(values, sort_keys=False))


    # values.append({
    #     'name': '',
    #     'text': '',
    #     'synonyms': '',
    #     'translation' : '',
    #     'purport': ''
    # })


# print(values)
# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)


#   data['verses'].append({
#     "name": "",
#     "text": "",
#     "synonyms": "",
#     "translation": "",
#     "purport": ""
#     })
