
def minTime(machines, goal):
    min_days = 1
    max_days = max(machines) * goal
    
    while(min_days!=max_days):

        mid = (min_days+max_days)//2
        workdone = 0

        for i in machines:
            workdone += mid//i
        
        if workdone >= goal:
            max_days = mid
        else:
            min_days = mid+1

    return min_days


machines = [2, 3, 4, 6]
goal = 20
print(minTime(machines, goal))
    