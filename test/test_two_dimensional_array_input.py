from app import word_search_solver


def test_grid_must_contain_all_elements_as_string():
    good_grid = [
        ['0'] * 10,
        ['1'] * 10,
        ['2'] * 10,
        ['3'] * 10,
        ['4'] * 10,
        ['5'] * 10,
    ]
    
    bad_grid = [
        [0] * 10,
        [2] * 10,
    ]
    
    bad_grid_2 = [
        ["0"] * 10,
        ["2"] * 10,
        [2] * 2,
    ]
    
    good = word_search_solver.WordSearchSolver._validate_grid(good_grid)
    bad = word_search_solver.WordSearchSolver._validate_grid(bad_grid)
    bad_2 = word_search_solver.WordSearchSolver._validate_grid(bad_grid_2)

    assert good == True
    
    assert bad == False
    assert bad_2 == False


def test_multiple_possible_string_grids():
   
    good_grid_1 = [
        ['0'] * 10,
        ['1'] * 10,
        ['2'] * 10,
        ['3'] * 10,
        ['4'] * 10,
        ['5'] * 10,
    ]
    good_grid_2 = [
        ['0'] * 5,
        ['1'] * 5,
        ['2'] * 5,
        ['3'] * 5,
        ['4'] * 5,
        ['5'] * 5,
    ]
    good_grid_3 = [
        ['0'] * 5,
        ['1'] * 5,
        ['2'] * 5,
        ['3'] * 5,
        ['4'] * 5,
        ['5'] * 5,
        ['6'] * 5,
        ['7'] * 5,
        ['8'] * 5,
    ] 
    
    bad_grid_1 = [
        ['0'] * 10,
        ['1'] * 10,
        ['2'] * 9,
        ['3'] * 10,
        ['4'] * 10,
        ['5'] * 10,
    ]  
    bad_grid_2 = [
        ['0'] * 1,
        ['1'] * 10,
        ['2'] * 9,
        ['3'] * 2,
        ['4'] * 10,
        ['5'] * 4,
    ]  
    bad_grid_3 = [
        ['0'] * 5,
        ['1'] * 5,
        ['2'] * 5,
        ['3'] * 5,
        ['4'] * 6,
        ['5'] * 5,
    ]
    
    
    good_1 = word_search_solver.WordSearchSolver._validate_grid(good_grid_1)
    good_2 = word_search_solver.WordSearchSolver._validate_grid(good_grid_2)
    good_3 = word_search_solver.WordSearchSolver._validate_grid(good_grid_3)

    bad_1 = word_search_solver.WordSearchSolver._validate_grid(bad_grid_1)
    bad_2 = word_search_solver.WordSearchSolver._validate_grid(bad_grid_2)
    bad_3 = word_search_solver.WordSearchSolver._validate_grid(bad_grid_3)

    assert good_1 == True
    assert good_2 == True
    assert good_3 == True

    assert bad_1 == False
    assert bad_2 == False
    assert bad_3 == False

    
