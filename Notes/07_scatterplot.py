import csv
import matplotlib.pyplot as plt
import numpy as np

with open("/Users/lindsaycarlin/Desktop/Programming/Programming II 2019/Notes/data/global_firearm_data.txt") as f:
    reader = csv.reader(f, delimiter="\t")
    data = list(reader)

print(data)
headers = data.pop(0)
print(headers)

comps = ["Australia", "Austria", "Belgium", "Belarus", "Canada", "Croatia", "Czech Republic", "Denmark", "England and Wales", "Estonia", "Finland", "France", "Germany", "Iceland", "India", "Ireland", "Italy", "Japan", "Korea, South", "Luxembourg", "Singapore", "Spain", "Sweden", "Taiwan", "Switzerland", "United States", "Turkey"]
country_list = []
homicide_rate = []
average_firearms = []

for country in data:
    if country[0] in comps:
        try:
            homicides = float(country[5])
            homicide_rate.append(homicides)
            firearms = float(country[-2])
            average_firearms.append(firearms)
            name = country[0]
            country_list.append(name)
        except ValueError:
            print(country[0], "had incomplete data")

print(country_list)
print(average_firearms)
print(homicide_rate)

plt.figure(1, figsize=(12, 6))
plt.scatter(average_firearms, homicide_rate)

# best fit line
m, b = np.polyfit(average_firearms, homicide_rate, 1)
fit_x = [0, 100]
fit_y = [b, m * 100 + b]
plt.plot(fit_x, fit_y, color="green")
plt.title("Concentration of Firearms by Country vs. Homicides")
plt.xlabel("Firearms per 100 people")
plt.ylabel("Homicides by firearm per 100k people")

for i in range(len(country_list)):
    plt.annotate(country_list[i], xy=(average_firearms[i], homicide_rate[i]), rotation=45)

plt.show()