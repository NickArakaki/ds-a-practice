"""
You are given an integer n, which indicates that there are n courses labeled from 1 to n.
You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej]
denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship).
Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it
takes to complete the (i+1)th course.

You must find the minimum number of months needed to complete all the courses following these rules:

You may start taking a course at any time if the prerequisites are met.
Any number of courses can be taken at the same time.
Return the minimum number of months needed to complete all the courses.

Note: The test cases are generated such that it is possible to complete every course
(i.e., the graph is a directed acyclic graph).
"""
from collections import defaultdict

def minimum_time(n: int, relations: list[list[int]], time: list[int]) -> int:
    # calculate time needed to complete each course
    # normalize relations -> { course: [pre-reqs...] }
    # cache = { course: min_time needed }
    # iterate through range (1, n + 1)
        # _recursive func (course)
            # if not normaized_relations[course]:
                # return time[course - 1]
            # if course in cache:
                # return cache[course]

            # cost = 0
            # prereqs = normalized_relations[course]
            # for prereq in prereqs:
                # cost = max(cost, _recursivefunc(prereq))
            # cache[course] = cost

    # list end nodes
    # iterate over end nodes, key into cache and get max of the vals
    # return res
    prereqs = defaultdict(list)
    final_courses = set()
    for prereq, course in relations:
        prereqs[course].append(prereq)
        final_courses.add(course)
        final_courses.discard(prereq)

    cache = {}
    def _calculate_min_time(course: int) -> int:
        course_prereqs = prereqs[course]

        if course in cache:
            return cache[course]
        if not course_prereqs:
            cache[course] = time[course - 1]
            return time[course - 1]

        cost = 0
        for course_prereq in course_prereqs:
            cost = max(cost, _calculate_min_time(course_prereq) + time[course - 1])

        cache[course] = cost
        return cost

    for course in range(1, n + 1):
        _calculate_min_time(course)

    res = 0
    for final_course in final_courses:
        res = max(res, cache[final_course])

    return res



print(minimum_time(n = 3, relations = [[1,3],[2,3]], time = [3,2,5]) == 8)
print(minimum_time(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]) == 12)
print(minimum_time(n = 11, relations=[[1,2],[3,4],[10,11],[2,5],[4,5],[5,6],[6,7],[5,8],[5,9]], time=[1,2,3,4,5,6,7,8,9,10,11]) == 25)
