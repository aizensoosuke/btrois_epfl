import numpy as np
from matplotlib import pyplot as plt
import grading.helpers as helpers

# def test(test_function):
#     """ Decorator used for each test case. Pretty-prints assert exceptions
#     (i.e. those asserts which are used within separate tests) and raises
#     unhandeled exceptions (i.e. those which might appear due to the bugs
#     on students' side).
#     """
#     def process_exceptions(*args, **kwargs):
#         exception_caught = None
#         function_result = None

#         try:
#             function_result = test_function(*args, **kwargs)
#         except AssertionError as e:
#             exception_caught = e
#         except Exception as other_exception:
#             raise other_exception

#         return function_result
#     return process_exceptions


################################################################################
# Saving student results
################################################################################

def save_find_probabilities(scope):
    exercise_id = 'find_probabilities'
    find_probabilities = helpers.resolve('find_probabilities', scope)

    grading_data = helpers.get_data(exercise_id)

    gr_X = grading_data["gr_X"]
    gr_W = grading_data["gr_W"]

     # Apply student's function and register results
    student_gr_probabilities = find_probabilities(gr_X, gr_W)
    helpers.register_answer(exercise_id, student_gr_probabilities, scope)


# For linear regression exercise
def save_linear_expansion_with_cross_validation(scope):
    exercise_id = 'linear_expansion_with_cross_validation'
    student_grid_val = helpers.resolve('grid_val', scope)
     # Apply student's function and register results
    helpers.register_answer(exercise_id, student_grid_val, scope)


def save_simulate_cover(scope):
    
    exercise_id = 'simulate_cover'
    simulate_cover_func = helpers.resolve('simulate_cover', scope)
    grading_data = helpers.get_data(exercise_id)
   
    gr_num_trials = grading_data['gr_num_trials']
    gr_D = grading_data['gr_D']
    gr_list_of_N = grading_data['gr_list_of_N']    
    student_gr_fractions = simulate_cover_func(gr_num_trials, gr_D, gr_list_of_N)
    helpers.register_answer(exercise_id, student_gr_fractions, scope)
    
def save_confusion_matrix(scope):
    exercise_id = 'confusion_matrix'
    confusion_matrix_func = helpers.resolve('confusion_matrix', scope)
    grading_data = helpers.get_data(exercise_id)

    X_gr_truelabel = grading_data["X_gr_truelabel"]
    X_gr_predlabel = grading_data["X_gr_predlabel"]
    num_classes = grading_data["num_classes"]


     # Apply student's function and register results
    student_gr_probabilities = confusion_matrix_func(X_gr_truelabel, X_gr_predlabel, num_classes)
    helpers.register_answer(exercise_id, student_gr_probabilities, scope)
    
def save_cosine_dist(scope):
    exercise_id = 'cosine_dist'
    cosine_dist_func = helpers.resolve('cosine_dist', scope)
    grading_data = helpers.get_data(exercise_id)

    example = grading_data["gr_example"]
    training_examples = grading_data["gr_training_examples"]

     # Apply student's function and register results
    student_cosine_dist = cosine_dist_func(example, training_examples)
    helpers.register_answer(exercise_id, student_cosine_dist, scope)
    
def save_predict_label(scope):
    exercise_id = 'predict_label'
    predict_label_func = helpers.resolve('predict_label', scope)
    grading_data = helpers.get_data(exercise_id)

    neighbor_labels = grading_data["gr_neighbor_labels"]
    neighbor_distance = grading_data["gr_neighbor_distance"]

     # Apply student's function and register results
    student_predict_label = predict_label_func(neighbor_labels, neighbor_distance)
    helpers.register_answer(exercise_id, student_predict_label, scope)


def save_expand_X_with_pairwise_products(scope):
    # Done
    exercise_id = 'expand_X_with_pairwise_products'
    expand_X_with_pairwise_products = helpers.resolve('expand_X_with_pairwise_products', scope)

    grading_data = helpers.get_data(exercise_id)
    student_solutions = {}
    for k, data in grading_data.items():
        # deciphter the settings...
        d = int(k.split('-')[-1])
        sol = expand_X_with_pairwise_products(data, d)
        student_solutions[k] = sol

    helpers.register_answer(exercise_id, student_solutions, scope)

def save_expand_and_normalize_X(scope):
    # Done
    exercise_id = 'expand_and_normalize_X'
    expand_and_normalize_X = helpers.resolve('expand_and_normalize_X', scope)
    expand_X = helpers.resolve('expand_X', scope)
    expand_X_with_pairwise_products = helpers.resolve('expand_X_with_pairwise_products', scope)

    grading_data = helpers.get_data(exercise_id)
    student_solutions = {}
    for k, data in grading_data.items():
        # deciphter the settings...
        d = int(k.split('-')[-1])
        sol_1 = expand_and_normalize_X(data, d, expand_X)
        sol_2 = expand_and_normalize_X(data, d, expand_X_with_pairwise_products)
        student_solutions[k + '-expand_X'] = sol_1
        student_solutions[k + '-expand_X_with_pairwise_products'] = sol_2

    helpers.register_answer(exercise_id, student_solutions, scope)

def save_find_C(scope):
    exercise_id = 'find_C'

    # Load test data
    test_data = helpers.get_data(exercise_id)

    gr_Ws = test_data['gr_Ws']
    gr_Cs = test_data['gr_Cs']


    ### Test `find_C function`.
    find_C_func = helpers.resolve('find_C', scope)

    # Test student implementation on grading data
    stud_gr_c = []
    for w,c in zip(gr_Ws,gr_Cs):
        stud_gr_c.append(find_C_func(w,c))

    stud_grad = dict(stud_gr_c=stud_gr_c)
    helpers.register_answer('find_C', stud_grad, scope)


def save_find_margin_width(scope):
    exercise_id = 'find_margin_width'

    # Load test data
    test_data = helpers.get_data(exercise_id)

    gr_x = test_data['X']
    gr_y = test_data['Y']
    gr_c = test_data['gr_C']

    ### Test `find_margin_width function`.
    find_margin_width_func = helpers.resolve('find_margin_width', scope)


    # Test student implementation on grading data
    stud_gr_width =[]
    for c in gr_c:
        stud_gr_width.append(find_margin_width_func(gr_x,gr_y,c))

    stud_grad = dict(stud_gr_width=stud_gr_width)
    helpers.register_answer('find_margin_width', stud_grad, scope)

def save_softmax(scope):
    exercise_id = 'softmax'

    # Get functions for which to generate grading data.
    softmax_func = helpers.resolve('softmax', scope)
    
    #get test data
    test_data = helpers.get_data(exercise_id)
    gr_X = test_data['gr_X']
    gr_W = test_data['gr_W']
    
    ### Test `save_softmax function`.
    softmax_res = softmax_func(gr_X, gr_W)

    # Save the grading data
    stud_grad = dict(softmax_res=softmax_res)

    helpers.register_answer('softmax', stud_grad, scope)

def save_loss_logreg(scope):
    exercise_id = 'loss_logreg'

    # Get functions for which to generate grading data.
    logreg_func = helpers.resolve('loss_logreg', scope)
    
    #get test data
    test_data = helpers.get_data(exercise_id)
    gr_X = test_data['gr_X']
    gr_W = test_data['gr_W']
    gr_Y = test_data['gr_Y']

    ### Test function.
    logreg_res = logreg_func(gr_X, gr_Y, gr_W)

    # Save the grading data
    stud_grad = dict(logreg_res=logreg_res)

    helpers.register_answer('loss_logreg', stud_grad, scope)

def initialize_res(scope):
    exercise_id = "sciper"
    sciper_number = helpers.resolve('sciper_number', scope)
    stud_grad = dict(sciper_number=sciper_number)
    helpers.register_answer(exercise_id, stud_grad, scope)

def save_gradient_logreg(scope):
    exercise_id = 'gradient_logreg'

    # Get functions for which to generate grading data.
    gradient_logreg_func = helpers.resolve('gradient_logreg', scope)
    
    #get test data
    test_data = helpers.get_data(exercise_id)
    gr_X = test_data['gr_X']
    gr_W = test_data['gr_W']
    gr_Y = test_data['gr_Y']

    ### Test function.
    gradient_logreg_res = gradient_logreg_func(gr_X, gr_Y, gr_W)

    # Save the grading data
    stud_grad = dict(gradient_logreg_res=gradient_logreg_res)

    helpers.register_answer('gradient_logreg', stud_grad, scope)


def save_predict_logreg(scope):
    exercise_id = 'predict_logreg'

    # Get functions for which to generate grading data.
    predict_logreg_func = helpers.resolve('predict_logreg', scope)
    
    #get test data
    test_data = helpers.get_data(exercise_id)
    gr_X = test_data['gr_X']
    gr_W = test_data['gr_W']

    ### Test function.
    predict_logreg_res = predict_logreg_func(gr_X, gr_W)

    # Save the grading data
    stud_grad = dict(predict_logreg_res=predict_logreg_res)

    helpers.register_answer('predict_logreg', stud_grad, scope)

def save_true_false_pos_neg(scope):
    exercise_id = 'true_false_pos_neg'

    # Get functions for which to generate grading data.
    true_false_pos_neg_func = helpers.resolve('true_false_pos_neg', scope)

    #get test data
    test_data = helpers.get_data(exercise_id)
    y_gt = test_data['y_gt']
    y_pred = test_data['y_pred']

    ### Test function.
    true_false_pos_neg_res = true_false_pos_neg_func(y_gt, y_pred)

    # Save the grading data
    stud_grad = dict(true_false_pos_neg_res=true_false_pos_neg_res)
    helpers.register_answer('true_false_pos_neg', stud_grad, scope)

def save_tp_rate(scope):
    exercise_id = 'tp_rate'

    # Get functions for which to generate grading data.
    tp_rate_func = helpers.resolve('tp_rate', scope)

    # Get parameters for grading data.
    test_data = helpers.get_data(exercise_id)
    tp = test_data['tp']
    fn = test_data['fn']
    fp = test_data['fp']
    tn = test_data['tn']

    # grading
    tp_rate_res = tp_rate_func(tp, fp, tn, fn)

    # Save the grading data
    stud_grad = dict(tp_rate_res=tp_rate_res)
    helpers.register_answer('tp_rate', stud_grad, scope)

def save_fp_rate(scope):
    exercise_id = 'fp_rate'

    # Get functions for which to generate grading data.
    fp_rate_func = helpers.resolve('fp_rate', scope)

    # Get parameters for grading data.
    test_data = helpers.get_data(exercise_id)
    fp = test_data['fp']
    tn = test_data['tn']
    tp = test_data['tp']
    fn = test_data['fn']
    
    # grading
    fp_rate_res = fp_rate_func(tp, fp, tn, fn)

    # Save the grading data
    stud_grad = dict(fp_rate_res=fp_rate_res)
    helpers.register_answer(exercise_id, stud_grad, scope)

def save_roc_curve(scope):
    exercise_id = 'roc_curve'

    # Get functions for which to generate grading data.
    roc_curve_func = helpers.resolve('roc_curve', scope)
    fcl = helpers.resolve('class_thresh', scope)

    # Get parameters for grading data.
    test_data = helpers.get_data(exercise_id)
    x = test_data['x']
    y = test_data['y']
    ts = test_data['ts']

    # grading
    roc_curve_res = roc_curve_func(fcl, x, y, ts)

    # Save the grading data
    stud_grad = dict(roc_curve_res=roc_curve_res)
    helpers.register_answer(exercise_id, stud_grad, scope)

def save_final_classifier(scope):
    exercise_id = "final_classifier"
    final_classifier = helpers.resolve('final_classifier', scope)
    stud_grad = dict(final_classifier=final_classifier)
    helpers.register_answer(exercise_id, stud_grad, scope)

def knn_q1(scope):
    exercise_id = "knn_q1"
    Q1 = helpers.resolve('Q1', scope)
    stud_grad = dict(Q1=Q1)
    helpers.register_answer(exercise_id, stud_grad, scope)


def knn_q2(scope):
    exercise_id = "knn_q2"
    Q2 = helpers.resolve('Q2', scope)
    stud_grad = dict(Q2=Q2)
    helpers.register_answer(exercise_id, stud_grad, scope)

    
def knn_q3(scope):
    exercise_id = "knn_q3"
    Q3 = helpers.resolve('Q3', scope)
    stud_grad = dict(Q3=Q3)
    helpers.register_answer(exercise_id, stud_grad, scope)


def knn_q4(scope):
    exercise_id = "knn_q4"
    Q4 = helpers.resolve('Q4', scope)
    stud_grad = dict(Q4=Q4)
    helpers.register_answer(exercise_id, stud_grad, scope)


    