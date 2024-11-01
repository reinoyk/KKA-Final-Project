import heapq
import numpy as np

# Define the restaurant data
restaurants = {
    'Restaurant1': {'location': (4, 2), 'rating': 4.5, 'type': 'Fast Food', 'price': 2},
    'Restaurant2': {'location': (5, 1), 'rating': 4.5, 'type': 'Healthy', 'price': 3},
    'Restaurant3': {'location': (1, 7), 'rating': 3.5, 'type': 'Traditional', 'price': 1},
    'Restaurant4': {'location': (7, 3), 'rating': 5.0, 'type': 'Fast Food', 'price': 4},
}

# Randomize user location
user_location = (np.random.randint(0, 10), np.random.randint(0, 10))
preferred_type = 'Fast Food'
max_price = 3

# Helper function to calculate Euclidean distance (g(n))
def calculate_distance(l1, l2):
    return ((l1[0] - l2[0]) ** 2 + (l1[1] - l2[1]) ** 2) ** 0.5

# Heuristic function based on rating and food type preference (h(n))
def heuristic(restaurant, preferred_type, max_price):
    rating_score = 5 - restaurant['rating']  # Higher rating = lower score
    type_score = 0 if restaurant['type'] == preferred_type else 1  # 0 if preferred type, 1 otherwise
    price_score = 0 if restaurant['price'] <= max_price else 1  # 0 if within budget, 1 otherwise
    return rating_score + type_score + price_score

# A* Algorithm implementation
def a_star(user_location, restaurants, preferred_type, max_price):
    # Priority queue to hold nodes, starting with the user's location
    queue = []
    heapq.heappush(queue, (0, 'Start', user_location))  # (f(n), current_node, location)

    visited = set()  # Track visited nodes

    while queue:
        f_cost, current_node, current_location = heapq.heappop(queue)

        if current_node != 'Start':
            # If this node represents a restaurant, it's a potential solution
            print(f"Recommended restaurant: {current_node} with f(n) = {f_cost:.2f}")
            return current_node

        visited.add(current_node)
        
        print("User location:", user_location)

        for restaurant, data in restaurants.items():
            if restaurant in visited:
                continue
            
            g_cost = calculate_distance(user_location, data['location'])  # Actual cost (distance)
            h_cost = heuristic(data, preferred_type, max_price)  # Heuristic based on preferences
            f_cost = round(g_cost + h_cost, 2)  # Limiting f_cost to 2 decimal places
            
            print(f"Distance to {restaurant}: {g_cost:.2f}")

            # Add the restaurant to the priority queue with updated f_cost
            heapq.heappush(queue, (f_cost, restaurant, data['location']))

    return None

# Execute A* search
result = a_star(user_location, restaurants, preferred_type, max_price)

if result:
    print(f"Final recommended restaurant: {result}")
else:
    print("No suitable restaurant found.")

