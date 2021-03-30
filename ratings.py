"""Restaurant rating lister."""

import random

score = open("scores.txt")
restaurant_ratings = {}

for line in score:
    restaurant_name = line.rstrip().split(':')[0]
    restaurant_rating = int(line.rstrip().split(':')[1])
    restaurant_ratings[restaurant_name] = restaurant_rating

def check_ratings_validity(rating):
    while True:
        if rating<1 or rating>5:
            rating = int(input('Please enter a valid rating between 1 and 5!'))
        else:
            return rating
    
    

while True:
    user_choice = input("""What would you like to do today?
                            A. Add a restaurant and rate it
                            B. View list of restaurants and ratings
                            C. Update a random restaurant's rating
                            D. Update a specific restaurant's rating
                            E. Quit""")

    if user_choice == 'A':
        user_restaurant = input('Please enter restaurant name!')
        user_rating = int(input('Please give it a rating between 1-5')) 
        restaurant_ratings[user_restaurant] = check_ratings_validity(user_rating)
    elif user_choice == 'B':
        for name, rating in sorted(restaurant_ratings.items()):
            print(f'{name}:{rating}')
    elif user_choice == 'C':
        random_restaurant = random.choice(list(restaurant_ratings.items()))
        print(f"Here's a random restaurant and it's rating for you: {random_restaurant[0]} : {random_restaurant[1]}")
        new_rating = int(input('Please enter a new rating!'))
        restaurant_ratings[random_restaurant[0]] = check_ratings_validity(new_rating) 
    elif user_choice == 'D':
        give_new_rating = input("Enter the name of the restaurant you'd like to re-rate:")
        if give_new_rating in restaurant_ratings:
            new_score = int(input("Enter new rating:"))
            restaurant_ratings[give_new_rating] = check_ratings_validity(new_score)  
    if user_choice == 'E':
        break 


    

    
    
    
    
    

        





