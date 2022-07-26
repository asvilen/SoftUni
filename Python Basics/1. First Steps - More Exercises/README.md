# First Steps in programming with Python - Extracurricular Exercises
The "More Exercises" section in the testing platform of SoftUni contains additional problems that were not disucssed during the lection/excersises sessions. This folder houses my suggestions for solutions to this set of problems.

## 1. Trapezium face
### Problem
Write a program that reads from the console three fractional numbers $b1$, $b2$ and $h$ and calculates the face of a trapezoid with bases $b1$ and $b2$ and height $h$. The formula for the face of a trapezoid is $(b1 + b2) * h / 2$.
The figure below shows a trapezoid with sides 8 and 13 and height 7. It has a face of $(8 + 13) * 7 / 2 = 73.5$.
The answer must be formatted to the second digit after the decimal point.

![alt text](https://csharp-book.softuni.bg/assets/chapter-2-images/05.Trapezoid-area-01.png "Trapezium")

### Sample Input and Output
| Input  | Output    |
| ------ |:---------:|
|   8    |           |
|   13   | `73.50`   |
|   7    |           |

### My Solution
```python
b1 = float(input())
b2 = float(input())
h = float(input())

area = (b1 + b2) * h / 2

print(f"{area:.2f}")
```
## 2. Face of a triangle
### Problem
Write a program that reads from the console the side and height of a triangle and calculates its face. Use the triangle face formula: $area = a * h / 2$. Format the output to the second decimal place.

### Sample Input and Output
| Input  | Output    |
| ------ |:---------:|
|   20   |           |
|   30   |  `300.00` |
|        |           |
|   15   |           |
|   35   |  `262.50` |
|        |           |
|  7.75  |           |
|  8.45  |  `32.74`  |
|        |           |
| 1.23456|           |
| 4.56789|  `32.74`  |
|        |           |

### My Solution
```python
a = float(input())
h = float(input())

area = a * h / 2

print(f"{area:.2f}")
```

## 3. Console converter: from degrees °C to degrees °F
### Problem
Write a program that reads degrees Celsius (°C) and converts them to degrees Fahrenheit (°F). Search the Internet for a suitable formula to do the calculations. Format the output to the second decimal place.

### Sample Input and Output
| Input  | Output    |    | Input  | Output    |    | Input  | Output    |    | Input  | Output    |
| ------ |:---------:| -- | ------ |:---------:| -- | ------ |:---------:| -- | ------ |:---------:|
|   25   |  `77.00`  |    |   0    |  `32.00`  |    |   -5.5 |  `22.10`  |    |   32.3 |  `90.14`  |

### My Solution
```Python

celcius = float(input())

fahrenheit = (celcius * 9 / 5) + 32

print(f"{fahrenheit:.2f}")
```
## 4. Vegetable market
### Problem
A gardener was selling the harvest from his garden at the vegetable market. It sells vegetables for N leva per kilogram and fruits for M leva per kilogram. Write a program to calculate the income from the harvest in euros (assuming that one euro is equal to BGN 1.94).
##### Console Input
4 numbers are read from the console, one per line:
* First row – Price per kilo of vegetables – real number[0.00… 1000.00]
* Second line – Price per kilogram of fruit – real number[0.00… 1000.00]
* Third row – Total kilograms of vegetables – integer[0… 1000]
* Fourth line – Total kilograms of fruit – integer[0… 1000]
##### Expected Output
To print a single number on the console: the revenue from all fruits and vegetables in euros.
Format the result to the second digit after the decimal point.

### Sample Input and Output
| Input  | Output    |
| ------ |:---------:|
| 0.194  |  `73.50`  |
|  19.4  |           |
|   10   |           |
|   10   |           |
|  1.5   |  `20.62`  |
|  2.5   |           |
|   10   |           |
|   10   |           |

### My Solution
```python
vegetable_price = float(input())
fruits_price = float(input())
vegetable_quantity = float(input())
fruits_quantity = float(input())

vegetables_income = vegetable_price * vegetable_quantity
fruits_income = fruits_price * fruits_quantity
total_in_eur = (vegetables_income + fruits_income) / 1.94

print(f"{total_in_eur:.2f}")
```
## 5. Training lab
### Problem
A classroom has a rectangular dimension w by h meters, without columns in its interior. The hall is divided into two parts - left and right, with a corridor approximately in the middle. There are rows of desks on the left and on the right. At the back of the hall is a large entrance door. In the front part of the hall there is a chair with a podium for the teacher. One workplace occupies 70 by 120 cm (table measuring 70 by 40 cm + space for a chair and passage measuring 70 by 80 cm). The corridor is at least 100 cm wide. It is estimated that exactly 1 job is lost because of the entrance door (which has a 160 cm opening) and because of the chair (which has a size of 160 by 120 cm) exactly 2 jobs are lost. Write a program that enters the dimensions of a classroom and calculates the number of workstations in it for the layout described (see figure).

![alt text](https://csharp-book.softuni.bg/assets/chapter-2-2-images/01.Training-lab-01.png "Study hall")

#### Console Input
2 numbers are read from the console, one per line: w (length in meters) and h (width in meters).
Constraints: 3 ≤ h ≤ w ≤ 100.
#### Expected Output
To print a single integer on the console: the number of seats in the classroom.

### Sample Input and Output
| Input  | Output    |
| ------ |:---------:|
|   15   |   `129`   |
|   8.9  |           |
|        |           |
|   8.4  |   `39`    |
|   5.2  |           |

### My Solution
```python
w = float(input())
h = float(input())
w *= 100
h = h * 100 - 100

columns_of_places = h // 70
rows_of_places = w // 120
total_places = columns_of_places * rows_of_places - 3

print(int(total_places))
```

## 6. Fish market
### Problem
Georgi will have guests in the evening and decides to treat them with bonito, saffron and mussels. So he goes to the fish market to buy a few kilos. The prices in BGN of mackerel and sprat are entered from the console. Also the amount of bonito, saffron and mussels in kilograms. How much money will he need to pay his bill if stock market prices are:
* Bonito – 60% more expensive than mackerel
* Safrid – 80% more expensive than sprat
* Mussels – BGN 7.50 per kilogram
#### Input
5 numbers are read from the console:
* First row – mackerel price per kilogram. A real number in the range [0.00…40.00]
* Second row – sprat price per kilogram. A real number in the range [0.00…30.00]
* Third row - kilos of bonito. A real number in the range [0.00…50.00]
* Fourth row - kilograms of saffron. A real number in the range [0.00… 70.00]
* Fifth row - the kilogram of mussels. An integer in the range [0 ... 100]
#### Output
To print a floating point number on the console: how much money George will need to pay his bill. The number must be formatted to the second decimal place (1.2457 -> 1.25).

### Sample Input and Output
| Input  | Output    |   | Input  | Output    |   | Input  | Output    |
| ------ |:---------:| - | ------ |:---------:| - | ------ |:---------:|
|  6.9   |  `42.96`  |   |  5.55  | `113.82`  |   |  7.79  | `115.92`  |
|  4.20  |           |   |  3.57  |           |   |  5.35  |           |
|  1.5   |           |   |  4.3   |           |   |  9.3   |           |
|  2.5   |           |   |  3.6   |           |   |   0    |           |
|   1    |           |   |   7    |           |   |   0    |           |

### My Solution
```python

macherel_price = float(input())
sprat_price = float(input())
bonito_amount = float(input())
scad_amount = float(input())
clam_amount = int(input())

bonito_price = macherel_price * 1.6
scad_price = sprat_price * 1.8
clam_price = 7.5

total_bill = bonito_price * bonito_amount + scad_amount * scad_price + clam_price * clam_amount

print(f"{total_bill:.2f}")
```

## 7. Painting a house
Write a program to calculate how many liters of paint are needed to paint a house. Green paint is used for the walls and red for the roof. The consumption of green paint is 1 liter for 3.4 m2, and for red - 1 liter for 4.3 m2.

The walls have the following dimensions:
* The front and back walls are squares with side "x"
    - on the front wall there is a rectangular door with a width of 1.2m and a height of 2m
* Sidewalls are rectangles with sides 'x' and 'y'
    - on both side walls there is one square window with a side of 1.5 m

The roof has the following dimensions:
* Two rectangles with sides "x" and "y"
* Two equilateral triangles with side "x" and height "h"

You need to calculate the area of ​​all the sides and the area of ​​the roof to find how many liters of each paint will be needed.
#### Input
3 lines are read from the console:
1. x – the height of the house – a real number in the interval [2...100]
2. y – the length of the side wall – a real number in the interval [2...100]
3. h – the height of the triangular wall of the opening – a real number in the interval [2...100]
#### Expected Output
To print to the console two numbers each on a new line:
* The liters of green paint
* Liters of red paint

Formatted to the second decimal place.

### Sample Input and Output
| Input  | Output    |   | Input  | Output    |
| ------ |:---------:| - | ------ |:---------:|
|   6    |  `54.44`  |   |  10.25 | `152.93`  |
|  10    |  `35.16`  |   |  15.45 | `94.82`   |
|  5.2   |           |   |  8.88  |           |

### My Solution
```python
from math import sqrt

x = float(input())
y = float(input())
h = float(input())

# Walls of the house
door = 1.2 * 2
window = 1.5 * 1.5
front_and_back_m2 = 2 * x * x - door
left_and_right_m2 = 2 * x * y - (2 * window)
# TOTAL
walls_total = front_and_back_m2 + left_and_right_m2
# Roof of the house
roof_top = 2 * x * y
roof_sides = 2 * x * h / 2
#TOTAL
roof_total = roof_sides + roof_top
#Walls Paint
green_paint = walls_total / 3.4
#Roof Paint
red_paint = roof_total / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
```
