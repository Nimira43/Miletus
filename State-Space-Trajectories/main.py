import numpy as np
import matplotlib.pyplot as plt

from scipy.io import loadmat

matdat = loadmat('./data/ALMdata.mat')
#print(matdat)

NOT_PREFERENCE = matdat['PSTH_nonprefer_cue_aligned']
PREFERENCE = matdat['PSTH_prefer_cue_aligned']
TIME = matdat['t'][0]
CHANNEL_INDEX = matdat['Channel_all']

print('===============================')
print(NOT_PREFERENCE.shape), print(' ')
print(PREFERENCE.shape), print(' ')
print(TIME.shape), print(' ')
CHANNEL_INDEX = CHANNEL_INDEX.flatten()
print(CHANNEL_INDEX.shape), print(' ')

#============================================================
# First Heatmaps image

# fig, ax = plt.subplots(1, 2, figsize=(10, 6))
# ax[0].imshow(NOT_PREFERENCE, extent=[TIME[0], TIME[-1], 0, NOT_PREFERENCE.shape[0]], origin='upper')
# ax[0].set_aspect(1/ax[0].get_data_ratio())
# ax[0].set_xlabel('Time (s)')
# ax[0].set_ylabel('Trial/Channels')
# ax[0].set_title('Non-preferred')
# ax[1].imshow(PREFERENCE, extent=[TIME[0], TIME[-1], 0, PREFERENCE.shape[0]], origin='upper')
# ax[1].set_aspect(1/ax[1].get_data_ratio())
# ax[1].set_xlabel('Time (s)')
# ax[1].set_ylabel('Trial/Channels')
# ax[1].set_title('Preferred')
#plt.show()

#===========================================
# ALM_PSTH_nonpreferred_cue_timeseries.png

#plt.plot(TIME, NOT_PREFERENCE.T)
#plt.show()

#===========================================
# ALM_PSTH_preferred_cue_timeseries.png

#plt.plot(TIME, PREFERENCE.T)
#plt.show()

#===========================================
print('Channel Quality Filtering:')
NOT_PREFERENCE = NOT_PREFERENCE[np.isfinite(NOT_PREFERENCE[:,0]),:]
print(NOT_PREFERENCE.shape)