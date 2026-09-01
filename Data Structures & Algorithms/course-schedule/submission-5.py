class Solution:
    def recurBuilder(self, key: int, dict_map: dict, visited: set, visiting: set):

        if key in visited:
            return True

        if key in visiting:
            return False

        visiting.add(key)

        for crs in dict_map[key]:
            if not self.recurBuilder(crs, dict_map, visited, visiting):
                return False

        visiting.remove(key)
        visited.add(key)

        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dict_map = {}
        visiting = set()
        visited = set()
        
        for i in range(numCourses):
            dict_map[i] = []

        for i in range(len(prerequisites)):
            dict_map[prerequisites[i][1]].append(prerequisites[i][0])

        for key, val in dict_map.items():
            if not self.recurBuilder(key, dict_map, visited, visiting):
                return False

        return True
