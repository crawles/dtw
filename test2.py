import random

a = [random.randrange(0,4) for i in range(10)]
b = [random.randrange(0,4) for i in range(10)]

y2 = .3*np.arange(10)
y2 = y2.tolist() + y2[::-1].tolist()

y1 = .5*np.arange(10)
y1 = y1.tolist() + y1[::-1].tolist()






