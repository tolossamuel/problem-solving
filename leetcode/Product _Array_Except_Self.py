
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = []
        prefix = []
        product1 = 1
        product2 = 1
        new_product = []
        for i in range(len(nums)):
            product1 *= nums[i]
            prefix.append(product1)
            product2 *= nums[len(nums)-1-i]
            postfix.insert(0,product2)
        for i in range(len(nums)):
            if i == 0:
                new_product.append(postfix[i+1])
            elif i ==  (len(nums)-1):
                new_product.append(prefix[i-1])
            else:
                mul = prefix[i-1]*postfix[i+1]
                new_product.append(mul)
        return new_product



