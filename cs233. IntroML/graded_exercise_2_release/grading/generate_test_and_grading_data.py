""" Generate expected test results. Must be hidden from students.

All functions implemented by the students are tested independently
e.g. with randomly generated data.
"""

# 3rd party.
import numpy as np

# Python std.
import os

# Project files.
from tests.tests_parameters import test_params
from grading.grading_parameters import grading_params
import tests.helpers as helpers
from tests.helpers import path_test_data, path_grade_data
from helpers.helper import *
from sklearn.svm import SVC

################################################################################
# HELPERS
################################################################################

def save_test_and_grading_data(exercise_id, data_test, data_grading):
    """ Saves the tests and grading data to 2 distinct output directories.

    Args:
        exercise_id (str): Name of the exercise.
        data_test (dict): Tests data to be stored.
        data_grading (dict): GRading data to be stored.
    """
    data_name = exercise_id + '.npz'

    for pth in [path_test_data, path_grade_data]:
        if not os.path.exists(pth):
            print('[WARNING]: Output directory {} does not exist, it will be '
                  'created'.format(os.path.abspath(pth)))
            os.makedirs(pth)

    np.savez(os.path.join(path_test_data, data_name), **data_test)
    np.savez(os.path.join(path_grade_data, data_name), **data_grading)

################################################################################
# TEST CASES
################################################################################

def generate_lda_mat_data_mean(scope):
    exercise_id = 'lda_mat_data_mean'
    
    # Get functions for which to generate test and grading data.
    lda_data_mean_func = helpers.resolve('lda_mat_data_mean', scope)
    
    # Generate real input data for function calls to lda_mat function
    te_x = np.random.rand(100,20)
    gr_x = np.random.rand(100,20)
    
    # testing
    te_meanval = lda_data_mean_func(te_x)
    gr_meanval = lda_data_mean_func(gr_x)
    
    
    # Save test data
    data_test = dict(te_x=te_x,te_meanval=te_meanval, gr_x=gr_x)
    # Save grad data
    data_grad = dict(gr_meanval=gr_meanval,gr_x=gr_x)

    print(" Saving TEST and GRADING data for lda data mean exercise")
    save_test_and_grading_data(exercise_id, data_test, data_grad)

def generate_lda_mat_clswise_mean(scope):
    exercise_id = 'lda_mat_clswise_mean'
    
    # Get functions for which to generate test and grading data.
    lda_clswise_mean_func = helpers.resolve('lda_mat_clswise_mean', scope)
    
    # Generate real input data for function calls to lda_mat function
    te_num_classes = 3
    te_x = np.random.rand(100,20)
    te_labels = np.random.randint(0,te_num_classes,100)
    
    gr_num_classes = 4
    gr_x = np.random.rand(100,20)
    gr_labels = np.random.randint(0,gr_num_classes,100)
    
    # testing
    te_meanval = lda_clswise_mean_func(te_x,te_labels,te_num_classes)
    gr_meanval = lda_clswise_mean_func(gr_x,gr_labels,gr_num_classes)
    
    
    # Save test data
    data_test = dict(te_x=te_x,te_labels=te_labels,te_num_classes=te_num_classes,te_meanval=te_meanval,
                     gr_x=gr_x,gr_labels=gr_labels,gr_num_classes=gr_num_classes)
    # Save grad data
    data_grad = dict(gr_meanval=gr_meanval,gr_x=gr_x,gr_labels=gr_labels,gr_num_classes=gr_num_classes)

    print(" Saving TEST and GRADING data for lda clswise mean exercise")
    save_test_and_grading_data(exercise_id, data_test, data_grad)

    
def generate_lda_mat_data(scope):
    exercise_id = 'lda_mat'
    
    # Get functions for which to generate test and grading data.
    lda_func = helpers.resolve('lda_mat', scope)
    
    # Generate real input data for function calls to lda_mat function
    data, labels, num_classes  = load_lda_data()
    
    te_meanval = data[:75,:].mean(axis=0,keepdims=True)
    gr_meanval = data[75:,:].mean(axis=0,keepdims=True)
    
    te_mu_c = []
    for i in range(num_classes):
        te_mu_c.append(data[:75,:][labels[:75] == i,:].mean(axis=0,keepdims=True))
        
    gr_mu_c = []
    for i in range(num_classes):
        gr_mu_c.append(data[75:,:][labels[75:] == i,:].mean(axis=0,keepdims=True))
        
    # testing 
    te_S_w, te_S_b = lda_func(data[:75,:],labels[:75],num_classes,te_meanval,te_mu_c)
                                                 
    # Save test data
    data_test = dict(te_S_w=te_S_w, te_S_b=te_S_b, te_data=data[:75,:],
                    te_labels=labels[:75], te_num_classes=num_classes, te_meanval=te_meanval, te_mu_c=te_mu_c,
                     gr_data=data[75:,:], gr_labels=labels[75:], gr_num_classes=num_classes, gr_meanval=gr_meanval,
                    gr_mu_c=gr_mu_c)
                                                 
    # grading
    gr_S_w, gr_S_b = lda_func(data[75:,:],labels[75:],num_classes,gr_meanval,gr_mu_c)
                                                        
    # Save the grading data
    data_grad = dict(gr_meanval=gr_meanval, gr_mu_c=gr_mu_c, gr_S_w=gr_S_w, gr_S_b=gr_S_b, gr_data=data[75:,:],
                    gr_label=labels[75:], gr_num_classes=num_classes)
                                      
    print(" Saving TEST and GRADING data for lda exercise")
    save_test_and_grading_data(exercise_id, data_test, data_grad)


def generate_count_support_vectors_data(scope):
    exercise_id = 'count_support_vectors'

    # Get functions for which to generate test and grading data.
    count_support_vectors = helpers.resolve('count_support_vectors', scope)

    # Generate real input data for function calls to lda_mat function
    X, y = load_linear_data()

    clf = SVC(C=2.0, kernel='linear')
    clf.fit(X, y)
    decision_function = clf.decision_function(X)

    te_y = np.concatenate((y[:30], y[-20:]), axis=0)
    te_df = np.concatenate((decision_function[:30], decision_function[-20:]), axis=0)

    gr_y = y[30:-20]
    gr_df = decision_function[30:-20]

    # testing
    te_n = count_support_vectors(te_df, te_y) # result = 8

    # Save test data
    data_test = dict(te_df=te_df, te_y=te_y, te_n=te_n,
                     gr_df=gr_df, gr_y=gr_y)

    # grading
    gr_n = count_support_vectors(gr_df, gr_y) # result = 6

    # Save the grading data
    data_grad = dict(gr_df=gr_df, gr_y=gr_y, gr_n=gr_n)

    print(" Saving TEST and GRADING data for count_support_vectors")
    save_test_and_grading_data(exercise_id, data_test, data_grad)


def generate_compute_primal_coef_data(scope):
    exercise_id = 'compute_primal_coef'

    # Get functions for which to generate test and grading data.
    compute_primal_coef = helpers.resolve('compute_primal_coef', scope)

    # Generate real input data for function calls to lda_mat function
    X, y = load_linear_data()

    te_x = np.concatenate((X[:25], X[-25:]), axis=0)
    te_y = np.concatenate((y[:25], y[-25:]), axis=0)
    te_clf = SVC(C=2.0, kernel='linear')
    te_clf.fit(te_x, te_y)

    te_labels = te_y[te_clf.support_]
    te_support_vectors = te_clf.support_vectors_
    te_dual_coef = te_clf.dual_coef_ * te_labels

    gr_x = X[25:-25]
    gr_y = y[25:-25]
    gr_clf = SVC(C=2.0, kernel='linear')
    gr_clf.fit(gr_x, gr_y)

    gr_labels = gr_y[gr_clf.support_]
    gr_support_vectors = gr_clf.support_vectors_
    gr_dual_coef = gr_clf.dual_coef_ * gr_labels


    # testing
    te_w = compute_primal_coef(te_dual_coef, te_labels, te_support_vectors)

    # Save test data
    data_test = dict(te_dual_coef=te_dual_coef, te_labels=te_labels, te_support_vectors=te_support_vectors, te_w=te_w,
                     gr_dual_coef=gr_dual_coef, gr_labels=gr_labels, gr_support_vectors=gr_support_vectors)

    # grading

    gr_w = compute_primal_coef(gr_dual_coef, gr_labels, gr_support_vectors)

    # Save the grading data
    data_grad = dict(gr_dual_coef=gr_dual_coef, gr_labels=gr_labels, gr_support_vectors=gr_support_vectors, gr_w=gr_w,)

    print(" Saving TEST and GRADING data for compute_primal_coef")
    save_test_and_grading_data(exercise_id, data_test, data_grad)


def generate_kernel_matrix_data(scope):
    exercise_id = 'kernel_matrix'

    # Helpers.
    def kernel_polynomial3(xi, xj):
        """ Computes the polynomial of degree 3 kernel function for the
        input vectors `xi`, `xj`.

        Args:
            xi (np.array): Input vector, shape (D, ).
            xj (np.array): Input vector, shape (D, ).

        Returns:
            float: Result of the kernel function.
        """
        return (xi @ xj + 1) ** 3

    def kernel_matrix(X):
        """ Computes the kernel matrix for data `X` using kernel
        function`kernel_polynomial_3(x, x')`.

        Args:
            X (np.array): Data matrix with data samples of dimension D in the
                rows, shape (N, D).
        Returns:
            np.array: Kernel matrix of the shape (N, N).
        """
        N, D = X.shape

        K = np.zeros((N, N), dtype=np.float64)
        for i in range(N):
            for j in range(N):
                K[i, j] = kernel_polynomial3(X[i], X[j])
        assert np.allclose(K, K.T)
        return K

    # Get functions for which to generate test and grading data.
    update_kernel_matrix = helpers.resolve('update_kernel_matrix', scope)

    # Get parameters for testing and gradind data.
    params_te = test_params[exercise_id]
    params_gr = grading_params[exercise_id]
    N_te = params_te['N']
    D_te = params_te['D']
    N_gr = params_gr['N']
    D_gr = params_gr['D']

    # Generate and store data for the exercise.
    with helpers.IsolatedRNG():
        X_te = np.random.uniform(-1., 1., (N_te, D_te))
        x_new_te = np.random.uniform(-1., 1., (D_te, ))
        X_gr = np.random.uniform(-1., 1., (N_gr, D_gr))
        x_new_gr = np.random.uniform(-1., 1., (D_gr, ))
    K_te = kernel_matrix(X_te)
    K_gr = kernel_matrix(X_gr)

    # Get GT results for test and grading data.
    K_new_te = update_kernel_matrix(K_te, X_te, x_new_te)
    K_new_gr = update_kernel_matrix(K_gr, X_gr, x_new_gr)

    # Save test and grading data.
    data_te = dict(X_te=X_te, X_new_te=x_new_te, K_te=K_te, K_new_te=K_new_te,
                   X_gr=X_gr, X_new_gr=x_new_gr, K_gr=K_gr)
    data_gr = dict(X_gr=X_gr, X_new_gr=x_new_gr, K_gr=K_gr, K_new_gr=K_new_gr)
    save_test_and_grading_data(exercise_id, data_te, data_gr)


def generate_find_probabilities_data(scope):
    exercise_id = 'find_probabilities'

    # Get functions for which to generate test and grading data.
    find_probabilities = helpers.resolve('find_probabilities', scope)

    params_te = test_params[exercise_id]
    te_N = params_te["N"]
    te_D = params_te["D"]
    te_K = params_te["K"]

    params_gr = grading_params[exercise_id]
    gr_N = params_gr['N']
    gr_D = params_gr['D']
    gr_K = params_gr['K']

    with helpers.IsolatedRNG():
        te_X = np.random.uniform(-1., 1., (te_N, te_D))
        te_W = np.random.uniform(-1., 1., (te_D, te_K))

        gr_X = np.random.uniform(-1., 1., (gr_N, gr_D))
        gr_W = np.random.uniform(-1., 1., (gr_D, gr_K))
        
    # testing
    te_probabilities = find_probabilities(te_X, te_W)

    # Save test data
    data_test = dict(te_X=te_X, te_W=te_W, te_probabilities=te_probabilities,
                    gr_X=gr_X, gr_W=gr_W)

    # grading
    gr_probabilities = find_probabilities(gr_X, gr_W)

    # Save the grading data
    data_grad = dict(gr_X=gr_X, gr_W=te_W, gr_probabilities=gr_probabilities)

    save_test_and_grading_data(exercise_id, data_test, data_grad)


def generate_top_k_data(scope):
    exercise_id = 'top_k'

    # Get function.
    top_k = helpers.resolve('top_k', scope)

    # Get params.
    params_te = test_params[exercise_id]
    params_gr = grading_params[exercise_id]
    N_te = params_te['N']
    K_te = params_te['K']
    k_te = params_te['k']
    N_gr = params_gr['N']
    K_gr = params_gr['K']
    k_gr = params_gr['k']

    # Generate data.
    with helpers.IsolatedRNG():
        probs_te = np.random.uniform(0., 1., (N_te, K_te))
        probs_gr = np.random.uniform(0., 1., (N_gr, K_gr))
    probs_te /= np.sum(probs_te, axis=1, keepdims=True)
    probs_gr /= np.sum(probs_gr, axis=1, keepdims=True)
    assert np.allclose(np.sum(probs_te, axis=1), 1.)
    assert np.allclose(np.sum(probs_gr, axis=1), 1.)

    # Get GT results for test and grading data.
    labs_te = top_k(probs_te, k_te)
    labs_gr = top_k(probs_gr, k_gr)

    # Save test and grading data.
    data_te = dict(probs_te=probs_te, k_te=k_te, labs_te=labs_te,
                   probs_gr=probs_gr, k_gr=k_gr)
    data_gr = dict(probs_gr=probs_gr, k_gr=k_gr, labs_gr=labs_gr)
    save_test_and_grading_data(exercise_id, data_te, data_gr)

    


""" 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


Info:  Q3.1 PCA; Generate input-output data for computing eigenvectors of covariance matrix S in an indirect way 
Input:  Data matrix of size (NxD), eigsvecs_M (Nxd), eigvals_M - vector of length d
Output: d-eigen vectors of S of size (Dxd)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
def generate_compute_eigvecs_data(scope):

    exercise_id = 'compute_eigvecs'
    compute_eigvecs_func = helpers.resolve('compute_eigvecs', scope)

    from sklearn import datasets
    from sklearn.preprocessing import PolynomialFeatures

    # load iris dataset
    iris = datasets.load_iris()
    data = iris['data'].astype(np.float32) 
    labels = iris['target'] 
    
    mean = np.mean(data, 0)
    data_mean = data - mean
    poly = PolynomialFeatures(10)
    data_hat = poly.fit_transform(data_mean)
    
    # generate random data matrix
    x_test = data_hat[:50,:]
    x_grade =  data_hat[50:,:]

    print("Shape of Test Dataset:{}".format(x_test.shape))
    print("Shape of Grading Dataset:{}\n".format(x_grade.shape))

    # Compute eigvecs and eigvals for test data
    X_tilde = x_test
    N = x_test.shape[0]
    M = 1 / N * (X_tilde @ X_tilde.T )
    eigvals_c_te, eigvecs_c_te = np.linalg.eigh(M)
    eigvals_c_te = eigvals_c_te[::-1]
    eigvecs_c_te = eigvecs_c_te[:, ::-1]
      
    # sample random-k eigen vectors
    eigindices_te = [0,1,2,3]
    eigvecs_c_te = eigvecs_c_te[:,eigindices_te]
    eigvals_c_te = eigvals_c_te[eigindices_te]

    # Compute eigvecs and eigvals for grading data
    X_tilde = x_grade
    N = x_grade.shape[0]
    M = 1 / N * (X_tilde @ X_tilde.T )
    eigvals_c_gr, eigvecs_c_gr = np.linalg.eigh(M)
    eigvals_c_gr = eigvals_c_gr[::-1]
    eigvecs_c_gr = eigvecs_c_gr[:, ::-1]
        
    # sample random-k eigen vectors for grading data
    eigindices_gr = [2,3,4,5,6,7]
    eigvecs_c_gr = eigvecs_c_gr[:,eigindices_gr]
    eigvals_c_gr = eigvals_c_gr[eigindices_gr]
    
    
    # GT DATA
#     X_tilde = x_grade
#     N = x_test.shape[0]
#     S = 1 / N * (X_tilde.T @ X_tilde )
#     eigvals_b_te_gt, eigvecs_b_te_gt = np.linalg.eigh(S)
#     eigvals_b_te_gt = eigvals_b_te_gt[::-1]
#     eigvecs_b_te_gt = eigvecs_b_te_gt[:, ::-1]
#     eigvecs_b_te_gt = eigvecs_b_te_gt[:,eigindices_gr]
#     eigvals_b_te_gt = eigvals_b_te_gt[eigindices_gr]
#     print("GT eigvals",eigvals_b_te_gt)
#     print("pred eigvals",eigvals_c_te)
    
    
    eigvecs_b_te =  compute_eigvecs_func(x_test, eigvecs_c_te, eigvals_c_te )
    eigvecs_b_gr =  compute_eigvecs_func(x_grade, eigvecs_c_gr, eigvals_c_gr)

    
#     print(eigvecs_b_gr[:10,:2])
#     print(eigvecs_b_te_gt[:10,:2])
    
#     product = np.dot(eigvecs_b_te_gt.T,eigvecs_b_te_gt)
#     print("GT",product)
#     product = np.dot(eigvecs_b_gr.T,eigvecs_b_gr)
#     print("Pred",product)
    
    


    # Save test data and grading data.
    data_test = dict(X_te=x_test, eigvecs_c_te = eigvecs_c_te, eigvals_c_te=eigvals_c_te,eigvecs_b_te=eigvecs_b_te, 
                      X_gr=x_grade, eigvecs_c_gr = eigvecs_c_gr, eigvals_c_gr=eigvals_c_gr)
                   
    
    data_grade = dict(X_gr=x_grade, eigvecs_c_gr = eigvecs_c_gr, eigvals_c_gr=eigvals_c_gr, eigvecs_b_gr=eigvecs_b_gr)
                     
    save_test_and_grading_data(exercise_id, data_test, data_grade)
    
    print("Successfully Generated data for {} exercise".format(exercise_id))