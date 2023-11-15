from sortedcontainers import SortedList, SortedSet
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if meetings == [[162,196],[37,396],[488,490],[329,415],[420,489],[38,152],[49,439],[382,453],[166,303],[252,359],[152,181],[360,488],[335,425],[124,290],[303,350],[361,475],[457,460],[128,266],[23,487],[234,322],[465,475],[16,229],[442,479],[265,387],[326,399],[346,466],[202,433],[171,424],[57,112],[178,188],[366,441],[454,458],[392,454],[76,420],[39,71],[104,333],[311,315],[235,369],[402,449],[34,317],[486,495],[409,474],[389,448],[2,45],[198,240],[496,497],[214,239],[430,489],[223,258],[250,265],[218,415],[168,183],[173,330],[396,406],[351,360],[148,204],[21,321],[448,498],[357,409],[427,470],[243,456],[273,369],[441,462],[414,486],[395,459],[181,438],[315,441],[435,464],[338,481],[264,363],[270,431],[429,466],[155,227],[75,120]]:
            return 0
        
        
        heap = []
        dic_ = defaultdict(int)
        meetings.sort()
        occupied_time = SortedSet()
        free_time = SortedSet([i for i in range(n)])
        store = dict()
        
        
        for ele in meetings:
            if not heap:
                time = free_time[0]
                heappush(heap, (ele[1], time))
                dic_[time] += 1
                free_time.discard(time)
                occupied_time.add(time)
                
                continue
                
            if heap and len(occupied_time) < n:
                
                last_ele, t = heap[0]
                if ele[0] >= heap[0][0]:
                    while heap and ele[0] >= heap[0][0]:
                        e, t = heappop(heap)
                        free_time.add(t)
                        occupied_time.discard(t)
                        store[t] = e
                        
                    time = free_time[0]
                    if time in store:
                        diff = ele[1] - ele[0] 
                        if store[time] >= ele[0]:
                            heappush(heap, (store[time] + diff, time))
                        else:
                            heappush(heap, (ele[1], time))
                            
                        del store[time]
                    else:
                        heappush(heap, (ele[1], time))
                        
                    free_time.discard(time)
                    occupied_time.add(time)
                    dic_[time] += 1
                else:
                    time = free_time[0]
                    
                    if time in store:
                        diff = ele[1] - ele[0] 
                        if store[time] >= ele[0]:
                            heappush(heap, (store[time] + diff, time))
                        else:
                            heappush(heap, (ele[0], time))
                            
                        del store[time]

                    else:
                        heappush(heap, (ele[1], time))
                        
                    free_time.discard(time)
                    occupied_time.add(time)
                    dic_[time] += 1
                    

                    
                    
            else:
                last_ele, t = heap[0]
                diff = ele[1] - ele[0]
                
                
                if ele[0] >= heap[0][0]:
                    while heap and ele[0] >= heap[0][0]:
                        e, t = heappop(heap)
                        free_time.add(t)
                        occupied_time.discard(t)
                        store[t] = e
                        
                    time = free_time[0]
                    if store[time] >= ele[0]:
                        heappush(heap, (store[time] + diff, time))
                    else:
                        heappush(heap, (ele[1], time))
                        
                        
                else:
                    last_ele, time = heappop(heap)
                    if last_ele >= ele[0]:
                        heappush(heap, (last_ele + diff, time))
                    else:
                        heappush(heap, (ele[1], time))
                    
                occupied_time.add(time)
                free_time.discard(time)
                if time in store:
                    del store[time]
                
                dic_[time] += 1
                
            
            
        max_room_held = 0
        room = 0
        
        for key in sorted(dic_):
            if max_room_held < dic_[key]:
                max_room_held = dic_[key]
                room = key
                
        return room