class Solution:
    def recurBuilder(self, dict_map, key, seen, visited) -> bool:

        if key in seen:
            return False

        if key in visited:
            return True

        seen.add(key)
        for crs in dict_map[key]:
            if not self.recurBuilder(dict_map, crs, seen, visited):
                return False
        
        seen.remove(key)
        visited.add(key)

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dict_map = {}
        seen = set()
        visited = set()
        
        # first create a prerequisite - dependency map
        for i in range(numCourses):
            dict_map[i] = []

        for i in range(len(prerequisites)):
            dict_map[prerequisites[i][1]].append(prerequisites[i][0])

        for key, val in dict_map.items():
            if not self.recurBuilder(dict_map, key, seen, visited):
                return False

        return True