class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
       
        self.times = times
        counter = persons[0]
        dic = defaultdict(int)
        dic[counter] += 1
        self.persons = [persons[0]]
        for i in range(1,len(persons)):
            dic[persons[i]] += 1
            if persons[i] != counter:
                if dic[persons[i]] >= dic[counter]:
                    counter = persons[i]
            self.persons.append(counter)
    def q(self, t: int) -> int:
        index = bisect.bisect_left(self.times,t)
        if index >= len(self.times) or (self.times[index] > t):
            index -= 1
        return self.persons[index]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)