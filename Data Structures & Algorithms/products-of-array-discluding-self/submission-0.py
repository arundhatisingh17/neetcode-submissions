class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # prefix product
        k = 1
        l = 1

        prefix_product = [1]
        suffix_product = [1]
        
        for i in range(1, len(nums)):
            k = k * nums[i - 1]
            prefix_product.append(k)

        for i in range(len(nums) - 2, -1, -1):
            l = l * nums[i + 1]
            suffix_product.append(l)

        suffix_product = suffix_product[::-1]
        
        for i in range(len(prefix_product)):
            prefix_product[i] = prefix_product[i] * suffix_product[i]

        return prefix_product
        