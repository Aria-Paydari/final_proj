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
    year: List[int]
    gdpp: List[float]
    gdp: List[float]
    tree_cover_loss: List[float]
    co2_emission: List[float]
    biomass_loss: List[float]

    def __init__(self, name: str, continent: str, year:List[int] , gdpp: List[float], gdp: List[float], tree_cover_loss:
    List[float], co2_emission: List[float], biomass_loss: List[float]) -> None:
        """Initialize a new Person object."""
        self.name = name
        self.continent = continent
        self.year =year
        self.gdpp = gdpp
        self.gdp = gdp
        self.tree_cover_loss =tree_cover_loss
        self. co2_emission =co2_emission
        self.biomass_loss =biomass_loss



    def whole_regression(self, economic_growth: List[float], y: List[float], year2: int) -> float:
        """
        returns predicted value of climate impact with a given year
        Preconditions:
            - len(year1) == len(economic_growth) == len(y)
            - 2050 >= year2 >= 2020
        """
        economic_growth_in_year2 = linear_regression_for_one(self.year, economic_growth, year2)
        predicted_value = linear_regression_for_two(self.year, economic_growth, y, year2, economic_growth_in_year2)
        return predicted_value


def create_all_countries(database: List[List[str]]) -> None:
    for country in database:
        Country(country[0],country[1], get_year_list(database), get_GDPP_list(database, country[0]),get_GDP_list(
            database, country[0]), get_tree_list(database, country[0]),
                                             get_co2_list(database, country[0]), get_biomass_list(database, country[0]))

def get_year_list(database: List[List[str]]) -> List[int]:
    year_list = []
    for country in database:
        if int(country[2]) not in year_list:
            year_list.append(int(country[2]))
    year_list.sort()
    return year_list
def get_GDPP_list(database: List[List[str]], country_name: str) -> List[float]:
    item_list = []
    for country in database:
        if country[0] == country_name:
            item_list.append(float(country[3]))
    return item_list


def get_GDP_list(database: List[List[str]], country_name: str) -> List[float]:
    item_list = []
    for country in database:
        if country[0] == country_name:
            item_list.append(float(country[4]))
    return item_list


def get_tree_list(database: List[List[str]], country_name: str) -> List[float]:
    item_list = []
    for country in database:
        if country[0] == country_name:
            item_list.append(float(country[5]))
    return item_list


def get_co2_list(database: List[List[str]], country_name: str) -> List[float]:
    item_list = []
    for country in database:
        if country[0] == country_name:
            item_list.append(float(country[6]))
    return item_list


def get_biomass_list(database: List[List[str]], country_name: str) -> List[float]:
    item_list = []
    for country in database:
        if country[0] == country_name:
            item_list.append(float(country[7]))
    return item_list

def coefficient_b1_and_b2(x1: List[float], x2: List[float], y: List[float]) -> Tuple[float, float]:
        """returns the coefficients of the linear regression line with two independent variables
            Preconditions:
                - len(x1) == len(x2) == len(y)
        """
        sum_of_x2_squared = 0
        for x in x2:
            sum_of_x2_squared = sum_of_x2_squared + x ** 2
        product_of_x1_y = 0
        for i in range(0, len(x1)):
            product_of_x1_y = product_of_x1_y + x1[i] * y[i]

        product_of_x1_x2 = 0
        for i in range(0, len(x1)):
            product_of_x1_x2 = product_of_x1_x2 + x1[i] * x2[i]

        product_of_x2_y = 0
        for i in range(0, len(x1)):
            product_of_x2_y = product_of_x2_y + x2[i] * y[i]

        sum_of_x1_squared = 0
        for x in x1:
            sum_of_x1_squared = sum_of_x1_squared + x ** 2

        b1 = (sum_of_x2_squared * product_of_x1_y - product_of_x1_x2 * product_of_x2_y) / \
             (sum_of_x1_squared * sum_of_x2_squared - product_of_x1_x2 ** 2)

        b2 = (sum_of_x1_squared * product_of_x2_y -
              product_of_x1_x2 * product_of_x1_y) / (sum_of_x1_squared * sum_of_x2_squared
                                                     - product_of_x1_x2 ** 2)

        return b1, b2

def intercept_for_two(x1: List[float], x2: List[float], b1: float, b2: float, y: List[float]) -> float:
        """
        returns the intercept for the linear regression line with two independent variables
        Preconditions:
            - len(x1) == len(x2) == len(y)
        """
        mean_y = sum(y) / len(y)
        mean_x1 = sum(x1) / len(x1)
        mean_x2 = sum(x2) / len(x2)
        a = mean_y - b1 * mean_x1 - b2 * mean_x2
        return a

def linear_regression_for_two(x1: List[float], x2: List[float], y: List[float], x_1: float, x_2: float) -> float:
        """
        returns the predicted y value with given inputs (two independent variable)
        Preconditions:
            - len(x1) == len(x2) == len(y)
        """
        b1_b2 = coefficient_b1_and_b2(x1, x2, y)
        a = intercept_for_two(x1, x2, b1_b2[0], b1_b2[1], y)
        return a + b1_b2[0] * x_1 + b1_b2[1] * x_2

def coefficient_b(x: List[float], y: List[float]) -> float:
        """
        returns the coefficient for one independent variable regression
        Preconditions:
            - len(x) == len(y)
        """
        product_of_x_y = 0
        for i in range(len(x)):
            product_of_x_y = product_of_x_y + x[i] * y[i]
        product_of_x_squared = 0
        for number in x:
            product_of_x_squared = product_of_x_squared + number * number
        return product_of_x_y / product_of_x_squared

def intercept_for_one(x: List[float], y: List[float], b: float) -> float:
        """
        returns the intercept for one independent variable regression
        Preconditions:
            - len(x) == len(y)
        """
        mean_y = sum(y) / len(y)
        mean_x = sum(x) / len(x)
        return mean_y - b * mean_x

def linear_regression_for_one(x: List[float], y: List[float], predict_x: float) -> float:
        """
        returns the predicted y value with given inputs (one independent variable)
        Preconditions:
            - len(x) == len(y)
        """
        b = coefficient_b(x, y)
        a = intercept_for_one(x, y, b)
        return a + b * predict_x
