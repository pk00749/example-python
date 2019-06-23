import yaml

class Monster(yaml.YAMLObject):
  yaml_tag = u'!Monster'

  def __init__(self, name, hp, ac, attacks):
    self.name = name
    self.hp = hp
    self.ac = ac
    self.attacks = attacks

  def __repr__(self):
    return "%s(name=%r, hp=%r, ac=%r, attacks=%r)" % (
       self.__class__.__name__, self.name, self.hp, self.ac,
       self.attacks)

y=yaml.load("""
--- !Monster
name: Cave spider
hp: [2,6]    # 2d6
ac: 16
attacks: [BITE, HURT]
# """)
print(y)

print("------------------------")
print(yaml.dump(Monster(
    name='Cave lizard', hp=[3,7], ac=27, attacks=['BITE','HURT', 'RUN'])))

print("------------------------")

class People(yaml.YAMLObject):
    yaml_tag = u'!People'

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "{}(name:{},age:{})".format(self.__class__.__name__, self.name, self.age)


f = yaml.load_all("""
--- !People
name: James
age: 20
--- 
name: Lily
age: 19
""")

print([data for data in f])


ff = '''
---
name: James
age: 20
---
name: Lily
age: 19
'''
y = yaml.load_all(ff)
print([data for data in y])
print("------------------------")

aproject = {'name': 'Silenthand Olleander',
            'race': 'Human',
            'traits': ['ONE_HAND', 'ONE_EYE']
            }

print(yaml.dump(aproject))