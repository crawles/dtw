from dtw import dtw

x = [0, 0, 1, 1, 2, 4, 2, 1, 2, 0]
y = x[1:] + [1] #[1, 1, 1, 2, 2, 2, 2, 3, 2, 0]

#x = range(10)
#y = [0] * 5 + x

plt.plot(x)
plt.plot(y)

dist, cost, path = dtw(x,y)

print 'Minimum distance found:', dist

imshow(cost.T, origin='lower', cmap=cm.gray, interpolation='nearest')
plot(path[0], path[1], 'w')
xlim((-0.5, cost.shape[0]-0.5))
ylim((-0.5, cost.shape[1]-0.5))


