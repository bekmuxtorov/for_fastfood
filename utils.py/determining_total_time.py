"""
5 minutda -> 4 ta
x minutda -> 1 ta

x = 5 / 4 = 1.25 minut

--

1 km -> 3 minut

"""
from math import sin, cos, sqrt, atan2, radians


TIME_PER_KM = 3
TIME_PER_PRODUCT = 1.25


def total_distance(latitude, longitude):

    # Approximate radius of earth in km
    R = 6373.0
    CURRENT_LAT = 40.36549849420402
    CURRENT_LON = 71.77496578887228

    lat1 = radians(CURRENT_LAT)
    lon1 = radians(CURRENT_LON)
    lat2 = radians(latitude)
    lon2 = radians(longitude)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return round(R * c, 2)


def total_time(latitude, longitude, products_count):
    distance = total_distance(latitude, longitude)
    return distance * TIME_PER_KM + round(products_count * TIME_PER_PRODUCT, 2)
