""" Creating and Combining Sets of Friends """

college = set(['Bill', 'Katy', 'Verne', 'Dillon',
               'Bruce', 'Olivia', 'Richard', 'Jim'])

coworker = set(['Aaron', 'Bill', 'Brandon', 'David',
                'Frank', 'Connie', 'Kyle', 'Olivia'])

family = set(['Garry', 'Landon', 'Larry', 'Mark',
              'Olivia', 'Katy', 'Rae', 'Tom'])

# combine all friends into a single set
friends = college.union(coworker, family)

# print out friends in each set
print('I have {} college buddies:'.format(len(college)))
print(college)

print('I have {} coworkers:'.format(len(coworker)))
print(coworker)

print('I have {} family friends:'.format(len(family)))
print(family)

print('I have {} total friends:'.format(len(friends)))
print(friends)


""" Sorting Friends into Sets """

# set of all friends
friends = set(['Mark', 'Rae', 'Verne', 'Richard',
               'Aaron', 'David', 'Bruce', 'Garry',
               'Bill', 'Connie', 'Larry', 'Jim',
               'Landon', 'Dillon', 'Frank', 'Tom',
               'Kyle', 'Katy', 'Olivia', 'Brandon'])

# set of people who live in my zip code
zipcode = set(['Jerry', 'Elaine', 'Cindy', 'Verne',
               'Rudolph', 'Bill', 'Olivia', 'Jim',
               'Lindsay', 'Rae', 'Mark', 'Kramer',
               'Landon', 'Newman', 'George'])

# set of people who play Munchkin
munchkins = set(['Steve', 'Jackson', 'Frank', 'Bill',
                 'Mark', 'Landon', 'Rae'])

# set of Olivia's friends
olivia = set(['Jim', 'Amanda', 'Verne', 'Nestor'])


# choose the friends who live near by
local = friends.intersection(zipcode)
print('I have {} local friends:'.format(len(local)))
print(local)

# remove munchkin players
invite = local.difference(munchkins)
print('I have {} friends to invite:'.format(len(invite)))
print(invite)

# revise the friends to invite set
invite = invite.symmetric_difference(olivia)
print(invite)
