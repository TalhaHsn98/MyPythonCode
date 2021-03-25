print("Bismiallah hir rahman nir raheem")
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
#test_traveler = ["Erin Wilkes", "Shanghai, China", ["historical site", "art"]]
def get_destination_index(str):
  destination_index = destinations.index(str)
  return destination_index
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index


#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)


attractions = []
for places in destinations:
    attractions.append([]) 

#attractions = [[], [], [], [], []]
print(attractions)

def add_attraction(destination,attraction):
  try:
    destination_index = get_destination_index(destination)
  except ValueError:
    print("Destination not found")  
    return
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)

add_attraction("Los Angeles, USA",['venice Beach', ['beach']])
print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination,interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  possible_attraction = attractions_in_city 
  attractions_with_interest = []

  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA",["art"])
print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination,traveler_interests)
  interests_strings = "Hi, " + str(traveler[0]) + ", we think you'll like these places around " + str(traveler_destination) + ":"
  for attractions in traveler_attractions:
    interests_strings += attractions   
  return interests_strings

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)

