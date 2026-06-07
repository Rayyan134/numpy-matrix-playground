import numpy as np

from src.matrix_ops import (
    create_matrix,
    get_shape,
    get_transpose,
    reshape_numbers,
    concatenate_arrays,
    vertical_stack,
    horizontal_stack,
)


def main() -> None:
    """Run NumPy array operation demonstrations."""

    matrix = create_matrix()

    print("Original Matrix:\n")
    print(matrix)
    print()

    print(f"Shape: {get_shape(matrix)}")
    print()

    print("Transpose:\n")
    print(get_transpose(matrix))
    print()

    numbers = np.array([1, 2, 3, 4, 5, 6])

    print("Reshaped:\n")
    print(reshape_numbers(numbers))
    print()

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print("Concatenated:\n")
    print(concatenate_arrays(a, b))
    print()

    c = np.array([7, 8, 9])

    print("Vertical Stack:\n")
    print(vertical_stack(a, b, c))
    print()

    matrix_a = np.array([
        [1, 2],
        [3, 4]
    ])

    matrix_b = np.array([
        [5, 6],
        [7, 8]
    ])

    print("Horizontal Stack:\n")
    print(horizontal_stack(matrix_a, matrix_b))


if __name__ == "__main__":
    main()