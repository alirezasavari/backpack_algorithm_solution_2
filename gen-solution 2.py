# Loop through the generations
for gen in range(max_gen):
  # Print the current generation number
  print("Generation", gen+1)
  # Create an empty list for the new population
  new_population = []
  # Loop through the population size
  for i in range(pop_size):
    # Perform the selection operator to select two parents
    parent1 = selection(population)
    parent2 = selection(population)
    # Perform the crossover operator to generate two offspring
    offspring1, offspring2 = crossover(parent1, parent2)
    # Perform the mutation operator on the offspring
    offspring1 = mutation(offspring1)
    offspring2 = mutation(offspring2)
    # Add the offspring to the new population
    new_population.append(offspring1)
    new_population.append(offspring2)
  # Replace the old population with the new population
  population = new_population
  # Loop through the population
  for solution in population:
    # Calculate the fitness of the solution
    solution_fitness = fitness(solution)
    # If the fitness is better than the best fitness
    if solution_fitness > best_fitness:
      # Update the best solution and its fitness
      best_solution = solution
      best_fitness = solution_fitness
  # Print the best solution and its fitness
  print("Best solution:", best_solution)
  print("Best fitness:", best_fitness)

# Print the final result
print("The final solution is:", best_solution)
print("The final fitness is:", best_fitness)
print("The items selected are:")
for i in range(n):
  if best_solution[i] == 1:
    print("Item", i+1, "with weight", weight[i], "size", size[i], "and value", value[i])
