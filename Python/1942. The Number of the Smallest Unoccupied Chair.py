'''
The main idea is to keep track of all the seats that are going to end up empty
before the targetFriend arrives, then, make them available once the leaving time
has passed, and everytime a new friend comes we check if there are available seats.
If not, it means all seats are taken and the friend has to sit on the rightmost seat,
increasing the amount of occupied seats
'''

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Save the arrival time of the target friend
        target = times[targetFriend][0]
        # Sort the list based on arrival time
        times.sort(key = lambda x: x[0])

        #Initially there are 0 occupied seat, no one is leaving, and there are no
        # available seats before all the occupied ones
        occupied = 0
        # This will be heap keeping track of the friends that will leave the fastest
        # along with the seat/position they occupied
        leaving = []
        # This will be a heap that keeps track of the seats that have been left available
        available = []

        for i in range(len(times)):

            # If there is a jump in arrival times (e.g 10 to 15) we want to remove
            # all the friends that left during that time period and set those seat,
            # (the positions) as available
            while leaving and leaving[0][0] <= times[i][0]:
                heapq.heappush(available, heapq.heappop(leaving)[1])
            
            # If we found the target we return available set if there is any, if not
            # he would sit in a new one in the rightmost postion (occupied)
            if times[i][0] == target:
                return available[0] if available else occupied

            # Initially set seat as the rightmost occupied seat 
            seat = occupied
            # If there are seats before the last one the new friend will sit in it
            if available:
                seat = heapq.heappop(available)
            # Else he will sit on the furthest right, which will be a new seat
            else:
                occupied += 1
            
            # Finally, we only care about the friends that will leave before the target
            # arrives, as otherwise the will no leave their sit before that. If they leave
            # before the target we append to the heap "leaving" which indicates the time
            # they will leave at and the position the occupied (either the last one or the
            # first available one)
            if times[i][1] <= target:
                heapq.heappush(leaving, [times[i][1], seat])
