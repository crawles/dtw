import librosa
from dtw import dtw
import IPython.display
import numpy as np

import matplotlib.pyplot as plt
%matplotlib inline


y1, sr1 = librosa.load('/Users/chris/Documents/audio_samples/elias_warping_cut.m4a')
y2, sr2 = librosa.load('/Users/chris/Documents/audio_samples/elias_leader_cut.m4a')
y3, sr3 = librosa.load('/Users/chris/Documents/audio_samples/chris_warping_cut.m4a')
y4, sr4 = librosa.load('/Users/chris/Documents/audio_samples/chris_follow_cut.m4a')
yX, srX = librosa.load('/Users/chris/Documents/audio_samples/full_sentence5.m4a')

#plt.close()
#plt.plot(y1,'b-')
#plt.plot(y2,'r-')
## remove mean


#n = 5
#subplot(1, n, 1)
#mfcc1 = librosa.feature.mfcc(y1, sr1)
#mfcc1 = mfcc1/np.max(mfcc1)
#librosa.display.specshow(mfcc1)
#
#subplot(1, n, 2)
#mfcc2 = librosa.feature.mfcc(y2, sr2)
#mfcc2 = mfcc2/np.max(mfcc2)
#librosa.display.specshow(mfcc2)
#
#subplot(1, n, 3)
#mfcc3 = librosa.feature.mfcc(y3, sr3)
#mfcc3 = mfcc3/np.max(mfcc3)
#librosa.display.specshow(mfcc3)
#
#subplot(1, n, 4)
#mfcc4 = librosa.feature.mfcc(y4, sr4)
#mfcc4 = mfcc4/np.max(mfcc4)
#librosa.display.specshow(mfcc4)
#
#subplot(1, n, 5)
#mfccX = librosa.feature.mfcc(yX, srX)
##mfccX = mfccX/np.max(mfccX)
#librosa.display.specshow(mfccX)
#
#
#from dtw import dtw
#
#
#dist12, cost12, path12 = dtw(mfcc1.T, mfcc2.T)
#dist13, cost13, path13 = dtw(mfcc1.T, mfcc3.T)
#dist14, cost14, path14 = dtw(mfcc1.T, mfcc4.T)
#dist24, cost24, path24 = dtw(mfcc2.T, mfcc4.T)
#dist23, cost23, path23 = dtw(mfcc2.T, mfcc3.T)
#dist34, cost34, path34 = dtw(mfcc3.T, mfcc4.T)
#print 'Normalized distance between the two sounds:', dist
#
#def show_image(dist,cost,path):
#    imshow(cost.T, origin='lower', cmap=cm.gray, interpolation='nearest')
#    plot(path[0], path[1], 'w')
#    xlim((-0.5, cost.shape[0]-0.5))
#    ylim((-0.5, cost.shape[1]-0.5))
#
#show_image(dist12, cost12, path12)
#show_image(dist13, cost13, path13)
#show_image(dist14, cost14, path14)
#show_image(dist23, cost23, path23)
#show_image(dist34, cost34, path34)


mfcc1 = librosa.feature.mfcc(y1, sr1)
mfcc1 = mfcc1/np.max(mfcc1)

mfcc3 = librosa.feature.mfcc(y3, sr3)
mfcc3 = mfcc3/np.max(mfcc3)


mfccX = librosa.feature.mfcc(yX, srX)
#mfccX = mfccX/np.max(mfccX)


#dists3i = np.zeros(mfccX.shape[1] - mfcc3.shape[1] + speed)
#dists3i = np.zeros(mfccX.shape[1] + mfcc3.shape[1] + speed) + 1.25

speed = 0
dists3i = np.zeros(mfccX.shape[1]) + 1.5
window_size = (mfcc1.shape[1]+speed)
for i in range(mfccX.shape[1] - window_size):

    mfcci = mfccX[:,i:i+window_size]
    mfcci = mfcci/np.max(mfcci)

    dist3i, cost3i, path3i = dtw(mfcc1.T, mfcci.T)
    dists3i[i] = dist3i

plt.plot(dists3i)

# 
#n_fft=2048
#hop_length=512
#

word_match_idx = dists3i.argmin()
word_match_idx_bnds = np.array([word_match_idx,np.ceil(word_match_idx+window_size)])
samples_per_mfcc = 512#len(yX)/mfccX.shape[1]
word_samp_bounds = (2/2) + (word_match_idx_bnds*samples_per_mfcc)

word = yX[word_samp_bounds[0]:word_samp_bounds[1]]
print [word_samp_bounds[1], word_samp_bounds[0]]

plt.plot(word)


IPython.display.Audio(data=word, rate=sr1)
#IPython.display.Audio(data=y1, rate=sr1)


