# Simple dictionary
capitals = {
    "france": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Little", "Bijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgard"],
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {
        "cities_visited" : ["Paris", "Little", "Bijon"], 
        "total_visits": 12,
            },
    "Germany": {
        "cities_visited" :["Berlin", "Hamburg", "Stuttgard"], 
        "total_visits": 2,
            },
}

# Nesting dictionaries in a list
travel_log = [
    {
        "country": "France", 
        "cities_visited" : ["Paris", "Lille", "Bijon"], 
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited" :["Berlin", "Hamburg", "Stuttgard"], 
        "total_visits": 2,
    },
]