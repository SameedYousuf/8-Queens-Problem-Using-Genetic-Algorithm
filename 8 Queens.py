import random

pop_size=1000
pop=[]
gen_gap=0.4
cutoff=int((1-gen_gap)*pop_size)

def fitness(pos):
  score=100
  #horizontal clashes
  for i in range(8):
    j=i+1
    while(j<8):
      if pos[i]==pos[j]:
        score=score-5
      j=j+1

  #positive diagonal    
  for i in range(8):
    row=pos[i]
    col=i
    while(row!=0 and col!=0):
      row=row-1
      col=col-1
      if(pos[col]==row):
        score=score-3
        
    row=pos[i]
    col=i
    while(row!=7 and col!=7):
      row=row+1
      col=col+1
      if(pos[col]==row):
        score=score-3

  #negitive diagonal    
  for i in range(8):
    row=pos[i]
    col=i
    while(row!=0 and col!=0):
      row=row+1
      col=col-1
      if(pos[col]==row):
        score=score-3
        
    row=pos[i]
    col=i
    while(row!=7 and col!=7):
      row=row-1
      col=col+1
      if(pos[col]==row):
        score=score-3

   
  return score


def crossover(par1,par2):
  cut=random.randint(0,7)
  child=par1[:cut]+par2[cut:]
  return child

#initial population
for i in range(pop_size):
  queens=[]
  for row in range(8):
    queens.append(random.randint(0,7))
  pop.append(queens)

gen=0
highest_fitness=0

while(highest_fitness!=100):
  gen=gen+1
  ranked=[]
  for i in range(pop_size):
    ranked.append((fitness(pop[i]),i))
  ranked.sort()
  ranked.reverse()

  highest_fitness=ranked[0][0]
  selected=[]
  for i in range(cutoff):
    selected.append(pop[ranked[i][1]])

  while(len(selected)<len(pop)):
    par1=random.randint(0,cutoff-1)
    par2=random.randint(0,cutoff-1)
    selected.append(crossover(selected[par1],selected[par2]))

  print("Generation number:"+str(gen))
  print("Highest fitness= " + str(highest_fitness))
  print(pop)

  pop=selected

  print(ranked)
  print(selected)