# General Calculator

A Python-based calculator that allows the user to perform a variety of arithmetic, statistical, and other mathematical operations.

## Features

- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division, Exponentiation, and Roots.
- **BMI Calculation**: Calculate Body Mass Index based on height and weight.
- **Advanced Operations**: Max, Min, Sum, Range, Sort, and Central Tendency (Mean, Median, Mode).
- **Statistical Measures**: Dispersion measures like Variance and Standard Deviation.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Operations](#operations)
  - [Arithmetic Operations](#arithmetic-operations)
  - [Other Operations](#other-operations)
- [Stopping and Clearing the Program](#stopping-and-clearing-the-program)
- [License](#license)

## Installation

1. Clone or download the repository containing the code.
   
2. Make sure you have Python 3 installed on your system.

3. If you want to run the program on your local machine, just execute the `GC.py` script.

   ```bash
   python GC.py
   ```

## Usage

1. Once the script is running, you'll be presented with the following operations:
   - **Basic Operations**: [ + , - , * , / , ** , Root , BMI , Other ]
   - **Control Commands**: [Stop] to stop or [Clear] to clear the screen.

2. Input the operation you want to perform. Based on the input, you'll be prompted to enter the required numbers.

3. The program will display the result of the operation.

## Operations

### Arithmetic Operations

These operations are for performing basic mathematical calculations.

1. **Addition (`+`)**: Add two numbers.
2. **Subtraction (`-`)**: Subtract the second number from the first.
3. **Multiplication (`*`)**: Multiply two numbers.
4. **Division (`/`)**: Divide the first number by the second.
5. **Exponentiation (`**`)**: Raise the first number to the power of the second.
6. **Root (`root`)**: Find the Nth root of a number.

When you choose one of these operations, you'll be prompted to input two numbers, and the program will show the result.

### BMI Calculation

Input your height in meters and weight in kilograms, and the program will calculate your **Body Mass Index (BMI)**.

### Other Operations

These operations are related to statistical and other mathematical calculations.

1. **Max**: Find the maximum number in a list of numbers.
2. **Min**: Find the minimum number in a list of numbers.
3. **Sum**: Calculate the sum of a list of numbers.
4. **Sort**: Sort a list of numbers in ascending order.
5. **Central Tendency**:
   - **Mean**: Calculate the average of the numbers.
   - **Median**: Find the middle value of a sorted list of numbers.
   - **Mode**: Find the most frequent number in the list.
6. **Range**: Calculate the difference between the largest and smallest number in a list.
7. **Dispersion**: Calculate variance and standard deviation of a list of numbers.

For operations like Max, Min, Sum, and others, the program will ask for multiple numbers, separated by commas.

### Stopping and Clearing the Program

- **Stop**: Enter "stop" to exit the program.
- **Clear**: Enter "clear" to clear the terminal/command prompt screen.

## Example Workflow

Here’s how the program runs:

1. You start the program and see the available operations:

   ```
   Operations: [ + , - , * , / , ** , Root , BMI , Other ], [Stop] to stop or [Clear] to clear
   ```

2. You choose an operation, e.g., `+` for addition. The program will prompt for two numbers:

   ```
   First number:_ 5
   Second number:_ 3
   Answer = 8
   ```

3. If you want to perform other operations like finding the Max value in a list, you can choose `Other` and then select a specific operation, like `Max`.

4. You can choose to stop the program by typing `stop`, or clear the screen with `clear`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.