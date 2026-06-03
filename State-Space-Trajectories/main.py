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
# plt.show()

#===========================================
# ALM_PSTH_nonpreferred_cue_timeseries.png

#plt.plot(TIME, NOT_PREFERENCE.T)
#plt.show()

#===========================================
# ALM_PSTH_preferred_cue_timeseries.png

#plt.plot(TIME, PREFERENCE.T)
#plt.show()

#===========================================
# print('Channel Quality Filtering:')

# print('Not Preference:')
# print(NOT_PREFERENCE.shape)
# NOT_PREFERENCE = NOT_PREFERENCE[np.isfinite(NOT_PREFERENCE[:,0]),:]
# print(NOT_PREFERENCE.shape)

# print('Preference:')
# print(PREFERENCE.shape)
# PREFERENCE = PREFERENCE[np.isfinite(PREFERENCE[:,0]),:]
# print(PREFERENCE.shape)

#===========================================
#Channel Index Map
# plt.plot(CHANNEL_INDEX, 'o')
# plt.show()

#===========================================
# Channel Quality Filtering 2

mask_not = np.isfinite(NOT_PREFERENCE[:, 0])
NOT_PREFERENCE = NOT_PREFERENCE[mask_not, :]
CHANNEL_INDEX_NOT = CHANNEL_INDEX[mask_not]

mask_pref = np.isfinite(PREFERENCE[:, 0])
PREFERENCE = PREFERENCE[mask_pref, :]
CHANNEL_INDEX_PREF = CHANNEL_INDEX[mask_pref]

# fig, ax = plt.subplots(1, 2, figsize=(10, 6))

# ax[0].imshow(NOT_PREFERENCE, extent=[TIME[0], TIME[-1], 0, NOT_PREFERENCE.shape[0]], vmin=0, vmax=10, origin='upper')
# ax[0].set_aspect(1/ax[0].get_data_ratio())
# ax[0].set_xlabel('Time (s)')
# ax[0].set_ylabel('Trial/Channels')
# ax[0].set_title('Non-preferred')

# ax[1].imshow(PREFERENCE, extent=[TIME[0], TIME[-1], 0, PREFERENCE.shape[0]], vmin=0, vmax=10, origin='upper')
# ax[1].set_aspect(1/ax[1].get_data_ratio())
# ax[1].set_xlabel('Time (s)')
# ax[1].set_ylabel('Trial/Channels')
# ax[1].set_title('Preferred')
# plt.show()

# Compute and Plot Population‑Average PSTHs
plt.plot(TIME, np.mean(NOT_PREFERENCE, axis=0), label='Non Preference')
plt.plot(TIME, np.mean(PREFERENCE, axis=0), label='Preference')
plt.show()