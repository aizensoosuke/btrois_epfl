""" Parameters for generating grading data.
"""

grading_params = {
    'find_probabilities': dict(N=100, D=5, K=6),
    'confusion_matrix':  dict(),
    'simulate_cover': dict(D=50, num_trials=50, min_N=2, max_N=200, step_of_N=25),
    'expand_X_with_pairwise_products': dict(X_0=[10, 20], X_1=[2,10,20], d=[2,3,5,15]),
    'expand_and_normalize_X': dict(X_0=[10, 20], X_1=[2,10,20], d=[2,3,5,15]),
    'find_margin_width': dict(),
    'find_C': dict(),
    'softmax': dict(N=100, D=5, C=8),
    'loss_logreg': dict(N=100, D=5, C=8),
    'gradient_logreg': dict(N=100, D=5, C=8),
    'predict_logreg': dict(N=100, D=5, C=8),
    'true_false_pos_neg': dict(N=1000),
    'cosine_dist': dict(N=200, D = 5),
    'predict_label': dict(K=10),
    'tp_rate': dict(tp=300, fn=600, fp=200, tn=500),
    'fp_rate': dict(fp=200, tn=500, tp=300, fn=600),
    'roc_curve': dict(N=1000)
}
