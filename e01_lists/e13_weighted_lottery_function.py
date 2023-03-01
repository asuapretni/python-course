import numpy as np

def weighted_lottery(weights) :
    container_list = []
    for (name, weight) in weights.items():  # looping over the dictionary
        for _ in range(weight):             # loop depending on weight value
            container_list.append(name)     # add the result (name) to container_list

    return np.random.choice(container_list)  # return a random element from container_list

other_weights = {
    'winning': 1,
    'break_even': 2,
    'losing': 3
}

print(other_weights.items())
print(weighted_lottery(other_weights))