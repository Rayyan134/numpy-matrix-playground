import numpy as np

# Create a script that:


# 1. Creates a 2D array

# 2. Prints shape

# 3. Prints transpose

# 4. Reshapes a 1D array

# 5. Demonstrates concatenate

# 6. Demonstrates vtack

# 7. Demonstrates hstack


# Example output:
"""
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

Vertical Stack:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Horizontal Stack:
[[1 2 5 6]
 [3 4 7 8]]
"""



# 1. Creates a 2D array

def create_matrix() -> np.ndarray:
    
    """
    Creates and returns a 2D NumPy array

    Returns:
        np.darray: A 2D array with shape (2, 3)
    """
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    return matrix



# 2. Prints shape

def get_shape(matrix: np.ndarray) -> tuple:
    
    """
    Returns the shape of a NumPy array.

    Args:
        matrix (np.ndarray): Input array.

    Returns:
        tuple: Shape of the array.
    """
     
    return matrix.shape



# 3. Prints transpose

def get_transpose(matrix: np.ndarray) -> np.ndarray:

    """
    Returns the transpose of a NumPy array.

    Args:
        matrix (np.ndarray): Input array.

    Returns:
        np.ndarray: Transposed array.
    """

    return matrix.T



# 4. Reshapes a 1D array

def reshape_numbers(numbers: np.ndarray) -> np.ndarray:

    """
    Reshapes a 1D array into a 3x2 matrix.

    Args:
        numbers (np.ndarray): 1D NumPy array.

    Returns:
        np.ndarray: Reshaped array.
    """

    numbers = np.array([1, 2, 3, 4, 5, 6])

    return numbers.reshape(3, 2)



# 5. Demonstrates concatenate

def concatenate_arrays(
        array1: np.ndarray,
        array2: np.ndarray
) -> np.ndarray:
    
    """
    Concatenates two arrays.

    Args:
        array1 (np.ndarray): First array.
        array2 (np.ndarray): Second array.

    Returns:
        np.ndarray: Combined array.
    """

    array1 = np.array([1, 2, 3])

    array2 = np.array([4, 5, 6])

    return np.concatenate((array1, array2))



# 6. Demonstrates vtack

def vertical_stack(
    array1: np.ndarray,
    array2: np.ndarray,
    array3: np.ndarray
) -> np.ndarray:
    
    """
    Stacks arrays vertically.

    Args:
        array1 (np.ndarray): First array.
        array2 (np.ndarray): Second array.
        array3 (np.ndarray): Third array.

    Returns:
        np.ndarray: Vertically stacked array.
    """

    array1 = np.array([1, 2, 3])

    array2 = np.array([4, 5, 6])

    array3 = np.array([7, 8, 9])


    return np.vstack((array1, array2, array3))



# 7. Demonstrates hstack

def horizontal_stack(
    matrix1: np.ndarray,
    matrix2: np.ndarray
) -> np.ndarray:
    """
    Stacks two matrices horizontally.

    Args:
        matrix1 (np.ndarray): First matrix.
        matrix2 (np.ndarray): Second matrix.

    Returns:
        np.ndarray: Horizontally stacked matrix.
    """
    
    matrix1 = np.array([
        [1, 2],
        [3, 4]
    ])

    matrix2 = np.array([
        [5, 6],
        [7, 8]
    ])

    return np.hstack((matrix1, matrix2))