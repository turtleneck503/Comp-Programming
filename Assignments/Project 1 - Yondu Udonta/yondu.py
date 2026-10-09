total_crew = int(input())
other_crew = total_crew - 2

total_gold = int(input())
gold = total_gold

gold -= 3 * other_crew


yondu_cut = int(gold * .13)
gold -= yondu_cut

peter_cut = int(gold * .11)
gold -= peter_cut

crew_cut = gold // total_crew
gold -= crew_cut * total_crew
yondu_cut += crew_cut
peter_cut += crew_cut

rbf = gold

print("Yondu's share: ", yondu_cut)
print("Peter's share: ", peter_cut)
print("Crew: ", crew_cut)
print("RBF: ", rbf)