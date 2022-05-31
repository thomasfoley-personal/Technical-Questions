""""
Given a circular list of gas stations, where we can go from a station i to the station i + 1, and the last one
goes back to the first one, find the index of the station from where we start to be able to traverse all the stations
and go back to the initial one without running out of gas
"""
# Initial thoughts: This is just a graph/optimization problem with conditions of touching all stations, and keeping gas
#                   Could brute force it, but it takes long time
#                   Ask question if it's a directed list, if so just need to find the one that makes sure we have enough
#                   gas prior to the big hit (station 4 to 5 is 8 gas)
"""
Conditions: 
 1) Can only move forward
 2) Gas tank starts empty
 3) gas[i] represents the amount of gas at the station i
 4) cost[i] represents the cost to go form the station i to the next one
 5) the answer is guaranteed ot be unique
 6) if station we're looking for doesn't exist, return -1
"""
def brute_force(gas, cost, start):
    n = len(gas)
    remaining = 0
    i = start
    started = False
    while i != start or not started:
        started = True
        remaining += gas[i] - cost[i]
        if remaining < 0:
            return False
        i = (i + 1) % n
    return True
def gas_station(gas, cost):
    for i in range(len(gas)):
        if brute_force(gas, cost, i):
            return i
    return -1


def optimized_gas_station(gas, cost):
    remaining = 0
    candidate = 0
    for i in range(len(gas)):
        remaining += gas[i] - cost[i]
        if remaining < 0:
            candidate = i + 1
            remaining = 0
    prev_remaining = sum(gas[:candidate])-sum(cost[:candidate])
    # Conditions, if candidate = len(gas), then cycled through array and found no candidate,
    # if remaining + prev_remaining goes negative then couldn't finish second cycle (beginning of array)
    # else then candidate = starting destination
    if candidate == len(gas) or remaining + prev_remaining < 0:
        return -1
    else:
        return candidate

if __name__ == '__main__':
    gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
    cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]
    print(gas_station(gas, cost))
