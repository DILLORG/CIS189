class County:
    def __init__(self, rank, name, incomePerCapita, incomePerHouseHold,
                 incomePerFamily, population, numHomes):
        """
        Create all our county objects.
        :params none
        :returns none
        """
        self.rank = rank
        self.name = name
        self.capita = incomePerCapita
        self.household = incomePerHouseHold
        self.family = incomePerFamily
        self.population = population
        self.numHomes = numHomes

    def __str__(self):
        """
        Return string representation of our county object.
        :params none
        :returns none
        """
        return f"County({self.rank}, {self.name}, {self.capita}, {self.household}, {self.family}, {self.population}, {self.numHomes})"

    def __repr__(self):
        """
        Returns representation of our county object.
        :params none
        :returns none
        """
        return f"'County({self.rank}, {self.name}, {self.capita}, {self.household}, {self.family}, {self.population}, {self.numHomes})'"
