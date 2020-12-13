import plotly.express as px
from typing import List


def bar_plot_co2(year: List[int], climate: List[float], country_name: str) -> None:
    """
    creates a bar plot that maps the given years to its CO2 emissions
    """
    fig = px.bar(x=year, y=climate, title='CO2 Emission for ' + country_name,
                 labels= dict(x="year", y="CO2 emission (Mg)"))
    fig.show()


def bar_plot_tree_loss(year: List[int], climate: List[float], country_name: str) -> None:
    fig = px.bar(x=year, y=climate, title='Tree Loss Rate for ' + country_name,
                 labels= dict(x="year", y="tree lost rate (ha)"))
    fig.show()


def bar_plot_biomass(year: List[int], climate: List[float], country_name: str) -> None:
    fig = px.bar(x=year, y=climate, title='Biomass Loss Rate for ' + country_name,
                 labels= dict(x="year", y="biomass loss (Mg)"))
    fig.add_trace(x=year, y=climate)
    fig.show()




