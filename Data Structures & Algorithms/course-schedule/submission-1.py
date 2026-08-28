class Solution:
    def crsSearch(self, dict_map: dict, seen: set, crs: int, visited: set) -> bool:

        if crs in visited:
            return True
        
        if crs in seen:
            return False

        seen.add(crs)

        for c in dict_map[crs]:
            if not self.crsSearch(dict_map, seen, c, visited):
                return False

        seen.remove(crs)
        visited.add(crs)

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dict_map = {}

        for i in range(numCourses):
            dict_map[i] = []

        for i in range(len(prerequisites)):
            crs = prerequisites[i][0]
            prereq = prerequisites[i][1]

            dict_map[prereq].append(crs)

        print(dict_map)

        seen = set()
        visited = set()

        for i in range(len(dict_map)):
            if not self.crsSearch(dict_map, seen, i, visited):
                return False

        return True

