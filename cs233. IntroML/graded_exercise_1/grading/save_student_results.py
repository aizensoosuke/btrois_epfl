import numpy as np
from matplotlib import pyplot as plt
import grading.helpers as helpers


################################################################################
# Saving student results
################################################################################
def initialize_res(scope):
    exercise_id = "sciper"
    sciper_number = helpers.resolve('sciper_number', scope)
    stud_grad = dict(sciper_number=sciper_number)
    helpers.register_answer(exercise_id, stud_grad, scope)

def kernel_function(scope):
    exercise_id = 'kernel_function'

    # Get functions for which to generate test and grading data.
    func = helpers.resolve(exercise_id, scope)

    # Get the grading data
    test_data = helpers.get_data(exercise_id)

    # run the students' functions
    stud_res = func(test_data['gr_X1'],test_data['gr_X2'])

    #save the students' results
    stud_grad = dict(stud_res=stud_res)
    helpers.register_answer(exercise_id, stud_grad, scope)





# ------------------------- kNN part -------------------------

def save_cosine_distance(scope):
    exercise_id = 'cosine_distance'
    cosine_dist_func = helpers.resolve('cosine_distance', scope)
    grading_data = helpers.get_data(exercise_id)

    example = grading_data["gr_example"]
    training_examples = grading_data["gr_training_examples"]

     # Apply student's function and register results
    student_cosine_dist = cosine_dist_func(example, training_examples)
    helpers.register_answer(exercise_id, student_cosine_dist, scope)




def save_manhattan_distance(scope):
    exercise_id = 'manhattan_distance'
    manhattan_dist_func = helpers.resolve('manhattan_distance', scope)
    grading_data = helpers.get_data(exercise_id)

    example = grading_data["gr_example"]
    training_examples = grading_data["gr_training_examples"]

     # Apply student's function and register results
    student_manhattan_dist = manhattan_dist_func(example, training_examples)
    helpers.register_answer(exercise_id, student_manhattan_dist, scope)




# def save_feature_expansion(scope):
#     exercise_id = 'feature_expansion'
#     feature_expansion_func = helpers.resolve('feature_expansion', scope)
#     grading_data = helpers.get_data(exercise_id)

#     example = grading_data["gr_example"]
#     training_examples = grading_data["gr_training_examples"]

#      # Apply student's function and register results
#     student_feature_expansion = feature_expansion_func(example, training_examples)
#     helpers.register_answer(exercise_id, student_feature_expansion, scope)



def save_feature_expansion(scope):
    # Done
    exercise_id = 'feature_expansion'
    feature_expansion_func = helpers.resolve('feature_expansion', scope)

    grading_data = helpers.get_data(exercise_id)
    student_solutions = {}
    for k, data in grading_data.items():
        # deciphter the settings...
        d = int(k.split('-')[-1])
        sol = feature_expansion_func(data, d)
        student_solutions[k] = sol

    helpers.register_answer(exercise_id, student_solutions, scope)



def save_predict_label(scope):
    exercise_id = 'predict_label'
    predict_label_func = helpers.resolve('predict_label', scope)
    grading_data = helpers.get_data(exercise_id)

    neighbor_labels = grading_data["gr_neighbor_labels"]
    neighbor_distance = grading_data["gr_neighbor_distance"]

     # Apply student's function and register results
    student_predict_label = predict_label_func(neighbor_labels, neighbor_distance)
    helpers.register_answer(exercise_id, student_predict_label, scope)

# ------------------------- linear regression part -------------------------


def save_remove_faulty_feature(scope):
    exercise_id = 'remove_faulty_feature'
    func = helpers.resolve(exercise_id, scope)
    grading_data = helpers.get_data(exercise_id)

    gr_X = grading_data["gr_X"]

     # Apply student's function and register results
    student_res = func(gr_X)
    helpers.register_answer(exercise_id, student_res, scope)

def save_get_w_analytical(scope):
    exercise_id = 'get_w_analytical'
    func = helpers.resolve(exercise_id, scope)
    grading_data = helpers.get_data(exercise_id)

    gr_X = grading_data["gr_X"]
    gr_Y = grading_data["gr_Y"]

    # Apply student's function and register results
    student_res = func(gr_X, gr_Y)
    helpers.register_answer(exercise_id, student_res, scope)

def save_RMSE(scope):
    exercise_id = 'RMSE'
    func = helpers.resolve(exercise_id, scope)
    grading_data = helpers.get_data(exercise_id)

    gr_X = grading_data["gr_X"]
    gr_Y = grading_data["gr_Y"]
    gr_w = grading_data["gr_w"]

     # Apply student's function and register results
    student_res = func(gr_X, gr_Y, gr_w)
    helpers.register_answer(exercise_id, student_res, scope)

def save_positively_correlated_features(scope):
    exercise_id = 'positively_correlated_features'
    func = helpers.resolve(exercise_id, scope)
    grading_data = helpers.get_data(exercise_id)

    gr_w = grading_data["gr_w"]

    # Apply student's function and register results
    keys = ["blacktea", "earlgray", "jasmine", "oolong", "hibiscus"]
    student_res = {}
    for key in keys:
        student_res[key] = func(gr_w, key)

    helpers.register_answer(exercise_id, student_res, scope)
    


# ------------------------- SVM part -------------------------


def decision_function(scope):
    exercise_id = 'decision_function'
    
    # Get functions for which to generate test and grading data.
    func = helpers.resolve(exercise_id, scope)
    
    # Get the grading data
    test_data = helpers.get_data(exercise_id)
    
    # run the students' functions
    stud_res = func(test_data['gr_x'], test_data['gr_w'], test_data['gr_w0'])
    
    #save the students' results
    stud_grad = dict(stud_res=stud_res)
    helpers.register_answer(exercise_id, stud_grad, scope)

def dist(scope):
    exercise_id = 'dist'
    
    # Get functions for which to generate test and grading data.
    func = helpers.resolve(exercise_id, scope)
    
    # Get the grading data
    test_data = helpers.get_data(exercise_id)
    
    # run the students' functions
    stud_res = func(test_data['gr_y_tilde'], test_data['gr_w'])
    
    #save the students' results
    stud_grad = dict(stud_res=stud_res)
    helpers.register_answer(exercise_id, stud_grad, scope)


def split_dists(scope):
    exercise_id = 'split_dists'
    
    # Get functions for which to generate test and grading data.
    func = helpers.resolve(exercise_id, scope)
    
    # Get the grading data
    test_data = helpers.get_data(exercise_id)
    
    # run the students' functions
    stud_res_p, stud_res_n = func(test_data['gr_r'], test_data['gr_Y'])
    
    #save the students' results
    stud_grad = dict(stud_res_p=stud_res_p, stud_res_n=stud_res_n)
    helpers.register_answer(exercise_id, stud_grad, scope)


def are_minimum_distances_close(scope):
    exercise_id = 'are_minimum_distances_close'
    
    # Get functions for which to generate test and grading data.
    func = helpers.resolve(exercise_id, scope)
    
    # Get the grading data
    test_data = helpers.get_data(exercise_id)
    
    # run the students' functions
    stud_res = (func(test_data['gr_r1'], test_data['gr_r1']), func(test_data['gr_r1'], test_data['gr_r2']))
    
    #save the students' results
    stud_grad = dict(stud_res=stud_res)
    helpers.register_answer(exercise_id, stud_grad, scope)


def accuracy(scope):
    exercise_id = 'accuracy'
    
    # Get functions for which to generate test and grading data.
    func = helpers.resolve(exercise_id, scope)
    
    # Get the grading data
    test_data = helpers.get_data(exercise_id)
    
    # run the students' functions
    stud_res = func(test_data['gr_slack'])
    
    #save the students' results
    stud_grad = dict(stud_res=stud_res)
    helpers.register_answer(exercise_id, stud_grad, scope)


def in_correct_margin(scope):
    exercise_id = 'in_correct_margin'
    
    # Get functions for which to generate test and grading data.
    func = helpers.resolve(exercise_id, scope)
    
    # Get the grading data
    test_data = helpers.get_data(exercise_id)
    
    # run the students' functions
    stud_res = func(test_data['gr_slack'])
    
    #save the students' results
    stud_grad = dict(stud_res=stud_res)
    helpers.register_answer(exercise_id, stud_grad, scope)

