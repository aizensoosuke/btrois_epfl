""" Parameters for generating grading data. This file must be hidden from
the students.
"""

grading_params = {
    'count_support_vectors': dict(),
    'compute_primal_coef': dict(),
    'find_probabilities': dict(N=100, D=5, K=6),
    'top_k': dict(N=517, K=13, k=7),
    'kernel_matrix': dict(N=43, D=13),
    'compute_eigvecs': dict()
}
