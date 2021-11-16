""" Parameters for generating grading data.
"""

grading_params = {
    'kernel_function': dict(D=5),
    'cosine_distance': dict(N=200, D = 5),
    'manhattan_distance': dict(N=200, D = 5),
    'feature_expansion': dict(),
    'predict_label': dict(K=10),
    'remove_faulty_feature': dict(),
    'get_w_analytical': dict(),
    'RMSE': dict(),
    'positively_correlated_features': dict(),
    'feature_expansion': dict(X_0=[100, 200], X_1=[2,10,20], d=[2,3,5]),
    'decision_function': dict(N=100, D=5),
    'dist': dict(N=100, D=5),
    'split_dists': dict(N=100),
    'are_minimum_distances_close': dict(M=25, L=77),
    'accuracy': dict(N=100),
    'in_correct_margin': dict(N=100),
}
