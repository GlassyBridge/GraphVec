# GraphVec

A Python-based Vector library that allows the user to perform a variety of calculations, including the abitily to visualize vectors with mathplotlib.

## Features

- **Vector class**: custom vector class object that allows you to perform basic operations that you would expect from any other types.
- **GraphVector class**: used to graph the custom defined vector objects using mathplotlib.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Operations](#operations)
- [License](#license)

## Installation

1. Clone or download the repository containing the code.
   
2. Make sure you have Python 3 installed on your system and matplotlib is supported(is installed).

3. If you want to run the program on your local machine, just import the `GraphVec.py` script.

   ```bash
   import GraphVec.py
   ```

## Usage

1. Once the script is imported, you'll be able to create a vector object using:
   - x = Vector((p1x,p1y),(p2x,p2y))
   where p1 and p2 are defined with their x and y components.

2. Graph the vectors by puttting them into a list or dictionary and into the GraphVector object.
   - Graphvector(vectors = [], dict = {})

## Operations

This library allows you to add two custom created vector objects.
## using the Vector(p1,p2) object
1. **Addition (`+`)**: Add two vectors.
2. **Subtraction (`-`)**: Subtract two vectors.
3. **Multiplication (`*`)**: Multiply the x and y component of the vector to a scalar.
4. **Division (`/`)**: Divide the x and y components of the vector to a scalar.
## using the GraphVector object
1. **Visualization of vectors from a list**
   you can create a list containing vectors like this:
   ```
   k = Vector((1,1),(2,2))
   vectors = [Vector((0,0),(1,1)),k]
   GraphVector(vectors)
   ```
2. **Visualization of vectors from a list**
   you can create a dictionary containing vectors like this:
   ```
   k = Vector((1,1),(2,2))
   vectors = {'A':Vector((0,0),(1,1)),
               'k':k}
   GraphVector(dict = vectors)
   ```
## Update
- A console based interaction to this library in the Console_GraphVec.py file.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
