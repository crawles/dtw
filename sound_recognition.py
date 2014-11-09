""" Just for testing .... """
import librosa
from dtw import dtw
import IPython.display
import numpy as np

import matplotlib.pyplot as plt
#%matplotlib inline


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
from matplotlib import pyplot as plt
def show_image(dist,cost,path):
    plt.imshow(cost.T, origin='lower', interpolation='nearest')
    plt.plot(path[0], path[1], 'w')
    plt.xlim((-0.5, cost.shape[0]-0.5))
    plt.ylim((-0.5, cost.shape[1]-0.5))



#### 
import copy
def preprocess_mfcc(mfcc):
    mfcc_cp = copy.deepcopy(mfcc)
    for i in xrange(mfcc.shape[1]):
        mfcc_cp[:,i] = mfcc[:,i] - np.mean(mfcc[:,i])
        mfcc_cp[:,i] = mfcc_cp[:,i]/np.max(np.abs(mfcc_cp[:,i]))
    return mfcc_cp

mfccX1 = preprocess_mfcc(mfccX)


####
####### ELIAS ########

#y1, sr1 = librosa.load('/Users/chris/Documents/audio_samples/elias_algorithm.m4a')
#yX, srX = librosa.load('/Users/chris/Documents/audio_samples/elias_algorithm_sentence.m4a')
y1, sr1 = librosa.load('/Users/chris/Documents/audio_samples/elias_mothers_milk_word.m4a')
y2, sr2 = librosa.load('/Users/chris/Documents/audio_samples/chris_mothers_milk_word.m4a')
y3, sr3 = librosa.load('/Users/chris/Documents/audio_samples/yaoquan_mothers_milk_word.m4a')
y4, sr4 = librosa.load('/Users/chris/Documents/audio_samples/chris_mothers_milk_word_slow.m4a')
yX, srX = librosa.load('/Users/chris/Documents/audio_samples/chris_mothers_milk_sentence_fast.m4a')

mfcc1 = librosa.feature.mfcc(y1, sr1)
mfcc2 = librosa.feature.mfcc(y2, sr2)
mfcc3 = librosa.feature.mfcc(y3, sr3)
mfcc4 = librosa.feature.mfcc(y4, sr4)
mfccX = librosa.feature.mfcc(yX, srX)

mfcc1 = preprocess_mfcc(mfcc1)
mfcc2 = preprocess_mfcc(mfcc2)
mfcc3 = preprocess_mfcc(mfcc3)
mfcc4 = preprocess_mfcc(mfcc4)
mfccX = preprocess_mfcc(mfccX)

######################

###My Voice###
#mfcc1 = librosa.feature.mfcc(y1, sr1)
#mfcc1 = mfcc1/np.max(mfcc1)
#
#mfcc3 = librosa.feature.mfcc(y3, sr3)
#mfcc3 = mfcc3/np.max(mfcc3)
#
#
#mfccX = librosa.feature.mfcc(yX, srX)
##mfccX = mfccX/np.max(mfccX)
##############


#dists3i = np.zeros(mfccX.shape[1] - mfcc3.shape[1] + speed)
#dists3i = np.zeros(mfccX.shape[1] + mfcc3.shape[1] + speed) + 1.25

speed = 0
dists = np.zeros(mfccX.shape[1]- window_size) + 1.5
window_size = (mfcc1.shape[1]+speed)
for i in range(mfccX.shape[1] - window_size - 1):

    mfcci = mfccX[:,i:i+window_size]
    #mfcci = mfcci/np.max(mfcci)

    dist3i, cost3i, path3i = dtw(mfcc1.T, mfcci.T)
    dist4i, cost4i, path4i = dtw(mfcc2.T, mfcci.T)
    dist5i, cost5i, path5i = dtw(mfcc3.T, mfcci.T)
    dist6i, cost6i, path6i = dtw(mfcc4.T, mfcci.T)
    dists[i] = (dist3i + dist4i + dist5i + dist6i)/4


plt.plot(dists)

word_match_idx = dists.argmin()
word_match_idx_bnds = np.array([word_match_idx,np.ceil(word_match_idx+window_size)])
samples_per_mfcc = 512#len(yX)/mfccX.shape[1]
word_samp_bounds = (2/2) + (word_match_idx_bnds*samples_per_mfcc)

word = yX[word_samp_bounds[0]:word_samp_bounds[1]]
print [word_samp_bounds[1], word_samp_bounds[0]]

plt.plot(word)


IPython.display.Audio(data=word, rate=sr1)
IPython.display.Audio(data=y1, rate=sr1)
IPython.display.Audio(data=yX, rate=srX)


### Narrow down word ###



#### Plot mel spectrogram ####
beg,end = word_match_idx_bnds[:]
beg,end = int(beg),int(end)
mfccWord = mfccX[:,beg:end]
librosa.display.specshow(mfccWord)



#dist1X, cost1X, path1X = dtw(mfcc1.T, mfccWord.T/np.max(mfccWord))
#dist1X, cost1X, path1X = dtw(mfcc1.T, mfccX.T/np.max(mfccX))
dist1X, cost1X, path1X = dtw(mfcc1.T, mfccWord.T)
dist1X, cost1X, path1X = dtw(mfcc1.T, mfccX.T)
show_image(dist1X,cost1X,path1X)

