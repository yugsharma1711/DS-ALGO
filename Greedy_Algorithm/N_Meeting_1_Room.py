def maximumMeetings(n,start,end):
        duration = list()
        for i in range(len(start)):
            duration.append((start[i], end[i]))
        duration = sorted(duration, key = lambda x : x[1])
        counter = 0
        end_duration = 0
        for i in duration:
            if i[0] > end_duration:
                counter += 1
                end_duration = i[1]
        return counter 
