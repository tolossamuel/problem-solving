class Solution:
    def bestClosingTime(self, customers: str) -> int:
        num_y = customers.count("Y")
        num_n = 0
        penality = float("inf")
        index = 0
        for i in range(len(customers)):
            if penality > (num_y+num_n):
                penality = num_y+num_n
                index = i
            # penality = min(penality,num_y + num_n)
            if customers[i] == "Y":
                num_y -= 1
            else:
                num_n += 1
        # print(num_y,num_n,penality)
        if penality > (num_y+num_n):
            penality = num_y+num_n
            index = len(customers)
        return index

        