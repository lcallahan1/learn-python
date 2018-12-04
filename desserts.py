import numpy as np
import h5py as h5
import sys


#cookies = np.random.random(size = 27)
#pies = np.random.random(size = 5)


#with h5.File('desserts.h5', 'w') as hdf:
    #hdf.create_dataset('cookies', data=cookies)
    #hdf.create_dataset('pies', data=pies)

with h5.File('desserts.h5', 'r') as hdf:

    if len(sys.argv) > 1:
        """            
        #because 0 is name of script
        if sys.argv[1] == "cookies":
            cookies = hdf.get('cookies')
            c = np.array(cookies) * 10
            print(c)
        elif sys.argv[1] == "pies":
            pies = hdf.get('pies')
            p = np.array(pies) * 10
            print(p)
        else: print('Dataset not found')
        """

        for dataset in sys.argv[1:]: #from first index to the end of array
            data=hdf.get(dataset)
            print(data)
    else:
        print('No dataset given')
