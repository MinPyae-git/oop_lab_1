import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps


def aggregate(aggregation_key, aggregation_function, dict_list):
    values = []
    for item in dict_list:
        values.append(float(item[aggregation_key]))
    return aggregation_function(values)
    


# Print the average temperature of all the cities
avg_temp = aggregate('temperature', lambda x: sum(x) / len(x), cities)
print(f'Average temperature of all cities: {avg_temp}°C')

# Print all cities in Germany
filtered= filter (lambda x:x['country'] == 'Germany' ,cities)
print(filtered)

# Print all cities in Spain with a temperature above 12°C
filtered_spain = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
print(filtered_spain)

# Count the number of unique countries
unique_countries = set()
for city in cities:
    unique_countries.add(city['country'])
print(f'Number of unique countries: {len(unique_countries)}')

# Print the average temperature for all the cities in Germany
avg_temp_germany = aggregate('temperature', lambda x: sum(x) / len(x), filter(lambda x: x['country'] == 'Germany', cities))
print(f'Average temperature of cities in Germany: {avg_temp_germany}°C')


# Print the max temperature for all the cities in Italy
max_temp_italy = aggregate('temperature', max, filter(lambda x: x['country'] == 'Italy', cities))
print(f'Max temperature of cities in Italy: {max_temp_italy}°C')
