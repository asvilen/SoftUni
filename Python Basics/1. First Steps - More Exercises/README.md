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
| Input  | Output    |    | Input  | Output    | Input  | Output    | Input  | Output    |
| ------ |:---------:|    | ------ |:---------:| ------ |:---------:| ------ |:---------:|
|   25   |   77.00   |    |   0    |   32.00   |   -5.5 |   22.10   |   32.3 |   90.14   |

### My Solution
```Python

celcius = float(input())

fahrenheit = (celcius * 9 / 5) + 32

print(f"{fahrenheit:.2f}")
```
