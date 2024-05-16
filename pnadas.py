
import pandas as pd


covid = pd.read_csv('italy-covid-daywise.csv')

print(covid)
print(type(covid))
print(covid.info())
print(covid.describe())
print(covid['new_cases'])
type(covid['new_cases'])

total_case = covid.new_cases.sum()
total_death = covid.new_deaths.sum()
print(f"El numero total de casos es {total_case} y el de muertes {total_death} ")

death_rate = covid.new_deaths.sum() / covid.new_cases.sum()
print(f"La tasa global de mortalidad registrada en italia es: {death_rate*100:.2f}%")

inicial_test = 935310
total_test = inicial_test + covid.new_tests.sum()
print(total_test)

casos_positivos = total_case/total_test
print(casos_positivos)

high_new_cases = covid.new_cases >= 1000
print(covid[high_new_cases])

high_cases = covid[covid.new_cases > 1000]
print(high_cases)
#############################################

with pd.option_context('display.max_rows', 100):
    filtered_covid = covid[covid.new_cases > 1000]
    print(filtered_covid)