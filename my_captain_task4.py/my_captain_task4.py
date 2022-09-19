#Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.
def most_frequent(d):
    import operator
    
    print('Original dictionary : ',d)
    sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
    print('Dictionary in descending order by value : ',sorted_d)
most_frequent({'m':1,"i":4,'s':4,'p':2})