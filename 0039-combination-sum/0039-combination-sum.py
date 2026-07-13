class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(index, target, path):
            if target == 0:
                result.append(path[:])
                return 

            if target < 0 or index == len(candidates):
                return
            
            path.append(candidates[index])
            dfs(index, target - candidates[index], path)
            path.pop()

            dfs(index+1, target, path)
        dfs(0, target,[])
        return result