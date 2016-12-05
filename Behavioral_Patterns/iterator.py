def count_to(count):
    """ Our iterator implementation """

    # Our list
    numbers_in_basque = ["bat", "bi", "hiru", "lau", "bost", "sei", "zazpi", "zortzi", "bederatzi", "hamar"]

    # Our built-in iterator creates a tuple such as (1, "bat")
    iterator = zip(range(count), numbers_in_basque)

    # Iterate through our iterable list. Extract the basque numbers. Put them in an iterator called 'number'
    for position, number in iterator:
        # Returns a 'generator' containing numbers in Basque
        yield number

# Let's test the generator returned by our iterator
max_number = 7
for num in count_to(max_number):
    print("{}".format(num))
