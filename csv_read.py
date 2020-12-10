import csv
from dataclasses import dataclass
from typing import List, Tuple

def read_csv_file(filename: str) -> Tuple[List[str], List[List[str]]]:
    with open(filename) as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = [row for row in reader]

    return (headers, data)


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
