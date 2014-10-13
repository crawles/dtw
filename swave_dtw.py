plt.plot(y1)
n = n
swindow = y1[133-n:133+n]
noswindow = y1[133-n:133+n]*0
swindow_abs = abs(y1[133-n:133+n])

plt.plot(swindow)

from dtw import dtw

obs_win = np.zeros([66,500])
dists = np.zeros(500+n)
dists_abs = np.zeros(500+n)
dists_no = np.zeros(500+n)
costs = np.zeros(500)
paths = np.zeros(500)

for i in range(len(y2)):
    obs_win[:,i] = y2[i:i+66]
    dist, cost, path = dtw(swindow,obs_win[:,i])
    distno, cost, path = dtw(noswindow,obs_win[:,i])
    dist_abs, cost, path = dtw(swindow_abs,abs(obs_win[:,i]))
    dists[i+n] = dist
    dists_abs[i+n] = dist_abs
    dists_no[i+n] = distno

    
plt.plot(y2)
plt.plot((dists/max(dists))*max(y2))
plt.plot((dists_abs/max(dists_abs))*max(y2))
plt.plot((dists_no/max(dists_abs))*max(y2))






