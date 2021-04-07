class Invoice:
    def __init__(self, invoiceId, customerId, lastName, firstName, phoneNumber,
                 address, items={}, salesTax=0):
        """
        Constructs all invoice object
        params: invoiceId, customerId lastName, firstName, phoneNumber, address
        optional itemsWith Price
        returns: constructed invoice object
        """

        self.__invoiceId = invoiceId
        self.__customerId = customerId
        self.__lastName = lastName
        self.__firstName = firstName
        self.__phoneNumber = phoneNumber
        self.__address = address
        self.__items = items
        self.__salesTax = salesTax

    def add_item(self, itemName, price):
        """
        Add item to invoice.
        :params itemName, price
        :returns None
        """
        self.__items.update({itemName: price})

    def create_invoice(self):
        """
        Returns printed invoice
        :params none
        :returns printed invoice
        """
        total = 0

        for itemName, itemPrice in self.__items.items():
            print(f"{itemName}......${itemPrice:,.2f}")
            total += itemPrice

        tax = total * self.__salesTax
        total += tax

        print(f"Tax.....${tax:,.2f}")
        print(f"Total.....${total:,.2f}")


if __name__ == '__main__':

    # Driver code
    # Sales tax is 7.75 % in Anaheim.
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802',
                      'Mouse', 'Minnie', '555-867-5309', salesTax=.0775)
    invoice.add_item('Ipad', 799.99)
    invoice.add_item('Surface', 999.99)
    invoice.create_invoice()
