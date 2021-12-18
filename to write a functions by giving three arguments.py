# Write a function which takes three arguments from user

def location (x, y, z):
    print(x,"is a city that is located in",y,"which is in",z)
city, country, continent =map(str, input().split())
location(city, country, continent)
