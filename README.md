# NumPy Basics Toolkit

A beginner-friendly Python project demonstrating core NumPy array operations such as reshaping, transposing, concatenation, and stacking.

This project helps build a strong foundation in NumPy and prepares for data science and AI engineering workflows.

---

## Features

- Create 2D NumPy arrays
- Check array shape
- Transpose matrices
- Reshape 1D arrays into 2D
- Concatenate arrays
- Vertical stacking (vstack)
- Horizontal stacking (hstack)
- Modular Python structure
- Type hints and docstrings

---

## Concepts Covered

- NumPy fundamentals
- Array manipulation
- Matrix operations
- Functional programming
- Modular project structure
- Separation of logic and execution

---

## Project Structure

numpy-basics-toolkit/
│
├── src/
│   ├── __init__.py
│   └── matrix_ops.py
│
├── tests/                      # (optional but professional)
│   └── test_matrix_ops.py
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE                    # (optional but recommended)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/numpy-basics.git
cd numpy-basics
```
## Install dependencies:

```Bash
pip install -r requirements.txt
```

## Usage

Run the project:

```Bash
python main.py
```

## Example Output
```Python
Original Matrix:
[[1 2 3]
[4 5 6]]

Shape: (2, 3)

Transpose:
[[1 4]
[2 5]
[3 6]]

Reshaped:
[[1 2]
[3 4]
[5 6]]

Concatenated:
[1 2 3 4 5 6]

Vertical Stack:
[[1 2 3]
[4 5 6]
[7 8 9]]

Horizontal Stack:
[[1 2 5 6]
[3 4 7 8]]
```

## What I Learned

* NumPy array operations
* Shape vs dimension
* Reshaping rules
* Axis-based stacking
* Modular Python design

## Future Improvements

* Add CLI menu system
* Accept user input arrays
* Add matrix multiplication
* Convert to Jupyter Notebook version
* Add visualizations

# Author
Learning project for AI Engineering / Data Science fundamentals.
