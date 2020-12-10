import csv
from dataclasses import dataclass
from typing import List, Tuple

def read_csv_file(filename: str) -> Tuple[List[str], List[List[str]]]:
    """Return the headers and data stored in a csv file with the given filename.

    The return value is a tuple consisting of two elements:

    - The first is a list of strings for the headers of the csv file.
    - The second is a list of lists of strings, where each inner list
      stores a row in the csv file.

    Preconditions:
      - filename refers to a valid csv file with headers
        (notice that we can't express this as a Python expression)
    """
    # "open" is a builtin function that accesses a file on your computer,
    # looking in the same folder as the current Python module.
    # "with" is a special type of compound statement in Python that
    # works with "open" to create a new variable "file" that you can use
    # inside the with block to access the file.
    with open(filename) as file:
        # This line creates a csv reader, which is a Python value that
        # can read csv data from a given file (essentially splitting up the
        # file into rows, and splitting each row by commas).
        reader = csv.reader(file)

        # This line reads the first row of the csv file, which contains the headers.
        # The result is a list of strings.
        headers = next(reader)

        # This list comprehension reads each remaining row of the file,
        # where each row is represented as a list of strings.
        # The header row is *not* included in this list.
        data = [row for row in reader]

    return (headers, data)


def process_row(row: List[str]) -> list:
    """Convert a row of subway delay data to a list with more appropriate data types.

    Notes:
    - You can use int(...) to convert from a string to an integer
    - You'll need to complete the str_to_date and str_to_time functions below
      to use them here.
    - We've left some comments to help you keep track of the values you're returning.

    Preconditions:
        - row has the correct format for the TTC subway delay data set
    """
    return [
        ...,  # date
        ...,  # time
        ...,  # day
        ...,  # station
        ...,  # code
        ...,  # min delay
        ...,  # min gap
        ...,  # bound
        ...,  # line
        ...  # vehicle
    ]


@dataclass
class Country:
    """A custom data type that represents data for a country.
    Instance Attributes:
        - name: the name of this country
        - continent: name of continent
        - year: the year which the data is recorded
        - gdpp: GDP per capita growth (annual %)
        - gdp: current GDP in $
        - tree_cover_loss: tree cover loss in ha
        - co2_emission: the aboveground co2 emission of the country in Mg
        - biomass_loss: aboveground biomass loss of the country in Mg
    """
    name: str
    continent: str
    year: int
    gdpp: float
    gdp: float
    tree_cover_loss: float
    co2_emission: float
    biomass_loss: float

    def __init__(self, name: str, continent: str, year: int, gdpp: float, gdp: float, tree_cover_loss: float, co2_emission: float, biomass_loss: float) -> None:
        """Initialize a new Person object."""
        self.name = name
        self.continent = continent
        self.year =year
        self.gdpp = gdpp
        self.gdp = gdp
        self.tree_cover_loss =tree_cover_loss
        self. co2_emission =co2_emission
        self.biomass_loss =biomass_loss

    def get_attribute(self, name:str, year: int) -> list:
        attribute_list = []
        for one_country in self:
            if name == self.name and year == self.year:
                attribute_list.append(self)

def create_all_countries(database: List[List[str]]) -> None:
    for country in database:
        Country(country[0],country[1], int(country[2]), float(country[3]), float(country[4]), float(country[5]),
                                             float(country[6]), float(country[7]))
