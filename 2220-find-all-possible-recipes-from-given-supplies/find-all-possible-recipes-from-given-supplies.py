class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        dic = defaultdict(list)
        dependet = defaultdict(int)
        
        for i in range(len(ingredients)):
            for y in ingredients[i]:
                dic[y] += [recipes[i]]
                dependet[recipes[i]] += 1
        order = []
        queue = deque(supplies)
        recipes = set(recipes)
        while(queue):
            curr = queue.popleft()
            if curr in recipes:
                order.append(curr)
            for i in dic[curr]:
                dependet[i] -= 1
                if dependet[i] == 0:
                    queue.append(i)
        return order