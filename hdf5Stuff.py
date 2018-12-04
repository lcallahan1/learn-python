# Import the numpy library. Saying "as np" means we can reference this library
# as `np` instead of `numpy`
import numpy as np
import h5py

# TODO: Talk about tuples
# NOTE: Something new! When you see something in python like (400, 400) in
# the example below, it is called a 'tuple'. It's basically a small array that
# cannot have any of its values changed (immutable).
# https://www.tutorialspoint.com/python/python_tuples.htm
#
# There are 2 ways you will see these used. One way is as a variable or
# parameter. You will see variables assigned like a = (1, 2). You can also
# address the values by using a[0] which would be 1.
#
# Another way you will see these in python, are when returned from a function
# call. You might see something like this:
# (data, err) = doSomething()
# What's happening in this scenario, is the doSomething method is returning
# a tuple. One of the values (data) will be the return value of the method.
# The other one (err) will be an error code. This way you can find out if
# something bad happened, without the program blowing up on some kind of
# exception being thrown.
values = np.random.random(size = (400, 400))
rates  = np.random.random(size = (300, 300))
thorin = np.random.random(size = (200, 200))
gus    = np.random.random(size = (100, 100))

with h5py.File('test.h5', 'w') as hdf:
    # Store home value data in a dataset called 'dollars'. This dataset will
    # live inside of the 'home' group and the 'value' subgroup
    print('Creating group1 (home/value)')
    group1 = hdf.create_group('home/value')
    group1.create_dataset('dollars', data=values)

    # Store mortgage rates in a dataset called 'rates'. This dataset will
    # live inside of the 'home' group and the 'mortgage' subgroup
    print('Creating group2 (home/mortgage)')
    group2 = hdf.create_group('home/mortgage')
    group2.create_dataset('rates', data=rates)


    # These last 2 datasets (thorin, and gus) contain a bunch of images of the
    # little buggers. They have nothing to do with data science, but could help
    # make your day a little better. Because of this, we'll store them in
    # another group called boogers, especially for them.
    print('Creating group3 (boogers)')
    group3 = hdf.create_group('boogers')
    group3.create_dataset('thorin', data=thorin)
    group3.create_dataset('gus', data=gus)

    # Add the DESC (description) attribute to the datasets to describe what
    # they do. You can embed this metadata to tell other people who use your
    # file what data is in the file, but it's far more likely, you'll be the
    # other person at some point in the future and won't remember what the hell
    # you were working on.
    group1.attrs['DESC'] = 'Home values in the last year'
    group2.attrs['DESC'] = 'Mortgage rates in the last year'
    group3.attrs['DESC'] = 'Pictures of the most ridiculous animals'

    print('Done creating test.h5')



print('\nBegin reading test.h5')
with h5py.File('test.h5', 'r') as hdf:
    # Listing all the base items in the hdf file. These are going to be the
    # root groups that were defined before.
    # NOTE: remember list(hdf.items()) is called 'casting'. This is converting
    #       a list of some kind into a python list.
    base_items = list(hdf.items())
    print(f'Items in base hdf5 directory ("boogers", "home"):\n{base_items}\n')

    # You can retrieve a group and then list all of the the subgroups that are
    # stored inside of it. This way you can sort of navigate what data is
    # stored in the hdf file
    home = hdf.get('home')
    home_items = list(home.items())
    print(f'Items in the /home directory ("value", "mortgage")\n{home_items}\n')

    # You can do the same with your subgroups. In this case, because we have a
    # couple of datasets in this subgroup, you'll see those data sets when we
    # print the list.
    mortgage = hdf.get('home/mortgage')
    mortgage_items = list(mortgage.items())
    print(f'Items in the home/mortgage subgroup ("rates")\n{mortgage_items}\n')


    values = hdf.get('home/value/dollars')
    # There are multiple ways to retrieve datasets. One way is to retrieve them
    # from the root hdf object (like above). Another way is to use a group that
    # you have already retrieved (with get) and retrieve the dataset inside it.
    rates  = mortgage.get('rates')
    thorin = hdf.get('boogers/thorin')
    gus    = hdf.get('boogers/gus')

    print(f'values shape: {values.shape}')
    print(f'rates  shape: {rates.shape}')
    print(f'thorin shape: {thorin.shape}')
    print(f'gus    shape: {gus.shape}')
