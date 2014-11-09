indiv_costs = []
for i,xy in enumerate(zip(*path1X)):
    cum_cost = cost1X[xy[0],xy[1]]
    if i:
        cur_cost = cum_cost - cost1X[prev_xy[0],prev_xy[1]]
    else:
        cur_cost = cum_cost
    indiv_costs.append(cur_cost)
    prev_xy = xy
plt.plot(indiv_costs)
