'''
Python script to conduct modelling of photon
interaction in connective tissues
'''

# run external scripts
import matlab.engine as mateng
import pandas as pd
import os

# data manipulation and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


path_data = './src_data'
os.chdir(path_data)

wave = pd.read_csv('wave2.csv')
eng = mateng.start_matlab()

for i in range(len(wave)):
    tissueName = 'csc_test_tissue_'+str(wave['nm'][i])
    print(tissueName)
    st = eng.tissuestruct(float(wave['nm'][i]), tissueName, nargout=1)
    if st == 1:
        print('Tissue structure successfully created!')
    else:
        print('Possible error, check code in MATLAB!')
eng.quit()


'''
- import one of the created tissue structure binary files reshape and visualize
'''
data = np.fromfile(tissueName+'_T.bin', dtype=np.ubyte)
print(type(data), ', data shape: ', data.shape)

nbins = 200
tissue_vox = data.reshape(nbins, nbins, nbins)
print('Shape after reshaping: ', tissue_vox.shape)

tissue2d = tissue_vox[:,:,1]
print(tissue2d.shape)

# matplotlib
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(tissue2d, cmap='jet')
plt.show()



