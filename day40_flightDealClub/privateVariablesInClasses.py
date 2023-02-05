import password

class Test:
    def __init__(self):
        """

        """
        # this is both visible and accessible from importing code
        self.kiwi = password.kiwi_password
        # this is NOT visible, BUT ACCESSIBLE
        self._us_kiwi = password.kiwi_password
        # this is NEITHER visible or ACCESSIBLE
        self.__tus_kiwi = password.kiwi_password

    # BOTH functions work as expected.
    def print_us(self):
        print(self._us_kiwi)

    # In particular, this one worked even though the variable
    # was invisible to the importing code
    def print_tus(self):
        print(self.__tus_kiwi)

    
