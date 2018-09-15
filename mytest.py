
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:06:40 2018

@author: mshokry
"""

import argparse
from timeit import default_timer as timer
from aimacode.search import InstrumentedProblem
from aimacode.search import (breadth_first_search, astar_search,
    breadth_first_tree_search, depth_first_graph_search, uniform_cost_search,
    greedy_best_first_graph_search, depth_limited_search,
    recursive_best_first_search,Node)
from my_air_cargo_problems import air_cargo_p1, air_cargo_p2, air_cargo_p3
from my_planning_graph import PlanningGraph
from run_search import run_search

print(air_cargo_p1)
#node = Node(air_cargo_p1.initial)
#print(node)

p = air_cargo_p1()
print("**** Have Cake example problem setup ****")
print("Initial state for this problem is {}".format(p.initial))
print("Actions for this domain are:")
for a in p.actions_list:
    print('   {}{}'.format(a.name, a.args))
print("Fluents in this problem are:")
for f in p.state_map:
    print('   {}'.format(f))
print("Goal requirement for this problem are:")
for g in p.goal:
    print('   {}'.format(g))
print()
print("*** Breadth First Search")
run_search(p, breadth_first_search)
print("*** Depth First Search")
run_search(p, depth_first_graph_search)
print("*** Uniform Cost Search")
run_search(p, uniform_cost_search)
print("*** Greedy Best First Graph Search - null heuristic")
run_search(p, greedy_best_first_graph_search, parameter=p.h_1)
print("*** A-star null heuristic")
run_search(p, astar_search, p.h_1)


p = air_cargo_p1()
print("**** Air Cargo Problem 1 setup ****")
print("Initial state for this problem is {}".format(p.initial))
print("Actions for this domain are:")
for a in p.actions_list:
    print('   {}{}'.format(a.name, a.args))
print("Fluents in this problem are:")
for f in p.state_map:
    print('   {}'.format(f))
print("Goal requirement for this problem are:")
for g in p.goal:
    print('   {}'.format(g))
print()
print("*** Breadth First Search")
run_search(p, breadth_first_search)
print("*** Depth First Search")
run_search(p, depth_first_graph_search)
print("*** Uniform Cost Search")
run_search(p, uniform_cost_search)
print("*** Greedy Best First Graph Search - null heuristic")
run_search(p, greedy_best_first_graph_search, parameter=p.h_1)
print("*** A-star null heuristic")
run_search(p, astar_search, p.h_1)
print("*** A-star ignore preconditions heuristic")
run_search(p, astar_search, p.h_ignore_preconditions)
print("*** A-star ignore delete lists heuristic")
run_search(p, astar_search, p.h_ignore_delete_lists)
print("*** A-star levelsum heuristic")
run_search(p, astar_search, p.h_pg_levelsum)