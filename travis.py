known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()
    
    if name in known_users:
        print("Hello {}! Welcome back".format(name))
        remove = input("... Or, maybe, you would like to be removed from our database (y/n)?: ").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("Thank you {} for sticking around for what's coming next".format(name))

    else:
        print("Hmmm I don't believe we have met before, {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No hard feelings, see you around!")
            
