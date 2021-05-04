from random import randint, shuffle


class NumberGuesser:

    def __init__(self, min, max, amount):
        """
        Construct all number guesser objects
        :params min smallest generated number, max largest generated number
        amount amount of numbers to generate.
        :returns NumberGuesser.
        """
        self.__guesses = []  # Holds user's guesses.
        self.__nums = []  # Holds generated numbers.

        # Generate a random list of numbers to choose from.
        for num in range(amount):
            self.__nums.append(randint(min, max))

        # Set the correct number to the first member in the list.
        self.__correct = self.__nums[0]

        # Shuffle list.
        shuffle(self.__nums)

    def add_guess(self, guess):
        """
        Add a guess to the list of guessed numbers if the guess is not
        in the list of generated numbers raise a value error.
        :params user's guess.
        :returns none
        """
        guess = int(guess)
        if guess not in self.__nums:
            raise ValueError(f"{guess} not in possible numbers.")

        self.__guesses.append(guess)

    def is_winner(self):
        """
        Check if the user has guessed correctly
        :params none
        :returns true if the user guessed correctly.
        """
        return self.__correct in self.__guesses

    def force_winner(self, index):
        """
        Force winning number to a given index.
        :params index of winning number.
        :returns none.
        """

        index = int(index)
        if index > len(self.__nums):
            raise IndexError(f"{index} is larger the list of possibles")

        # Set the correct number and append it to the list.
        self.__correct = self.__nums[index]
        self.__guesses.append(self.__correct)

    def get_possibles(self):
        """
        Return the list of generated numbers.
        :params none.
        :returns none.
        """
        return self.__nums

    def get_guesses(self):
        """
        Return the list of guessed numbers.
        :params none.
        :returns none.
        """
        return self.__guesses
