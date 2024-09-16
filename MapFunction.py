#The map() function applies the specified function to every item of the passed iterable, yields the results, and returns an iterator.
#Parameters:
#function: The function to be called for each element of the specified iterable.
#iterables: One or more iterables separated by a comma (such as string, list, tuple, dictionary).

def square(x):
    return x*x

numbers=[1,2,3,4,5]
sqr_of_numbers=map(square,numbers)
for x in numbers:
    print(next(sqr_of_numbers))


"""In the above example, the map() function applies to each element in the numbers list.
This will return an object of the map class, which is an iterator, and so, we can use the next() function to traverse the list.
https://www.tutorialsteacher.com/python/python-map-function for more use cases with maps"""