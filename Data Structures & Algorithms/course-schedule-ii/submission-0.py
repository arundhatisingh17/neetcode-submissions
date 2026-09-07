class Solution:
    def dfs(self, crs: int, prereq_dep: dict, visited: set, visiting: set) -> bool:

        if crs in visited:
            return True

        if crs in visiting:
            return False

        visiting.add(crs)

        for c in prereq_dep[crs]:
            if not self.dfs(c, prereq_dep, visited, visiting):
                return False

        visiting.remove(crs)
        visited.add(crs)
        self.final_list.append(crs)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereq_dep = {}
        self.final_list = []

        visited = set()
        visiting = set()

        for i in range(numCourses):
            prereq_dep[i] = []
        
        # build out the dependency list
        for item in prerequisites:
            crs = item[0]
            prereq = item[1]
            prereq_dep[prereq].append(crs)

        for key, val in prereq_dep.items():
            if not self.dfs(key, prereq_dep, visited, visiting):
                return []

        return self.final_list[::-1]