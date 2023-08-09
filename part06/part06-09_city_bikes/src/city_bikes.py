# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    stations = {}
    with open("src/" + filename) as file_name:
        for line in file_name:
            line = line.replace("\n", "")
            data = line.split(";")
            if data[0] == "Longitude":
                continue
            stations[data[3]] = (float(data[0]), float(data[1]))
    return stations

def distance(stations: dict, station1: str, station2: str):
    station1_location = stations[station1]
    station2_location = stations[station2]
    x_km = (float(station1_location[0]) - float(station2_location[0])) * 55.26
    y_km = (float(station1_location[1]) - float(station2_location[1])) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    greatest = ["", "", 0]
    for station1 in stations:
        for station2 in stations:
            temp_distance = distance(stations, station1, station2)
            if temp_distance > greatest[2]:
                greatest.clear()
                greatest.append(station1)
                greatest.append(station2)
                greatest.append(temp_distance)
    return (greatest[0], greatest[1], greatest[2])

if __name__ == "__main__":
    stations = get_station_data("stations1.csv")
    distance_between = distance(stations, "Kaivopuisto", "Viiskulma")
    print(greatest_distance(stations))