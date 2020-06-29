#!/usr/bin/python3

'''
multi line comments
'''

def main():
    movies = [] #one way to create a list
    movies.append('Avatar') #Adds to end of list
    movies.append('Back to the Future')

    print(movies)

    print(movies[0]) #will display first element
    movies.append('GhostBusters')
    print(movies[2])
    print(movies[-1]) #can count backwards through list




if __name__ == '__main__':
    main()
