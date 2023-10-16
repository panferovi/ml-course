import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    step = np.random.randn(data.shape[0])
    for _ in range(num_steps):
        A =  np.matmul(data, step)
        step = A / np.sqrt(np.sum(A * A))

    return float(np.matmul(step, np.matmul(data, step)) / np.matmul(step, step)), step