class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        solution = []

        for i in range(len(nums)):
            seen = {}
            target = -nums[i]

            for index in range(i + 1, len(nums)):
                number = nums[index]
                diff = target - number
                if diff in seen:
                    triplet = sorted([-target, diff, number])
                    output.add(tuple(triplet))
                seen[number] = index

        for triplet in output:
            solution.append(list(triplet))
        
        return solution

            




        