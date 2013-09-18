weird_thing = {'stuff':[[3,5,4], {'abc':'def'}]}
weird_thing['other_stuff'] = 'green'
weird_thing['numbers'] = range(100)
print(weird_thing)
json.dump(weird_thing, open('weird_thing.json', 'w'))


# On another computer
print json.load(open('weird_thing.json', 'r'))
