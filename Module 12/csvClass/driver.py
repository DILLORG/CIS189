import csv
from county import County


def find_pop(lookUpName, counties):
    for name, county in counties.items():
        if name == lookUpName:
            return f"{name} has a population of {county.population} and an average household income of {county.household}"

    return f"{name} not found in Counties"


def total_population(counties):
    total = 0

    for county in counties.values():
        total += int(county.population)

    return f"The total population is {total}"


if __name__ == '__main__':

    counties = {}
    file = 'data.csv'

    with open(file) as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, row in enumerate(csv_reader):

            # If header row skip
            if index == 0:
                index += 1
                continue

            rank = row[0]
            name = row[1]
            incomePerCapita = row[2]
            incomePerHouseHold = row[3]
            incomePerFamily = row[4]
            population = row[5].replace(',', '')
            numHomes = row[6]

            # Clense data.
            if name == 'Iowa State' or name == 'United States':
                index += 1
                continue

            # Create county and assignt it to its name in the dictionary.
            county = County(rank, name, incomePerCapita, incomePerHouseHold,
                            incomePerFamily, population, numHomes)
            counties[name] = county

    print(find_pop('Dallas', counties))
    print(total_population(counties))
