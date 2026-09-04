class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        arr = [0] * len(temperatures)
        stack = []

        stack.append(0)

        for i in range(1, len(temperatures)):
            while stack:
                if temperatures[i] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    arr[idx] = i - idx
                else:
                    break

            stack.append(i)

        return arr