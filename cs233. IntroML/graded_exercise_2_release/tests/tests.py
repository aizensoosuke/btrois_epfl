""" Unit tests for Graded Exercise #1.
"""

# 3rd party.
import numpy as np

# Project files.
import tests.helpers as helpers
from matplotlib import pyplot as plt

def test(test_function):
    """ Decorator used for each test case. Pretty-prints assert exceptions
    (i.e. those asserts which are used within separate tests) and raises
    unhandeled exceptions (i.e. those which might appear due to the bugs
    on students' side).
    """
    def process_exceptions(*args, **kwargs):
        exception_caught = None
        function_result = None

        try:
            function_result = test_function(*args, **kwargs)
        except AssertionError as e:
            exception_caught = e
        except Exception as other_exception:
            raise other_exception

        if exception_caught is None:
            print("[{}] No problems detected. Your code is correct! "
                  "\U0001f60e".format(test_function.__name__))
        else:
            print("[{}] - {} \U0001f635".format(test_function.__name__,
                                                exception_caught))
        return function_result
    return process_exceptions


################################################################################
# TESTS
################################################################################

@test
def test_lda_mat_data_mean(scope):
    exercise_id = 'lda_mat_data_mean'
    
    # Load test data
    test_data = helpers.get_test_data(exercise_id)
    
    te_x = test_data['te_x']
    te_meanval = test_data['te_meanval']
    gr_x = test_data['gr_x']
    
    ### Test `lda_mat_data_mean function`.
    lda_mat_data_mean_func = helpers.resolve('lda_mat_data_mean', scope)
    
    # Test student implementation on unit test data
    stud_te_meanval = lda_mat_data_mean_func(te_x)
    
    # Test student implementation on grading data
    stud_gr_meanval = lda_mat_data_mean_func(gr_x)
    
    stud_grad = dict(stud_gr_meanval=stud_gr_meanval)
    helpers.register_answer('lda_mat_data_mean', stud_grad, scope)
    
    # [TEST] Number of dims.
    fail_msg = 'Function should return 2-dimensional array. Found {} dims'.\
        format(stud_te_meanval.ndim)
    assert stud_te_meanval.ndim == 2, fail_msg
    
    #[TEST]
    helpers.compare_np_arrays(stud_te_meanval, te_meanval, varname='x_bar')

@test
def test_lda_mat_clswise_mean(scope):
    exercise_id = 'lda_mat_clswise_mean'
    
    # Load test data
    test_data = helpers.get_test_data(exercise_id)
    
    te_x=test_data['te_x']
    te_labels=test_data['te_labels']
    te_num_classes=test_data['te_num_classes']
    te_meanval=test_data['te_meanval']
    
    gr_x=test_data['gr_x']
    gr_labels=test_data['gr_labels']
    gr_num_classes=test_data['gr_num_classes']

    
    ### Test `lda_mat_data_mean function`.
    lda_mat_clswise_mean_func = helpers.resolve('lda_mat_clswise_mean', scope)
    
    # Test student implementation on unit test data
    stud_te_meanval = lda_mat_clswise_mean_func(te_x,te_labels,te_num_classes)
    
    # Test student implementation on grading data
    stud_gr_meanval = lda_mat_clswise_mean_func(gr_x,gr_labels,gr_num_classes)
    
    stud_grad = dict(stud_gr_meanval=stud_gr_meanval)
    helpers.register_answer('lda_mat_clswise_mean', stud_grad, scope)
    
    # [TEST] Data type.
    fail_msg = 'Function should return list, found "{}"'.\
        format(type(stud_te_meanval))
    assert isinstance(stud_te_meanval, list), fail_msg

    
    # [TEST] Number of dims.
    fail_msg = 'Function should return list of 2-dimensional array. Found {} dims'.\
        format(stud_te_meanval[0].ndim)
    assert stud_te_meanval[0].ndim == 2, fail_msg
    
    # [TEST] Shape of elements.
    fail_msg = 'Function should return list of 2-dimensional array with shape:{} found shape as {}'.\
        format(te_meanval[0].shape, stud_te_meanval[0].shape)
    assert stud_te_meanval[0].shape == te_meanval[0].shape , fail_msg
    
    
    #[TEST]
    helpers.compare_np_arrays(np.array(stud_te_meanval), np.array(te_meanval), varname='mu_c')


@test
def test_lda_mat(scope):
    exercise_id = 'lda_mat'
    
    # Load test data
    test_data = helpers.get_test_data(exercise_id)
    
    te_meanval = test_data['te_meanval']
    te_mu_c = test_data['te_mu_c']
    te_S_w = test_data['te_S_w'] 
    te_S_b = test_data['te_S_b'] 
    te_data = test_data['te_data']
    te_labels = test_data['te_labels']
    te_num_classes = test_data['te_num_classes']
    
    gr_data = test_data['gr_data']
    gr_labels = test_data['gr_labels']
    gr_num_classes = test_data['gr_num_classes']
    gr_meanval = test_data['gr_meanval']
    gr_mu_c = test_data['gr_mu_c']
    
    ### Test `lda_mat function`.
    lda_mat_func = helpers.resolve('lda_mat', scope)
    
    # Test student implementation on unit test data
    stud_te_S_w, stud_te_S_b = lda_mat_func(te_data,te_labels,te_num_classes,te_meanval,te_mu_c)
    
    # Test student implementation on grading test data
    stud_gr_S_w, stud_gr_S_b = lda_mat_func(gr_data,gr_labels,gr_num_classes,gr_meanval,gr_mu_c)
    
    stud_grad = dict(stud_gr_S_w=stud_gr_S_w, stud_gr_S_b=stud_gr_S_b)
    helpers.register_answer('lda_mat', stud_grad, scope)
    
    # [TEST] Data type.
    fail_msg = 'Function should return S_w as np.ndarray, found "{}"'.\
        format(type(stud_te_S_w))
    assert isinstance(stud_te_S_w, np.ndarray), fail_msg
    
    # [TEST] Data type.
    fail_msg = 'Function should return S_b as np.ndarray, found "{}"'.\
        format(type(stud_te_S_b))
    assert isinstance(stud_te_S_b, np.ndarray), fail_msg
    
    # [TEST] Shape of mat.
    fail_msg = 'Function should return S_w with shape:{} found shape as {}'.\
        format(te_S_w.shape, stud_te_S_w.shape)
    assert te_S_w.shape == stud_te_S_w.shape , fail_msg

    # [TEST] Shape of mat.
    fail_msg = 'Function should return S_b with shape:{} found shape as {}'.\
        format(te_S_b.shape, stud_te_S_b.shape)
    assert te_S_b.shape == stud_te_S_b.shape , fail_msg
    
    #[TEST]
    helpers.compare_np_arrays(stud_te_S_w, te_S_w, varname='S_w')
    helpers.compare_np_arrays(stud_te_S_b, te_S_b, varname='S_b')

@test
def test_count_support_vectors(scope):
    exercise_id = 'count_support_vectors'
    test_data = helpers.get_test_data(exercise_id)

    y_te = test_data['te_y']
    df_te = test_data['te_df']
    n_te = test_data['te_n']

    y_gr = test_data['gr_y']
    df_gr = test_data['gr_df']

    count_support_vectors = helpers.resolve('count_support_vectors', scope)
    # Apply student's `init_centers` and register the results.
    stud_te_n = count_support_vectors(df_te, y_te)
    stud_gr_n = count_support_vectors(df_gr, y_gr)
    helpers.register_answer('count_support_vectors', stud_gr_n, scope)

    helpers.compare_int(stud_te_n, n_te, varname='count_support_vectors')


@test
def test_compute_primal_coef(scope):
    exercise_id = 'compute_primal_coef'
    test_data = helpers.get_test_data(exercise_id)

    te_dual_coef = test_data['te_dual_coef']
    te_labels = test_data['te_labels']
    te_support_vectors = test_data['te_support_vectors']
    te_w = test_data['te_w']

    gr_dual_coef = test_data['gr_dual_coef']
    gr_labels = test_data['gr_labels']
    gr_support_vectors = test_data['gr_support_vectors']

    compute_w = helpers.resolve('compute_primal_coef', scope)
    # Apply student's `init_centers` and register the results.
    stud_te_w = compute_w(te_dual_coef, te_labels, te_support_vectors)
    stud_gr_n = compute_w(gr_dual_coef, gr_labels, gr_support_vectors)
    helpers.register_answer('compute_primal_coef', stud_gr_n, scope)

    helpers.compare_np_arrays(stud_te_w, te_w, varname='compute_primal_coef')


def test_choose_kernel(scope, answer):
    # if answer != 'P' or answer != 'R':
    fail_msg = 'Your answer is not \'P\' or \'p\' or \'R \' or \'r\'. It is \'{}\''. \
        format(answer)
    assert (answer == 'P' or answer == 'p' or answer == 'R' or answer == 'r'), fail_msg
    print('Format is correct.\U0001f60e')
    helpers.register_answer('choose_kernel', answer, scope)


@test
def test_kernel_matrix(scope):
    exercise_id = 'kernel_matrix'

    # Load test data
    test_data = helpers.get_test_data(exercise_id)
    X_te = test_data['X_te']
    X_new_te = test_data['X_new_te']
    K_te = test_data['K_te']
    K_new_te = test_data['K_new_te']
    X_gr = test_data['X_gr']
    X_new_gr = test_data['X_new_gr']
    K_gr = test_data['K_gr']

    # Get student's implementation.
    update_kernel_matrix = helpers.resolve('update_kernel_matrix', scope)

    # Apply student's `update_kernel_matrix` and register the results.
    stud_K_new_te = update_kernel_matrix(K_te, X_te, X_new_te)
    stud_K_new_gr = update_kernel_matrix(K_gr, X_gr, X_new_gr)
    helpers.register_answer('update_kernel_matrix', stud_K_new_gr, scope)

    # [TEST] Data type.
    fail_msg = 'Function should return np.ndarray, found "{}"'.\
        format(type(stud_K_new_te))
    assert isinstance(stud_K_new_te, np.ndarray), fail_msg

    # [TEST] Number of dims.
    fail_msg = 'Function should return 2-dimensional array. Found {} dims'.\
        format(stud_K_new_te.ndim)
    assert stud_K_new_te.ndim == 2, fail_msg

    # [TEST] Shape.
    fail_msg = 'Your kernel matrix has wrong shape.'
    assert K_new_te.shape == stud_K_new_te.shape

    # [TEST] Last row/column.
    fail_msg = 'Your kernel matrix does not contain correct values.'
    assert np.allclose(K_new_te[-1, :-1], stud_K_new_te[-1, :-1]), fail_msg
    assert np.allclose(K_new_te[:-1, -1], stud_K_new_te[:-1, -1]), fail_msg

    # [TEST] Last row/column.
    fail_msg = 'You might have forgotten to compute the kernel value for ' \
               '`x_new` itself or you are doing something else wrong.'
    assert np.isclose(K_new_te[-1, -1], stud_K_new_te[-1, -1])

@test 
def test_find_probabilities(scope):
    exercise_id = 'find_probabilities'
    find_probabilities = helpers.resolve('find_probabilities', scope)

    test_data = helpers.get_test_data(exercise_id)
    te_X = test_data["te_X"]
    te_W = test_data["te_W"]
    te_probabilities = test_data["te_probabilities"]

    gr_X = test_data["gr_X"]
    gr_W = test_data["gr_W"]

     # Apply student's function and register results
    student_te_probabilities = find_probabilities(te_X, te_W)
    student_gr_probabilities = find_probabilities(gr_X, gr_W)
    helpers.register_answer(exercise_id, student_gr_probabilities, scope)

    # [TEST] Data type.
    fail_msg = 'Function should return np.ndarray, found "{}"'.format(type(student_te_probabilities))
    assert isinstance(student_te_probabilities, np.ndarray), fail_msg

    # [TEST] shape of probabilities array
    fail_msg = 'The shape of your probabilities array is incorrect.'
    assert student_te_probabilities.shape == te_probabilities.shape, fail_msg

    # [TEST] min prob, max prob
    fail_msg = 'Your probability values should be between 0 and 1. In your case, the minimum probability is {}' \
                'and your maximum probability is {}'.format(np.min(student_te_probabilities), np.max(student_te_probabilities))    
    assert np.min(student_te_probabilities) >= 0. and np.max(student_te_probabilities) <= 1., fail_msg

    fail_msg = 'Probability values should sum up to 1 for all classes.'
    assert np.allclose(np.sum(student_te_probabilities, axis=1), 1.), fail_msg

    helpers.compare_np_arrays(te_probabilities, student_te_probabilities, varname=exercise_id)
    
    return student_te_probabilities


@test
def test_top_k(scope):
    exercise_id = 'top_k'

    # Load test data
    test_data = helpers.get_test_data(exercise_id)
    probs_te = test_data['probs_te']
    k_te = test_data['k_te']
    labs_te = test_data['labs_te']
    probs_gr = test_data['probs_gr']
    k_gr = test_data['k_gr']

    # Get student's implementation.
    top_k = helpers.resolve('top_k', scope)

    # Apply student's `update_kernel_matrix` and register the results.
    stud_labs_te = top_k(probs_te, k_te)
    stud_labs_gr = top_k(probs_gr, k_gr)
    helpers.register_answer('top_k', stud_labs_gr, scope)

    # [TEST] Shape.
    fail_msg = 'Your labels have wrong shape. Expected {}, received {}.'.\
        format(labs_te.shape, stud_labs_te.shape)
    assert stud_labs_te.shape == labs_te.shape

    # [TEST] Wrong values.
    fail_msg = 'You return wrong labels.'
    assert np.allclose(stud_labs_te, labs_te)
    

@test
def test_compute_eigvecs(scope):
    
    exercise_id = 'compute_eigvecs'
    test_data = helpers.get_test_data(exercise_id)

    # get implementation
    compute_eigenvec_func = helpers.resolve('compute_eigvecs', scope)

    # get data from stored file
    X_te = test_data['X_te']
    eigvals_c_te = test_data['eigvals_c_te']
    eigvecs_c_te = test_data['eigvecs_c_te']
    eigvecs_b_te = test_data['eigvecs_b_te']

    X_gr = test_data['X_gr']
    eigvecs_c_gr = test_data['eigvecs_c_gr']
    eigvals_c_gr = test_data['eigvals_c_gr']

    

    # run the function on test data
    eigvecs_b_te_stud  =  compute_eigenvec_func(X_te,eigvecs_c_te, eigvals_c_te)
   
    # run the function on grading data
    eigvecs_b_gr_stud  =  compute_eigenvec_func(X_gr,eigvecs_c_gr, eigvals_c_gr)
    
     # [TEST] shape of eigvecs_b should the same
    fail_msg = 'The shape of your computed eigvecs_S matrix is incorrect.'
    assert eigvecs_b_te_stud.shape == eigvecs_b_te.shape, fail_msg

    # [TEST]
    helpers.compare_np_arrays(eigvecs_b_te_stud, eigvecs_b_te, varname='eigvecs_S')
    
    # register answer 
    helpers.register_answer('compute_eigvecs', eigvecs_b_gr_stud, scope)


    
