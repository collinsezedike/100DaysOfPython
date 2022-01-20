travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities" : ["Paris", "Lille", "Bijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities" :["Berlin", "Hamburg", "Stuttgard"]    
},
]

def add_new_country(country_visited, num_visits, cities_visited):
    travel_log.append(
        {
        'country': country_visited, 
        'visits': num_visits, 
        'cities': cities_visited,
        }
    )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)