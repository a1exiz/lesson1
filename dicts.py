from pprint import pprint

location = {
    "city": "Москва", 
    "temperature": "20"
}
print(location["city"])
location["temperature"] = int(location["temperature"]) - 5
print(location["temperature"])

pprint(location)

print(location.get("country", "Россия"))

location["date"] = "27.05.2019"
print(len(location))