def find_multiples(integer, limit):
    multiples = []
    for i in range(integer,limit + 1):
        if i % integer == 0: 
            multiples.append(i)
    return multiples