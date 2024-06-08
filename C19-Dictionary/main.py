########### Dictionary
capitals = {'USA':'DC',
            'Indo':'Jkt',
            'Jpn':'Tokyo',
            'Russia':'Moscow'}

capitals.update({'German':'Berlin'})
capitals.update({'Indo':'IKN'})
capitals.pop('Jpn')
# capitals.clear()

print(capitals['Indo'])
print(capitals['German'])
print(capitals.get('German'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)