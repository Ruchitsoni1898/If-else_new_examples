theater_name = "cinestar"
rated_r_age_limit = 18
print(f"welcome to {theater_name} theaters!!!")
print("welcome to {} theaters!!!".format(theater_name))

user_input = input("Enter your age:")
print(f"user input is: {user_input}")

if int(user_input) >= rated_r_age_limit:
    print("Enjoy your movie")
else:
    adult_present = input("Is another adult with you? Yes or No")
    if adult_present.lower() == 'yes':
        print("Enjoy the movie")
    else:
       print("you must be 18 to watch the movie.")
