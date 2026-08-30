class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre_product = [] 
        suff_product = [0] * len(nums)

        prod = 1
        prod2 = 1

        pre_product.append(1)

        for i in range(1, len(nums)):
            prod *= nums[i-1]
            pre_product.append(prod)

        # nums = nums[::-1]

        suff_product[-1] = 1
        
        # for j in range(1, len(nums)):
        #     prod2 *= nums[j-1]
        #     suff_product.append(prod2)

        for j in range(len(nums) - 2, -1, -1):
            prod2 *= nums[j + 1]
            suff_product[j] = prod2

        for i in range(len(nums)):
            pre_product[i] = pre_product[i] * suff_product[i]

        return pre_product