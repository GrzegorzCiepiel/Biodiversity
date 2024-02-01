import pandas as pd
pd.set_option('display.max_columns', None)
import matplotlib.pyplot as plt

observations = pd.read_csv('observations.csv')
print(observations.head())
print(observations.info())
print('\n')
print(observations.describe())
print('\n')
species_info = pd.read_csv('species_info.csv')
print(species_info.head())
print('\n')
print(species_info.info())
print('\n')
print(species_info.describe())
print('\n')


# What is the distribution of conservation_status for animals?
# Are certain types of species more likely to be endangered?
# Are the differences between species and their conservation status significant?
# Which species were spotted the most at each park?

1.
print(species_info.conservation_status.unique())
print(species_info.conservation_status.value_counts(dropna=False))
print(species_info.conservation_status.value_counts(normalize=True, dropna=False))

endangered = species_info.common_names[species_info.conservation_status == 'Endangered']
print(endangered)