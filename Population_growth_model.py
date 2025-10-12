import matplotlib.pyplot as plt

def logistic_growth(p0, r, K, generations):
    """Model population growth with logistic equation"""
    population = [p0]
    
    for _ in range(generations):
        p_current = population[-1]
        p_next = p_current + r * p_current * (1 - p_current/K)
        population.append(p_next)
    
    return population

def get_float_input(prompt, default_value=None):
    """Get float input from user with optional default value"""
    while True:
        try:
            user_input = input(prompt)
            if default_value and user_input.strip() == "":
                return default_value
            value = float(user_input)
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int_input(prompt, default_value=None):
    """Get integer input from user with optional default value"""
    while True:
        try:
            user_input = input(prompt)
            if default_value and user_input.strip() == "":
                return default_value
            value = int(user_input)
            if value <= 0:
                print("Please enter a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Main program
print("Population Growth Model (Logistic Growth)")
print("=" * 40)
print("This model simulates population growth with limited resources.")
print()

# Get input from user with sensible defaults
print("Enter the parameters for the population growth model:")
print("(Press Enter to use default values)")

initial_pop = get_float_input("Initial population size [default: 100]: ", 100)
growth_rate = get_float_input("Growth rate (0-1) [default: 0.5]: ", 0.5)
carrying_capacity = get_float_input("Carrying capacity [default: 10000]: ", 10000)
time_points = get_int_input("Number of time periods [default: 50]: ", 50)

# Validate growth rate
if growth_rate > 1:
    print("Warning: Growth rate > 1 may lead to unstable behavior.")
    proceed = input("Do you want to continue? (y/n): ").lower()
    if proceed != 'y':
        print("Simulation cancelled.")
        exit()

# Run simulation
print("\nRunning simulation...")
pop_history = logistic_growth(initial_pop, growth_rate, carrying_capacity, time_points)

# Display results summary
print("\nSimulation Results:")
print(f"Final population size: {pop_history[-1]:.2f}")
print(f"Maximum population reached: {max(pop_history):.2f}")
print(f"Percentage of carrying capacity: {(pop_history[-1]/carrying_capacity)*100:.2f}%")

# Create the plot
plt.figure(figsize=(12, 6))

# Main population growth curve
plt.plot(pop_history, 'b-', linewidth=2, label='Population Size')

# Add carrying capacity line
plt.axhline(y=carrying_capacity, color='r', linestyle='--', 
            label=f'Carrying Capacity (K={carrying_capacity})')

# Customize the plot
plt.xlabel('Time (generations)')
plt.ylabel('Population Size')
plt.title(f'Logistic Population Growth\n'
          f'r={growth_rate}, K={carrying_capacity}, N₀={initial_pop}')
plt.legend()
plt.grid(True, alpha=0.3)

# Add some annotations
plt.text(len(pop_history)*0.7, carrying_capacity*0.8, 
         f'Final population: {pop_history[-1]:.0f}', 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

plt.tight_layout()
plt.show()

# Optional: Ask if user wants to see data table
show_table = input("\nWould you like to see the population data table? (y/n): ").lower()
if show_table == 'y':
    print("\nTime vs Population Data:")
    print("Time\tPopulation")
    print("-" * 20)
    for i, pop in enumerate(pop_history):
        if i % 5 == 0 or i == len(pop_history) - 1:  # Show every 5th point and last point
            print(f"{i}\t{pop:.2f}")
