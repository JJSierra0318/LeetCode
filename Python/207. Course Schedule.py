'''
The idea is to verify if there is any cycle in the prerequisites for the courses.
If there is we return false, for that we keep track of every course's prereq and
which courses we have visited. If we find a visited course while recursivily checking
the prerequisites then we return False.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        visited = set()
        # Save every course with all of their prerequisites
        for course, prereq in prerequisites:
            if course in dic:
                dic[course].append(prereq)
            else:
                dic[course] = [prereq]

        def dfs(course):
            # If it was already visited then there's a cycle
            if course in visited:
                return False
            # If there are no prerequisites
            if not dic.get(course):
                return True
            
            visited.add(course)
            # Then we recursive call for every prerequisite course
            for prereq in dic[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            # If there wasn't any cycle we can remove the prerequisites
            # as it won't change in future interations the fact that there
            # weren't any conflicts with this specific course
            dic[course] = []
            return True

        for crs in dic:
            if not (dfs(crs)):
                return False
        return True