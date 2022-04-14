"""Customers at Hackbright."""


class Customer:
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about melon in console."""

        return (
            f"<Customer: {self.first_name}, {self.last_name}, {self.email}, {self.password}>"
        )


def read_customers_from_file(filepath):
    """Read melon type data and populate dictionary of customers.

    Dictionary will be {id: Melon object}
    """

    customers = {}

    with open(filepath) as file:
        for line in file:
            (
                first_name,
                last_name,
                email,
                password
            ) = line.strip().split("|")

            customers[email] = Customer(
                first_name,
                last_name,
                email,
                password
            )

    return customers


def get_all():
    """Return list of customer objects.

    If you call this function, you should get back a list like the one below.
    NOTE: This is an example of a doctest.

    >>> get_all()
    [<Melon: 2, Crenshaw, $2.00>, <Melon: 14, Ali Baba Watermelon, $2.50>, <Melon: 15, Ancient Watermelon, $3.00>, <Melon: 16, Arkansas Black Watermelon, $4.00>, <Melon: 21, Chris Cross Watermelon, $2.50>, <Melon: 23, Congo Watermelon, $2.00>, <Melon: 25, Crimson Sweet Watermelon, $1.75>, <Melon: 27, Desert King Watermelon, $2.00>, <Melon: 28, Dixie Queen Watermelon, $2.00>, <Melon: 29, Moonbeam Watermon, $2.25>, <Melon: 30, Fairfax Watermelon, $2.00>, <Melon: 32, Golden Honey Watermelon, $2.50>, <Melon: 33, Golden Midget Watermelon, $2.50>, <Melon: 34, Hopi Yellow Watermelon, $2.50>, <Melon: 35, Irish Grey Watermelon, $2.50>, <Melon: 37, Jubilee Bush Watermelon, $2.50>, <Melon: 38, Jubilee Watermelon, $2.50>, <Melon: 42, Ledmon Watermelon, $3.00>, <Melon: 44, Malali Watermelon, $2.00>, <Melon: 45, Melitopolski Watermelon, $3.00>, <Melon: 48, Montenegro Man Melon, $2.50>, <Melon: 49, Moon and Stars Watermelon, $2.50>, <Melon: 52, Navajo Winter Watermelon, $3.00>, <Melon: 54, Orangeglo Watermelon, $2.75>, <Melon: 56, Royal Golden Watermelon, $2.25>, <Melon: 57, Scaly Bark Watermelon, $4.00>, <Melon: 58, Stone Mountain Watermelon, $3.00>, <Melon: 59, Sugar Baby Watermelon, $2.50>, <Melon: 60, Takii Gem Watermelon, $2.75>, <Melon: 61, Tendergold Watermelon, $2.50>, <Melon: 62, Texas Golden Watermelon, $2.75>, <Melon: 63, Thai Rom Dao Watermelon, $2.50>, <Melon: 64, Tom Watson Watermelon, $2.25>, <Melon: 66, White Wonder Watermelon, $2.50>, <Melon: 67, Wilson's Sweet Watermelon, $2.50>]
    """

    # This relies on access to the global dictionary `melon_types`

    return list(customers.values())


def get_by_email(email):
    """Return a customer object, given an email."""

    # This relies on access to the global dictionary `melon_types`

    return customers[email]


# Dictionary to hold types of customers.
#
# Format is {email: Customer object, ... }

customers = read_customers_from_file("customers.txt")

