import numpy as np
import h5py

values = np.random.random(size = (400, 400))
rates  = np.random.random(size = (300, 300))
thorin = np.random.random(size = (200, 200))
gus    = np.random.random(size = (100, 100))

#TIME TO WRITE!

with h5py.File('test.h5', 'w') as hdf:
    #to store home value data inside a dataset called "dollas"
    #inside "home" group and "values" subgroup
    # 1st "random" is the random-related package, 2nd "random" is function call
   
    print('creating group1 (Home group with Value subgroup)')
    group1 = hdf.create_group('home/value')
    group1.create_dataset('dolla dolla bills', data=values)

    #to store mortgage rates inside dataset called "rates"
    #inside home group and mortgage subgroup

    print('creating group2 (Home group with Mortgage (Rates) subgroup)')
    group2 = hdf.create_group('home/mortgage')
    group2.create_dataset('rates', data=rates)

    #because those bastards are cute
    print('creating group3 (Boogers group)')
    group3 = hdf.create_group('boogers')
    group3.create_dataset('dogs', data=thorin)
    group3.create_dataset('cat', data=gus)

    #DESC descrition attribute
    group1.attrs['DESC'] = 'Home values in the last year'
    group2.attrs['DESC'] = 'Home morgage rates in the last year'
    group3.attrs['DESC'] = 'Home photos of the resident fuzz'

    print('Finished creating test.h5 file')


#TIME TO READ!
with h5py.File('test.h5', 'r') as hdf:
    # Listing all the base items in the hdf file. These are going to be the
    # root groups that were defined before.
    # NOTE: remember list(hdf.items()) is called 'casting'. This is converting
    #       a list of some kind into a python list.
    base_items = list(hdf.items())
    print(f'The items in base HDF5 directory ("boogers", "home")\n{base_items}\n')

    home = hdf.get('home')
    home_items = list(home.items())
    print(f'Items in the /home directory ("value", "mortgage")\n{home_items}\n')

    boogers = hdf.get('boogers')
    boogers_items = list(boogers.items())
    print(f'Items in the /boogers directory ("gus", "thorin")\n{boogers_items}\n')

    mortgage = hdf.get('home/mortgage')
    mortgage_items = list(mortgage.items())
    print(f'The items in the home/mortgage subgroup ("rates")\n{mortgage_items}\n')

    values = home.get('values')
    rates = hdf.get('home/mortgage/rates')
    thorin = boogers.get('thorin')
    gus = hdf.get('boogers/gus')
