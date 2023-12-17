
from sortedcontainers import SortedSet
class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foodDic = {}
        self.ratingDic = {}
        self.cuisinesDic = defaultdict(SortedSet)
        for i in range(len(cuisines)):
            self.cuisinesDic[cuisines[i]].add((-ratings[i],foods[i]))
            self.foodDic[foods[i]] = cuisines[i]
            self.ratingDic[foods[i]] = ratings[i]
        
        

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        cuisine = self.foodDic[food]
        rating = self.ratingDic[food]
        self.cuisinesDic[cuisine].remove((-rating,food))
        self.cuisinesDic[cuisine].add((-newRating,food))
        self.ratingDic[food] = newRating
        print(self.cuisinesDic)
        

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        return self.cuisinesDic[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
