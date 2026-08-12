from datetime import datetime
import csv


def tet_syllogism_deduction_first_value_n(first_formula, second_formula, third_formula):
    if first_formula[0] == "n" and first_formula[4] == "n":  # caluculates potential "n"-values of first value
        return ("n")
    elif second_formula[0] == "n" and second_formula[4] == "n":
        return ("n")
    elif third_formula[0] == "n" and third_formula[4] == "n":
        return ("n")

    elif first_formula[0] == "n" and second_formula[4] == "n":
        return ("n")
    elif second_formula[0] == "n" and first_formula[4] == "n":
        return ("n")

    elif first_formula[0] == "n" and third_formula[4] == "n":
        return ("n")        
    elif third_formula[0] == "n" and first_formula[4] == "n":
        return ("n")

    elif second_formula[0] == "n" and third_formula[4] == "n":
        return ("n")        
    elif third_formula[0] == "n" and second_formula[4] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of first value
        return ("u")

def tet_syllogism_deduction_first_value_a(first_formula, second_formula, third_formula):
    if first_formula[0] == "a" and second_formula[1] == "n":  # calculates potential "a"-values of first value
        return ("a")
    elif first_formula[0] == "a" and third_formula[1] == "n":
        return ("a")
    elif first_formula[4] == "a" and second_formula[5] == "n":
        return ("a")
    elif first_formula[4] == "a" and third_formula[5] == "n":
        return ("a")
    elif second_formula[0] == "a" and first_formula[2] == "n":
        return ("a")
    elif second_formula[0] == "a" and third_formula[2] == "n":
        return ("a")
    elif second_formula[4] == "a" and first_formula[6] == "n":
        return ("a")
    elif second_formula[4] == "a" and third_formula[6] == "n":
        return ("a")
    elif third_formula[0] == "a" and first_formula[1] == "n":
        return ("a")
    elif third_formula[0] == "a" and second_formula[2] == "n":
        return ("a")
    elif third_formula[4] == "a" and first_formula[5] == "n":
        return ("a")
    elif third_formula[4] == "a" and second_formula[6] == "n":
        return ("a")
    else:  # calculates potential "u"-values of first value
        return ("u")

def tet_syllogism_deduction_second_value_n(first_formula, second_formula, third_formula):
    if first_formula[0] == "n" and first_formula[4] == "n":  # caluculates potential "n"-values of second value
        return ("n")
    elif second_formula[1] == "n" and second_formula[5] == "n":
        return ("n")
    elif third_formula[1] == "n" and third_formula[5] == "n":
        return ("n")

    elif first_formula[0] == "n" and second_formula[5] == "n":
        return ("n")
    elif second_formula[1] == "n" and first_formula[4] == "n":
        return ("n")

    elif first_formula[0] == "n" and third_formula[5] == "n":
        return ("n")        
    elif third_formula[1] == "n" and first_formula[4] == "n":
        return ("n")

    elif second_formula[1] == "n" and third_formula[5] == "n":
        return ("n")        
    elif third_formula[1] == "n" and second_formula[5] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of first value
        return ("u")

def tet_syllogism_deduction_second_value_a(first_formula, second_formula, third_formula):
    if first_formula[0] == "a" and second_formula[0] == "n":  # calculates potential "a"-values of second value
        return ("a")
    elif first_formula[0] == "a" and third_formula[0] == "n":
        return ("a")
    elif first_formula[4] == "a" and second_formula[4] == "n":
        return ("a")
    elif first_formula[4] == "a" and third_formula[4] == "n":
        return ("a")
    elif second_formula[1] == "a" and first_formula[2] == "n":
        return ("a")
    elif second_formula[1] == "a" and third_formula[3] == "n":
        return ("a")
    elif second_formula[5] == "a" and first_formula[6] == "n":
        return ("a")
    elif second_formula[5] == "a" and third_formula[7] == "n":
        return ("a")
    elif third_formula[1] == "a" and first_formula[1] == "n":
        return ("a")
    elif third_formula[1] == "a" and second_formula[3] == "n":
        return ("a")
    elif third_formula[5] == "a" and first_formula[5] == "n":
        return ("a")
    elif third_formula[5] == "a" and second_formula[7] == "n":
        return ("a")
    else:  # calculates potential "u"-values of second value
        return ("u")

def tet_syllogism_deduction_third_value_n(first_formula, second_formula, third_formula):
    if first_formula[1] == "n" and first_formula[5] == "n":  # caluculates potential "n"-values of third value
        return ("n")
    elif second_formula[2] == "n" and second_formula[6] == "n":
        return ("n")
    elif third_formula[0] == "n" and third_formula[4] == "n":
        return ("n")

    elif first_formula[1] == "n" and second_formula[6] == "n":
        return ("n")
    elif second_formula[2] == "n" and first_formula[5] == "n":
        return ("n")

    elif first_formula[1] == "n" and third_formula[4] == "n":
        return ("n")        
    elif third_formula[0] == "n" and first_formula[5] == "n":
        return ("n")

    elif second_formula[2] == "n" and third_formula[4] == "n":
        return ("n")        
    elif third_formula[0] == "n" and second_formula[6] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of third value
        return ("u")

def tet_syllogism_deduction_third_value_a(first_formula, second_formula, third_formula):
    if first_formula[1] == "a" and second_formula[3] == "n":  # calculates potential "a"-values of third value
        return ("a")
    elif first_formula[1] == "a" and third_formula[1] == "n":
        return ("a")
    elif first_formula[5] == "a" and second_formula[7] == "n":
        return ("a")
    elif first_formula[5] == "a" and third_formula[5] == "n":
        return ("a")
    elif second_formula[2] == "a" and first_formula[3] == "n":
        return ("a")
    elif second_formula[2] == "a" and third_formula[2] == "n":
        return ("a")
    elif second_formula[6] == "a" and first_formula[7] == "n":
        return ("a")
    elif second_formula[6] == "a" and third_formula[6] == "n":
        return ("a")
    elif third_formula[0] == "a" and first_formula[0] == "n":
        return ("a")
    elif third_formula[0] == "a" and second_formula[0] == "n":
        return ("a")
    elif third_formula[4] == "a" and first_formula[4] == "n":
        return ("a")
    elif third_formula[4] == "a" and second_formula[4] == "n":
        return ("a")
    else:  # calculates potential "u"-values of third value
        return ("u")

def tet_syllogism_deduction_fourth_value_n(first_formula, second_formula, third_formula):
    if first_formula[1] == "n" and first_formula[5] == "n":  # caluculates potential "n"-values of fourth value
        return ("n")
    elif second_formula[3] == "n" and second_formula[7] == "n":
        return ("n")
    elif third_formula[1] == "n" and third_formula[5] == "n":
        return ("n")

    elif first_formula[1] == "n" and second_formula[7] == "n":
        return ("n")
    elif second_formula[3] == "n" and first_formula[5] == "n":
        return ("n")

    elif first_formula[1] == "n" and third_formula[5] == "n":
        return ("n")        
    elif third_formula[1] == "n" and first_formula[5] == "n":
        return ("n")

    elif second_formula[3] == "n" and third_formula[5] == "n":
        return ("n")        
    elif third_formula[1] == "n" and second_formula[7] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of fourth value
        return ("u")

def tet_syllogism_deduction_fourth_value_a(first_formula, second_formula, third_formula):
    if first_formula[1] == "a" and second_formula[2] == "n":  # calculates potential "a"-values of fourth value
        return ("a")
    elif first_formula[1] == "a" and third_formula[0] == "n":
        return ("a")
    elif first_formula[5] == "a" and second_formula[6] == "n":
        return ("a")
    elif first_formula[5] == "a" and third_formula[4] == "n":
        return ("a")
    elif second_formula[3] == "a" and first_formula[3] == "n":
        return ("a")
    elif second_formula[3] == "a" and third_formula[3] == "n":
        return ("a")
    elif second_formula[7] == "a" and first_formula[7] == "n":
        return ("a")
    elif second_formula[7] == "a" and third_formula[7] == "n":
        return ("a")
    elif third_formula[1] == "a" and first_formula[0] == "n":
        return ("a")
    elif third_formula[1] == "a" and second_formula[1] == "n":
        return ("a")
    elif third_formula[5] == "a" and first_formula[4] == "n":
        return ("a")
    elif third_formula[5] == "a" and second_formula[5] == "n":
        return ("a")
    else:  # calculates potential "u"-values of fourth value
        return ("u")
    
def tet_syllogism_deduction_fifth_value_n(first_formula, second_formula, third_formula):
    if first_formula[2] == "n" and first_formula[6] == "n":  # caluculates potential "n"-values of fifth value
        return ("n")
    elif second_formula[0] == "n" and second_formula[4] == "n":
        return ("n")
    elif third_formula[2] == "n" and third_formula[6] == "n":
        return ("n")

    elif first_formula[2] == "n" and second_formula[4] == "n":
        return ("n")
    elif second_formula[0] == "n" and first_formula[6] == "n":
        return ("n")

    elif first_formula[2] == "n" and third_formula[6] == "n":
        return ("n")        
    elif third_formula[2] == "n" and first_formula[6] == "n":
        return ("n")

    elif second_formula[0] == "n" and third_formula[6] == "n":
        return ("n")        
    elif third_formula[2] == "n" and second_formula[4] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of fifth value
        return ("u")

def tet_syllogism_deduction_fifth_value_a(first_formula, second_formula, third_formula):
    if first_formula[2] == "a" and second_formula[1] == "n":  # calculates potential "a"-values of fifth value
        return ("a")
    elif first_formula[2] == "a" and third_formula[3] == "n":
        return ("a")
    elif first_formula[6] == "a" and second_formula[5] == "n":
        return ("a")
    elif first_formula[6] == "a" and third_formula[7] == "n":
        return ("a")
    elif second_formula[0] == "a" and first_formula[0] == "n":
        return ("a")
    elif second_formula[0] == "a" and third_formula[0] == "n":
        return ("a")
    elif second_formula[4] == "a" and first_formula[4] == "n":
        return ("a")
    elif second_formula[4] == "a" and third_formula[4] == "n":
        return ("a")
    elif third_formula[2] == "a" and first_formula[3] == "n":
        return ("a")
    elif third_formula[2] == "a" and second_formula[2] == "n":
        return ("a")
    elif third_formula[6] == "a" and first_formula[7] == "n":
        return ("a")
    elif third_formula[6] == "a" and second_formula[6] == "n":
        return ("a")
    else:  # calculates potential "u"-values of fifth value
        return ("u")

def tet_syllogism_deduction_sixth_value_n(first_formula, second_formula, third_formula):
    if first_formula[2] == "n" and first_formula[6] == "n":  # caluculates potential "n"-values of sixth value
        return ("n")
    elif second_formula[1] == "n" and second_formula[5] == "n":
        return ("n")
    elif third_formula[3] == "n" and third_formula[7] == "n":
        return ("n")

    elif first_formula[2] == "n" and second_formula[5] == "n":
        return ("n")
    elif second_formula[1] == "n" and first_formula[6] == "n":
        return ("n")

    elif first_formula[2] == "n" and third_formula[7] == "n":
        return ("n")        
    elif third_formula[3] == "n" and first_formula[6] == "n":
        return ("n")

    elif second_formula[1] == "n" and third_formula[7] == "n":
        return ("n")        
    elif third_formula[3] == "n" and second_formula[5] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of sixth value
        return ("u")

def tet_syllogism_deduction_sixth_value_a(first_formula, second_formula, third_formula):
    if first_formula[2] == "a" and second_formula[0] == "n":  # calculates potential "a"-values of sixth value
        return ("a")
    elif first_formula[2] == "a" and third_formula[2] == "n":
        return ("a")
    elif first_formula[6] == "a" and second_formula[4] == "n":
        return ("a")
    elif first_formula[6] == "a" and third_formula[6] == "n":
        return ("a")
    elif second_formula[1] == "a" and first_formula[0] == "n":
        return ("a")
    elif second_formula[1] == "a" and third_formula[1] == "n":
        return ("a")
    elif second_formula[5] == "a" and first_formula[4] == "n":
        return ("a")
    elif second_formula[5] == "a" and third_formula[5] == "n":
        return ("a")
    elif third_formula[3] == "a" and first_formula[3] == "n":
        return ("a")
    elif third_formula[3] == "a" and second_formula[3] == "n":
        return ("a")
    elif third_formula[7] == "a" and first_formula[7] == "n":
        return ("a")
    elif third_formula[7] == "a" and second_formula[7] == "n":
        return ("a")
    else:  # calculates potential "u"-values of sixth value
        return ("u")
    
def tet_syllogism_deduction_seventh_value_n(first_formula, second_formula, third_formula):
    if first_formula[3] == "n" and first_formula[7] == "n":  # caluculates potential "n"-values of seventh value
        return ("n")
    elif second_formula[2] == "n" and second_formula[6] == "n":
        return ("n")
    elif third_formula[2] == "n" and third_formula[6] == "n":
        return ("n")

    elif first_formula[3] == "n" and second_formula[6] == "n":
        return ("n")
    elif second_formula[2] == "n" and first_formula[7] == "n":
        return ("n")

    elif first_formula[3] == "n" and third_formula[6] == "n":
        return ("n")        
    elif third_formula[2] == "n" and first_formula[7] == "n":
        return ("n")

    elif second_formula[2] == "n" and third_formula[6] == "n":
        return ("n")        
    elif third_formula[2] == "n" and second_formula[6] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of seventh value
        return ("u")

def tet_syllogism_deduction_seventh_value_a(first_formula, second_formula, third_formula):
    if first_formula[3] == "a" and second_formula[3] == "n":  # calculates potential "a"-values of seventh value
        return ("a")
    elif first_formula[3] == "a" and third_formula[3] == "n":
        return ("a")
    elif first_formula[7] == "a" and second_formula[7] == "n":
        return ("a")
    elif first_formula[7] == "a" and third_formula[7] == "n":
        return ("a")
    elif second_formula[2] == "a" and first_formula[1] == "n":
        return ("a")
    elif second_formula[2] == "a" and third_formula[0] == "n":
        return ("a")
    elif second_formula[6] == "a" and first_formula[5] == "n":
        return ("a")
    elif second_formula[6] == "a" and third_formula[4] == "n":
        return ("a")
    elif third_formula[2] == "a" and first_formula[2] == "n":
        return ("a")
    elif third_formula[2] == "a" and second_formula[0] == "n":
        return ("a")
    elif third_formula[6] == "a" and first_formula[6] == "n":
        return ("a")
    elif third_formula[6] == "a" and second_formula[4] == "n":
        return ("a")
    else:  # calculates potential "u"-values of seventh value
        return ("u")

def tet_syllogism_deduction_eighth_value_n(first_formula, second_formula, third_formula):
    if first_formula[3] == "n" and first_formula[7] == "n":  # caluculates potential "n"-values of eighth value
        return ("n")
    elif second_formula[3] == "n" and second_formula[7] == "n":
        return ("n")
    elif third_formula[3] == "n" and third_formula[7] == "n":
        return ("n")

    elif first_formula[3] == "n" and second_formula[7] == "n":
        return ("n")
    elif second_formula[3] == "n" and first_formula[7] == "n":
        return ("n")

    elif first_formula[3] == "n" and third_formula[7] == "n":
        return ("n")        
    elif third_formula[3] == "n" and first_formula[7] == "n":
        return ("n")

    elif second_formula[3] == "n" and third_formula[7] == "n":
        return ("n")        
    elif third_formula[3] == "n" and second_formula[7] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of eighth value
        return ("u")

def tet_syllogism_deduction_eighth_value_a(first_formula, second_formula, third_formula):
    if first_formula[3] == "a" and second_formula[2] == "n":  # calculates potential "a"-values of eighth value
        return ("a")
    elif first_formula[3] == "a" and third_formula[2] == "n":
        return ("a")
    elif first_formula[7] == "a" and second_formula[6] == "n":
        return ("a")
    elif first_formula[7] == "a" and third_formula[6] == "n":
        return ("a")
    elif second_formula[3] == "a" and first_formula[1] == "n":
        return ("a")
    elif second_formula[3] == "a" and third_formula[1] == "n":
        return ("a")
    elif second_formula[7] == "a" and first_formula[5] == "n":
        return ("a")
    elif second_formula[7] == "a" and third_formula[5] == "n":
        return ("a")
    elif third_formula[3] == "a" and first_formula[2] == "n":
        return ("a")
    elif third_formula[3] == "a" and second_formula[1] == "n":
        return ("a")
    elif third_formula[7] == "a" and first_formula[6] == "n":
        return ("a")
    elif third_formula[7] == "a" and second_formula[5] == "n":
        return ("a")
    else:  # calculates potential "u"-values of eighth value
        return ("u")

def syllogism_contradiction_test_tet(first_formula, second_formula, third_formula):

    conclusion = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    conclusion[0] = tet_syllogism_deduction_first_value_n(first_formula, second_formula, third_formula)
    conclusion[1] = tet_syllogism_deduction_first_value_a(first_formula, second_formula, third_formula)
    if conclusion[0] == 'n' and conclusion[1] == 'a':
        return ('W')
    conclusion[2] = tet_syllogism_deduction_second_value_n(first_formula, second_formula, third_formula)
    conclusion[3] = tet_syllogism_deduction_second_value_a(first_formula, second_formula, third_formula)
    if conclusion[2] == 'n' and conclusion[3] == 'a':
        return ('W')
    conclusion[4] = tet_syllogism_deduction_third_value_n(first_formula, second_formula, third_formula)
    conclusion[5] = tet_syllogism_deduction_third_value_a(first_formula, second_formula, third_formula)
    if conclusion[4] == 'n' and conclusion[5] == 'a':
        return ('W')
    conclusion[6] = tet_syllogism_deduction_fourth_value_n(first_formula, second_formula, third_formula)
    conclusion[7] = tet_syllogism_deduction_fourth_value_a(first_formula, second_formula, third_formula)
    if conclusion[6] == 'n' and conclusion[7] == 'a':
        return ('W')
    conclusion[8] = tet_syllogism_deduction_fifth_value_n(first_formula, second_formula, third_formula)
    conclusion[9] = tet_syllogism_deduction_fifth_value_a(first_formula, second_formula, third_formula)
    if conclusion[8] == 'n' and conclusion[9] == 'a':
        return ('W')
    conclusion[10] = tet_syllogism_deduction_sixth_value_n(first_formula, second_formula, third_formula)
    conclusion[11] = tet_syllogism_deduction_sixth_value_a(first_formula, second_formula, third_formula)
    if conclusion[10] == 'n' and conclusion[11] == 'a':
        return ('W')
    conclusion[12] = tet_syllogism_deduction_seventh_value_n(first_formula, second_formula, third_formula)
    conclusion[13] = tet_syllogism_deduction_seventh_value_a(first_formula, second_formula, third_formula)
    if conclusion[12] == 'n' and conclusion[13] == 'a':
        return ('W')
    conclusion[14] = tet_syllogism_deduction_eighth_value_n(first_formula, second_formula, third_formula)
    conclusion[15] = tet_syllogism_deduction_eighth_value_a(first_formula, second_formula, third_formula)
    if conclusion[14] == 'n' and conclusion[15] == 'a':
        return ('W')

    conclusion_solution = [0,0,0,0,0,0,0,0]
        
    for i in range(8):

        if conclusion_solution[i] == 0 or conclusion_solution[i] == 'u':

            if conclusion[2*i] == 'a':
                conclusion_solution[i] = 'a'
            elif conclusion[2*i] == 'n':
                conclusion_solution[i] = 'n'
            elif conclusion[2*i+1] == 'a':
                conclusion_solution[i] = 'a'
            elif conclusion[2*i+1] == 'n':
                conclusion_solution[i] = 'n'
            else:
                conclusion_solution[i] = 'u'
        
    return (conclusion_solution, 'kW')

def triadic_name_fn( formula, index_premis_circumstance):
    
    list_formulas_names = [[['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 1']],\
                            [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 2']],\
                            [['a', 'a', 'a', 'n', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 3']],\
                            [['a', 'a', 'a', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\cup D, 1A, 5A$']],\
                            [['a', 'a', 'a', 'a', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 5']],\
                            [['a', 'a', 'a', 'a', 'a', 'n', 'a', 'n'], ['$B\\cup C, C\\cup D, B\\sqcup D, 1A, 3A$']],\
                            [['a', 'a', 'a', 'n', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 7']],\
                            [['a', 'a', 'a', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\sqcup D, 1A$']],\
                            [['a', 'n', 'a', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 9']],\
                            [['a', 'n', 'a', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 10']],\
                            [['a', 'n', 'a', 'n', 'a', 'a', 'a', 'a'], ['$B\\cup C, C\\cup D, B\\subset D, 5A, 7A$']],\
                            [['a', 'n', 'a', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\subset D, 5A$']],\
                            [['a', 'n', 'a', 'a', 'a', 'n', 'a', 'a'], ['$B\\subset C, C\\cup D, B\\cup D, 3A, 7A$']],\
                            [['a', 'n', 'a', 'a', 'a', 'n', 'a', 'n'], ['$B\\subset C, C\\cup D, B\\sqcup D, 3A$']],\
                            [['a', 'n', 'a', 'n', 'a', 'n', 'a', 'a'], ['$B\\subset C, C\\cup D, B\\subset D, 7A$']],\
                            [['a', 'n', 'a', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqsubset C, C\\cup D, B\\sqsubset D$']],\
                            [['a', 'a', 'a', 'a', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 17']],\
                            [['a', 'a', 'a', 'a', 'a', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\cup D, 1A, 2A$']],\
                            [['a', 'a', 'a', 'n', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 19']],\
                            [['a', 'a', 'a', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\cup D, 1A$']],\
                            [['a', 'a', 'a', 'a', 'a', 'n', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 21']],\
                            [['a', 'a', 'a', 'a', 'a', 'n', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\sqcup D, 1A$']],\
                            [['a', 'a', 'a', 'n', 'a', 'n', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 23']],\
                            [['a', 'a', 'a', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\sqcup D, 1A$']],\
                            [['a', 'n', 'a', 'a', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 25']],\
                            [['a', 'n', 'a', 'a', 'a', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\cup D, 1A, 2N$']],\
                            [['a', 'n', 'a', 'n', 'a', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\subset D, 5A, 7N$']],\
                            [['a', 'n', 'a', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\subset D$']],\
                            [['a', 'n', 'a', 'a', 'a', 'n', 'n', 'a'], ['$B\\subset C, C\\cup D, B\\cup D, 3A, 7N$']],\
                            [['a', 'n', 'a', 'a', 'a', 'n', 'n', 'n'], ['$B\\subset C, C\\sqcup D, B\\sqcup D$']],\
                            [['a', 'n', 'a', 'n', 'a', 'n', 'n', 'a'], ['$B\\subset C, C\\cup D, B\\subset D, 7N$']],\
                            [['a', 'n', 'a', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqsubset C, C\\sqcup D, B\\sqsubset D$']],\
                            [['a', 'a', 'n', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 33']],\
                            [['a', 'a', 'n', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 34']],\
                            [['a', 'a', 'n', 'n', 'a', 'a', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\cup D, 5A, 6A$']],\
                            [['a', 'a', 'n', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\cup D, 5A$']],\
                            [['a', 'a', 'n', 'a', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 37']],\
                            [['a', 'a', 'n', 'a', 'a', 'n', 'a', 'n'], ['$B\\cup C, C\\cup D, B\\sqcup D, 1A, 3N$']],\
                            [['a', 'a', 'n', 'n', 'a', 'n', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\cup D, 5A, 6N$']],\
                            [['a', 'a', 'n', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\sqcup D$']],\
                            [['a', 'n', 'n', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 41']],\
                            [['a', 'n', 'n', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 42']],\
                            [['a', 'n', 'n', 'n', 'a', 'a', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\subset D, 5A$']],\
                            [['a', 'n', 'n', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\subset D, 5A$']],\
                            [['a', 'n', 'n', 'a', 'a', 'n', 'a', 'a'], ['$B\\subset C, C\\cup D, B\\cup D, 3N, 7A$']],\
                            [['a', 'n', 'n', 'a', 'a', 'n', 'a', 'n'], ['$B\\subset C, C\\cup D, B\\sqcup D, 3N$']],\
                            [['a', 'n', 'n', 'n', 'a', 'n', 'a', 'a'], ['$B\\subset C, C\\subset D, B\\subset D$']],\
                            [['a', 'n', 'n', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqsubset C, C\\subset D, B\\sqsubset D$']],\
                            [['a', 'a', 'n', 'a', 'a', 'a', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\cup D, 2A, 6A$']],\
                            [['a', 'a', 'n', 'a', 'a', 'a', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\cup D, 2A$']],\
                            [['a', 'a', 'n', 'n', 'a', 'a', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\cup D, 6A$']],\
                            [['a', 'a', 'n', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\cup D$']],\
                            [['a', 'a', 'n', 'a', 'a', 'n', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\cup D, 2A, 6N$']],\
                            [['a', 'a', 'n', 'a', 'a', 'n', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\sqcup D$']],\
                            [['a', 'a', 'n', 'n', 'a', 'n', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\cup D, 6N$']],\
                            [['a', 'a', 'n', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\sqcup D$']],\
                            [['a', 'n', 'n', 'a', 'a', 'a', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\cup D, 2N, 6A$']],\
                            [['a', 'n', 'n', 'a', 'a', 'a', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\cup D, 2N$']],\
                            [['a', 'n', 'n', 'n', 'a', 'a', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\subset D$']],\
                            [['a', 'n', 'n', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\subset D$']],\
                            [['a', 'n', 'n', 'a', 'a', 'n', 'n', 'a'], ['$B\\cap C, C\\cup D, B\\cup D$']],\
                            [['a', 'n', 'n', 'a', 'a', 'n', 'n', 'n'], ['$B\\cap C, C\\sqcup D, B\\sqcup D$']],\
                            [['a', 'n', 'n', 'n', 'a', 'n', 'n', 'a'], ['$B\\cap C, C\\subset D, B\\subset D$']],\
                            [['a', 'n', 'n', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqcap C, C\\sqsubset D, B\\sqsubset D$']],\
                            [['a', 'a', 'a', 'a', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 65']],\
                            [['a', 'a', 'a', 'a', 'n', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 66']],\
                            [['a', 'a', 'a', 'n', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 67']],\
                            [['a', 'a', 'a', 'n', 'n', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\cup D, 1A, 5N$']],\
                            [['a', 'a', 'a', 'a', 'n', 'n', 'a', 'a'], ['$B\\cup C, C\\supset D, B\\cup D, 3A, 4A$']],\
                            [['a', 'a', 'a', 'a', 'n', 'n', 'a', 'n'], ['$B\\cup C, C\\supset D, B\\sqcup D, 3A$']],\
                            [['a', 'a', 'a', 'n', 'n', 'n', 'a', 'a'], ['$B\\cup C, C\\supset D, B\\cup D, 3A, 4N$']],\
                            [['a', 'a', 'a', 'n', 'n', 'n', 'a', 'n'], ['$B\\sqcup C, C\\supset D, B\\sqcup D$']],\
                            [['a', 'n', 'a', 'a', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 73']],\
                            [['a', 'n', 'a', 'a', 'n', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 74']],\
                            [['a', 'n', 'a', 'n', 'n', 'a', 'a', 'a'], ['$B\\cup C, C\\cup D, B\\subset D, 5N, 7A$']],\
                            [['a', 'n', 'a', 'n', 'n', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\subset D, 5N$']],\
                            [['a', 'n', 'a', 'a', 'n', 'n', 'a', 'a'], ['$B\\subset C, C\\supset D, B\\cup D, 3A$']],\
                            [['a', 'n', 'a', 'a', 'n', 'n', 'a', 'n'], ['$B\\subset C, C\\supset D, B\\sqcup D, 3A$']],\
                            [['a', 'n', 'a', 'n', 'n', 'n', 'a', 'a'], ['$B\\subset C, C\\supset D, B\\subset D$']],\
                            [['a', 'n', 'a', 'n', 'n', 'n', 'a', 'n'], ['$B\\sqsubset C, C\\supset D, B\\sqsubset D$']],\
                            [['a', 'a', 'a', 'a', 'n', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\supset D, 2A, 4A$']],\
                            [['a', 'a', 'a', 'a', 'n', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\supset D, 2A$']],\
                            [['a', 'a', 'a', 'n', 'n', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\supset D, 2A, 4N$']],\
                            [['a', 'a', 'a', 'n', 'n', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\supset D$']],\
                            [['a', 'a', 'a', 'a', 'n', 'n', 'n', 'a'], ['$B\\cup C, C\\supset D, B\\supset D, 4A$']],\
                            [['a', 'a', 'a', 'a', 'n', 'n', 'n', 'n'], ['$B\\cup C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'a', 'a', 'n', 'n', 'n', 'n', 'a'], ['$B\\cup C, C\\supset D, B\\supset D, 4N$']],\
                            [['a', 'a', 'a', 'n', 'n', 'n', 'n', 'n'], ['$B\\sqcup C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'n', 'a', 'a', 'n', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\supset D, 2N, 4A$']],\
                            [['a', 'n', 'a', 'a', 'n', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\supset D, 2N$']],\
                            [['a', 'n', 'a', 'n', 'n', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\cap D$']],\
                            [['a', 'n', 'a', 'n', 'n', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\cap D$']],\
                            [['a', 'n', 'a', 'a', 'n', 'n', 'n', 'a'], ['$B\\subset C, C\\supset D, B\\supset D$']],\
                            [['a', 'n', 'a', 'a', 'n', 'n', 'n', 'n'], ['$B\\subset C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'n', 'a', 'n', 'n', 'n', 'n', 'a'], ['$B\\subset C, C\\supset D, B\\cap D$']],\
                            [['a', 'n', 'a', 'n', 'n', 'n', 'n', 'n'], ['$B\\sqsubset C, C\\sqsupset D, B\\sqcap D$']],\
                            [['a', 'a', 'n', 'a', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 97']],\
                            [['a', 'a', 'n', 'a', 'n', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 98']],\
                            [['a', 'a', 'n', 'n', 'n', 'a', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\cup D, 5N, 6A$']],\
                            [['a', 'a', 'n', 'n', 'n', 'a', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\cup D, 5N$']],\
                            [['a', 'a', 'n', 'a', 'n', 'n', 'a', 'a'], ['$B\\cup C, C\\supset D, B\\cup D, 3N, 4A$']],\
                            [['a', 'a', 'n', 'a', 'n', 'n', 'a', 'n'], ['$B\\cup C, C\\supset D, B\\sqcup D, 3N$']],\
                            [['a', 'a', 'n', 'n', 'n', 'n', 'a', 'a'], ['$B\\cup C, C\\cap D, B\\cup D$']],\
                            [['a', 'a', 'n', 'n', 'n', 'n', 'a', 'n'], ['$B\\sqcup C, C\\cap D, B\\sqcup D$']],\
                            [['a', 'n', 'n', 'a', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 105']],\
                            [['a', 'n', 'n', 'a', 'n', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 106']],\
                            [['a', 'n', 'n', 'n', 'n', 'a', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\subset D, 5N$']],\
                            [['a', 'n', 'n', 'n', 'n', 'a', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\subset D, 5N$']],\
                            [['a', 'n', 'n', 'a', 'n', 'n', 'a', 'a'], ['$B\\subset C, C\\supset D, B\\cup D, 3N$']],\
                            [['a', 'n', 'n', 'a', 'n', 'n', 'a', 'n'], ['$B\\subset C, C\\supset D, B\\sqcup D, 3N$']],\
                            [['a', 'n', 'n', 'n', 'n', 'n', 'a', 'a'], ['$B\\subset C, C\\cap D, B\\subset D$']],\
                            [['a', 'n', 'n', 'n', 'n', 'n', 'a', 'n'], ['$B\\sqsubset C, C\\cap D, B\\sqsubset D$']],\
                            [['a', 'a', 'n', 'a', 'n', 'a', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\supset D, 2A$']],\
                            [['a', 'a', 'n', 'a', 'n', 'a', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\supset D, 2A$']],\
                            [['a', 'a', 'n', 'n', 'n', 'a', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\supset D$']],\
                            [['a', 'a', 'n', 'n', 'n', 'a', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\supset D$']],\
                            [['a', 'a', 'n', 'a', 'n', 'n', 'n', 'a'], ['$B\\supset C, C\\supset D, B\\supset D$']],\
                            [['a', 'a', 'n', 'a', 'n', 'n', 'n', 'n'], ['$B\\supset C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'a', 'n', 'n', 'n', 'n', 'n', 'a'], ['$B\\supset C, C\\cap D, B\\supset D$']],\
                            [['a', 'a', 'n', 'n', 'n', 'n', 'n', 'n'], ['$B\\sqsupset C, C\\sqcap D, B\\sqsupset D$']],\
                            [['a', 'n', 'n', 'a', 'n', 'a', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\supset D, 2N$']],\
                            [['a', 'n', 'n', 'a', 'n', 'a', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\supset D, 2N$']],\
                            [['a', 'n', 'n', 'n', 'n', 'a', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\cap D$']],\
                            [['a', 'n', 'n', 'n', 'n', 'a', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\cap D$']],\
                            [['a', 'n', 'n', 'a', 'n', 'n', 'n', 'a'], ['$B\\cap C, C\\supset D, B\\supset D$']],\
                            [['a', 'n', 'n', 'a', 'n', 'n', 'n', 'n'], ['$B\\cap C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'n', 'n', 'n', 'n', 'n', 'n', 'a'], ['$B\\cap C, C\\cap D, B\\cap D$']],\
                            [['a', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], ['$B\\sqcap C, C\\sqcap D, B\\sqcap D$']],\
                            [['n', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 129']],\
                            [['n', 'a', 'a', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 130']],\
                            [['n', 'a', 'a', 'n', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 131']],\
                            [['n', 'a', 'a', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\cup D, 1N, 5A$']],\
                            [['n', 'a', 'a', 'a', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 133']],\
                            [['n', 'a', 'a', 'a', 'a', 'n', 'a', 'n'], ['$B\\cup C, C\\cup D, B\\sqcup D, 1N, 3A$']],\
                            [['n', 'a', 'a', 'n', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 135']],\
                            [['n', 'a', 'a', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\sqcup D, 1N$']],\
                            [['n', 'n', 'a', 'a', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\cup D, 7A, 8A$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'a', 'a', 'n'], ["$B\\cup C, C\\sqcap 'D, B\\cup D, 7A, 8N$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\subset D, 7A$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'a', 'a', 'n'], ["$B\\sqcup C, C\\sqcap 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'n', 'a', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\cup D, 7A$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'n', 'a', 'n'], ["$B\\subset C, C\\sqcap 'D, B\\sqcup D$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'n', 'a', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\subset D, 7A$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'n', 'a', 'n'], ["$B\\sqsubset C, C\\sqcap 'D, B\\sqsubset D$"]],\
                            [['n', 'a', 'a', 'a', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 145']],\
                            [['n', 'a', 'a', 'a', 'a', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\cup D, 1N, 2A$']],\
                            [['n', 'a', 'a', 'n', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 147']],\
                            [['n', 'a', 'a', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\cup D, 1N$']],\
                            [['n', 'a', 'a', 'a', 'a', 'n', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 149']],\
                            [['n', 'a', 'a', 'a', 'a', 'n', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\sqcup D, 1N$']],\
                            [['n', 'a', 'a', 'n', 'a', 'n', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 151']],\
                            [['n', 'a', 'a', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\sqcup D, 1N$']],\
                            [['n', 'n', 'a', 'a', 'a', 'a', 'n', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\cup D, 7N, 8A$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'a', 'n', 'n'], ["$B\\cup C, C\\cap 'D, B\\cup D$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'a', 'n', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\subset D, 7N$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'a', 'n', 'n'], ["$B\\sqcup C, C\\cap 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'n', 'n', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\cup D, 7N$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'n', 'n', 'n'], ["$B\\subset C, C\\cap 'D, B\\sqcup D$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'n', 'n', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\subset D, 7N$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'n', 'n', 'n'], ["$B\\sqsubset C, C\\cap 'D, B\\sqsubset D$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\cup D, B\\sqcap 'D, 6A, 8A$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'a', 'a', 'n'], ["$B\\cup C, C\\cup D, B\\sqcap 'D, 6A, 8N$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\subset D, B\\sqcap 'D, 6A$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'a', 'a', 'n'], ["$B\\sqcup C, C\\subset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'n', 'a', 'a'], ["$B\\cup C, C\\cup D, B\\sqcap 'D, 6N, 8A$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'n', 'a', 'n'], ["$B\\cup C, C\\cup D, B\\cap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'n', 'a', 'a'], ["$B\\cup C, C\\subset D, B\\sqcap 'D, 6N$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'n', 'a', 'n'], ["$B\\sqcup C, C\\subset D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\sqcap 'D, 8A$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'a', 'a', 'n'], ["$B\\cup C, C\\sqcap 'D, B\\sqcap 'D, 8N$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'a', 'a', 'n'], ["$B\\sqcup C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'n', 'a', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'n', 'a', 'n'], ["$B\\subset C, C\\sqcap 'D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'n', 'a', 'a'], ["$B\\subset C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'n', 'a', 'n'], ["$B\\sqsubset C, C\\sqsupset 'D, B\\supset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'a', 'n', 'a'], ["$B\\supset C, C\\cup D, B\\sqcap 'D, 6A$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'a', 'n', 'n'], ["$B\\supset C, C\\sqcup D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'a', 'n', 'a'], ["$B\\supset C, C\\subset D, B\\sqcap 'D, 6A$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'a', 'n', 'n'], ["$B\\sqsupset C, C\\sqsubset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'n', 'n', 'a'], ["$B\\supset C, C\\cup D, B\\sqcap 'D, 6N$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'n', 'n', 'n'], ["$B\\supset C, C\\sqcup D, B\\cap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'n', 'n', 'a'], ["$B\\supset C, C\\subset D, B\\sqcap 'D, 6N$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'n', 'n', 'n'], ["$B\\sqsupset C, C\\sqsubset D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'a', 'n', 'a'], ["$B\\supset C, C\\sqcap 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'a', 'n', 'n'], ["$B\\supset C, C\\cap 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'a', 'n', 'a'], ["$B\\supset C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'a', 'n', 'n'], ["$B\\sqsupset C, C\\supset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'n', 'n', 'a'], ["$B\\cap C, C\\sqcap 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'n', 'n', 'n'], ["$B\\cap C, C\\cap 'D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'n', 'n', 'a'], ["$B\\cap C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'n', 'n', 'n'], ["$B\\sqcap C, C\\supset 'D, B\\supset 'D$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\cup D, 4A, 8A$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'a', 'a', 'n'], ["$B\\sqcap 'C, C\\cup D, B\\cup D, 4A, 8N$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\cup D, 4N, 8A$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'a', 'a', 'n'], ["$B\\cap 'C, C\\cup D, B\\cup D$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'n', 'a', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\cup D, 4A$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'n', 'a', 'n'], ["$B\\sqcap 'C, C\\supset D, B\\sqcup D$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'n', 'a', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\cup D, 4N$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'n', 'a', 'n'], ["$B\\cap 'C, C\\supset D, B\\sqcup D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\cup D, 8A$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'a', 'a', 'n'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\cup D, 8N$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'a', 'a', 'n'], ["$B\\cap 'C, C\\sqcap 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'n', 'a', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\cup D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'n', 'a', 'n'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\sqcup D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'n', 'a', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'n', 'a', 'n'], ["$B\\supset 'C, C\\sqsubset 'D, B\\sqsubset D$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'a', 'n', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\supset D, 4A$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'a', 'n', 'n'], ["$B\\sqcap 'C, C\\sqcup D, B\\supset D$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'a', 'n', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\supset D, 4N$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'a', 'n', 'n'], ["$B\\cap 'C, C\\sqcup D, B\\supset D$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'n', 'n', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\supset D, 4A$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'n', 'n', 'n'], ["$B\\sqcap 'C, C\\sqsupset D, B\\sqsupset D$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'n', 'n', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\supset D, 4N$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'n', 'n', 'n'], ["$B\\cap 'C, C\\sqsupset D, B\\sqsupset D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'a', 'n', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\supset D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'a', 'n', 'n'], ["$B\\sqcap 'C, C\\cap 'D, B\\supset D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'a', 'n', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\cap D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'a', 'n', 'n'], ["$B\\cap 'C, C\\cap 'D, B\\cap D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'n', 'n', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\supset D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'n', 'n', 'n'], ["$B\\sqsupset 'C, C\\subset 'D, B\\sqsupset D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'n', 'n', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\cap D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'n', 'n', 'n'], ["$B\\supset 'C, C\\subset 'D, B\\sqcap D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\sqcap 'D, 8A$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'a', 'a', 'n'], ["$B\\sqcap 'C, C\\cup D, B\\sqcap 'D, 8N$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\subset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'a', 'a', 'n'], ["$B\\cap' C, C\\subset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'n', 'a', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'n', 'a', 'n'], ["$B\\sqcap 'C, C\\supset D, B\\cap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'n', 'a', 'a'], ["$B\\sqcap 'C, C\\cap D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'n', 'a', 'n'], ["$B\\cap 'C, C\\cap D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D B\\sqcap 'D, 8A$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'a', 'a', 'n'], ["$B\\sqcap 'C, C\\sqcap 'D B\\sqcap 'D, 8N$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'a', 'a', 'n'], ["$B\\cap 'C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'n', 'a', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'n', 'a', 'n'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'n', 'a', 'a'], ["$B\\sqsupset 'C, C\\sqcup 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'n', 'a', 'n'], ["$B\\supset 'C, C\\sqcup 'D, B\\supset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'a', 'n', 'a'], ["$B\\sqsubset 'C, C\\cup D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'a', 'n', 'n'], ["$B\\sqsubset 'C, C\\sqcup D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'a', 'n', 'a'], ["$B\\sqsubset 'C, C\\subset D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'a', 'n', 'n'], ["$B\\subset 'C, C\\sqsubset D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'n', 'n', 'a'], ["$B\\sqsubset 'C, C\\supset D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'n', 'n', 'n'], ["$B\\sqsubset 'C, C\\sqsupset D, B\\subset 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'n', 'n', 'a'], ["$B\\sqsubset 'C, C\\cap D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'n', 'n', 'n'], ["$B\\subset 'C, C\\sqcap D, B\\subset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'a', 'n', 'a'], ["$B\\sqsubset 'C, C\\sqcap 'D, B\\sqsubset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'a', 'n', 'n'], ["$B\\sqsubset 'C, C\\cap 'D, B\\sqsubset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'a', 'n', 'a'], ["$B\\sqsubset 'C, C\\sqsupset 'D, B\\sqcup 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'a', 'n', 'n'], ["$B\\subset 'C, C\\supset 'D, B\\sqcup 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'n', 'n', 'a'], ["$B\\sqcup 'C, C\\sqsubset 'D, B\\sqsubset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'n', 'n', 'n'], ["$B\\sqcup 'C, C\\subset 'D, B\\subset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'a'], ["$B\\sqcup 'C, C\\sqcup 'D, B\\sqcup 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], ["$B\\cup 'C, C\\cup 'D, B\\cup 'D$"]]]

    for formulas_names in list_formulas_names:
        if formulas_names[0] == formula:
            #print(formula_list_name[0])
            if index_premis_circumstance == 2:
                new_formula_A = formulas_names[1][0][:].replace("B", "X")
                new_formula_2 = new_formula_A.replace("D", "E")
                new_formula_3 = new_formula_2.replace("C", "D")
                new_formula_4 = new_formula_3.replace("X", "C")
                return [new_formula_4]
            #"$C$\textbullet$D$\textbullet$E$"
            elif index_premis_circumstance == 1:
                new_formula_B = formulas_names[1][0][:].replace("D", "E")
                return [new_formula_B]
            #"$B$\textbullet$C$\textbullet$E$"
            elif index_premis_circumstance == 3:
                new_formula_C = formulas_names[1][0][:].replace("D", "E")
                new_formula_2 = new_formula_C.replace("C", "D")
                return [new_formula_2]
            #"$B$\textbullet$D$\textbullet$E$"
            elif index_premis_circumstance == 4:
                return [formulas_names[1][0]]
            #"$B$\textbullet$C$\textbullet$D$"


                                        
def deduction_of_tetradic_total_formulas_from_triadic_level( *args):
    #~4 billion Possibilitys from triadic possibilitys to tetradic possibilitys:
    #21 places = 12 sec
    #22 places = 24 sec
    #32 places = 6.8 h (calculated approximatly)
    #BEGIN: 2025-02-06 22:46:15.554045
    #END: 2025-02-07 05:24:23.855997

    list_syllogism_total_formulas = [[['a', 'a', 'u', 'u', 'n', 'n', 'a', 'a'], 'MP'] ,\
                                    [['n', 'n', 'a', 'a', 'a', 'a', 'u', 'u'], 'MP'] ,\
                                    [['a', 'a', 'u', 'u', 'u', 'u', 'u', 'u'], 'MP'] ,\
                                    [['u', 'u', 'u', 'u', 'a', 'a', 'u', 'u'], 'MP'] ,\
                                    [['a', 'a', 'n', 'n', 'u', 'u', 'a', 'a'], 'MP'] ,\
                                    [['u', 'u', 'a', 'a', 'a', 'a', 'n', 'n'], 'MP'] ,\
                                    [['u', 'u', 'u', 'u', 'u', 'u', 'a', 'a'], 'MP'] ,\
                                    [['u', 'u', 'a', 'a', 'u', 'u', 'u', 'u'], 'MP'] ,\
                                    [['a', 'u', 'n', 'a', 'a', 'u', 'n', 'a'], 'SM'] ,\
                                    [['n', 'a', 'a', 'u', 'n', 'a', 'a', 'u'], 'SM'] ,\
                                    [['a', 'u', 'u', 'u', 'a', 'u', 'u', 'u'], 'SM'] ,\
                                    [['u', 'u', 'a', 'u', 'u', 'u', 'a', 'u'], 'SM'] ,\
                                    [['a', 'n', 'u', 'a', 'a', 'n', 'u', 'a'], 'SM'] ,\
                                    [['u', 'a', 'a', 'n', 'u', 'a', 'a', 'n'], 'SM'] ,\
                                    [['u', 'u', 'u', 'a', 'u', 'u', 'u', 'a'], 'SM'] ,\
                                    [['u', 'a', 'u', 'u', 'u', 'a', 'u', 'u'], 'SM'] ,\
                                    [['a', 'u', 'a', 'u', 'n', 'a', 'n', 'a'], 'SP'] ,\
                                    [['n', 'a', 'n', 'a', 'a', 'u', 'a', 'u'], 'SP'] ,\
                                    [['a', 'u', 'a', 'u', 'u', 'u', 'u', 'u'], 'SP'] ,\
                                    [['u', 'u', 'u', 'u', 'a', 'u', 'a', 'u'], 'SP'] ,\
                                    [['a', 'n', 'a', 'n', 'u', 'a', 'u', 'a'], 'SP'] ,\
                                    [['u', 'a', 'u', 'a', 'a', 'n', 'a', 'n'], 'SP'] ,\
                                    [['u', 'u', 'u', 'u', 'u', 'a', 'u', 'a'], 'SP'] ,\
                                    [['u', 'a', 'u', 'a', 'u', 'u', 'u', 'u'], 'SP']]
    
    list_syllogistik_ganzformeln = [[['a', 'u', 'n', 'u', 'n', 'n', 'n', 'a'], ['$MaP$', '$SaM$', '$SaP$']],\
[['n', 'a', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$SeM$', '$S\\tilde{o}P$']],\
[['a', 'u', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$SiM$', '$SiP$']],\
[['a', 'n', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$S\\tilde{a}M$', '$SiP$']],\
[['u', 'a', 'u', 'n', 'n', 'n', 'a', 'n'], ['$MaP$', '$S\\ddot{e}M$', '$SS\\ddot{e}P$']],\
[['u', 'a', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$S\\tilde{o}M$', '$S\\tilde{o}P$']],\
[['n', 'n', 'n', 'a', 'a', 'u', 'n', 'u'], ['$MeP$', '$SaM$', '$SeP$']],\
[['n', 'n', 'u', 'u', 'n', 'a', 'u', 'u'], ['$MeP$', '$SeM$', '$S\\ddot{\\imath}P$']],\
[['n', 'n', 'u', 'u', 'a', 'u', 'u', 'u'], ['$MeP$', '$SiM$', '$SoP$']],\
[['n', 'n', 'u', 'u', 'a', 'n', 'u', 'u'], ['$MeP$', '$S\\tilde{a}M$', '$SoP$']],\
[['n', 'n', 'a', 'n', 'u', 'a', 'u', 'n'], ['$MeP$', '$S\\ddot{e}M$', '$S\\tilde{a}P$']],\
[['n', 'n', 'u', 'u', 'u', 'a', 'u', 'u'], ['$MeP$', '$S\\tilde{o}M$', '$S\\ddot{\\imath}P$']],\
[['n', 'a', 'u', 'u', 'n', 'u', 'u', 'u'], ['$MiP$', '$SeM$', '$S\\tilde{o}P$']],\
[['a', 'n', 'u', 'u', 'u', 'n', 'u', 'u'], ['$MiP$', '$S\\tilde{a}M$', '$SiP$']],\
[['n', 'u', 'u', 'u', 'n', 'a', 'u', 'u'], ['$MoP$', '$SeM$', '$S\\ddot{\\imath}P$']],\
[['u', 'n', 'u', 'u', 'a', 'n', 'u', 'u'], ['$MoP$', '$S\\tilde{a}M$', '$SoP$']],\
[['u', 'u', 'n', 'n', 'u', 'u', 'n', 'a'], ['$M\\tilde{a}P$', '$SaM$', '$S\\ddot{\\imath}P$']],\
[['n', 'a', 'n', 'n', 'n', 'u', 'a', 'u'], ['$M\\tilde{a}P$', '$SeM$', '$SeP$']],\
[['u', 'u', 'n', 'n', 'u', 'u', 'a', 'u'], ['$M\\tilde{a}P$', '$SoM$', '$SoP$']],\
[['a', 'n', 'n', 'n', 'u', 'n', 'u', 'a'], ['$M\\tilde{a}P$', '$S\\tilde{a}M$', '$S\\tilde{a}P$']],\
[['u', 'u', 'n', 'n', 'u', 'u', 'a', 'n'], ['$M\\tilde{a}P$', '$S\\ddot{e}M$', '$SoP$']],\
[['u', 'u', 'n', 'n', 'u', 'u', 'u', 'a'], ['$M\\tilde{a}P$', '$S\\ddot{\\imath}M$', '$S\\ddot{\\imath}P$']],\
[['u', 'u', 'n', 'a', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$SaM$', '$S\\tilde{o}P$']],\
[['n', 'u', 'a', 'u', 'n', 'a', 'n', 'n'], ['$M\\ddot{e}P$', '$SeM$', '$SaP$']],\
[['u', 'u', 'a', 'u', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$SoM$', '$SiP$']],\
[['u', 'n', 'u', 'a', 'a', 'n', 'n', 'n'], ['$M\\ddot{e}P$', '$S\\tilde{a}M$', '$SS\\ddot{e}P$']],\
[['u', 'u', 'a', 'n', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$S\\ddot{e}M$', '$SiP$']],\
[['u', 'u', 'u', 'a', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$S\\ddot{\\imath}M$', '$S\\tilde{o}P$']],\
[['u', 'u', 'n', 'u', 'u', 'u', 'n', 'a'], ['$M\\ddot{\\imath}P$', '$SaM$', '$S\\ddot{\\imath}P$']],\
[['u', 'u', 'u', 'n', 'u', 'u', 'a', 'n'], ['$M\\ddot{\\imath}P$', '$S\\ddot{e}M$', '$SoP$']],\
[['u', 'u', 'n', 'a', 'u', 'u', 'n', 'u'], ['$M\\tilde{o}P$', '$SaM$', '$S\\tilde{o}P$']],\
[['u', 'u', 'a', 'n', 'u', 'u', 'u', 'n'], ['$M\\tilde{o}P$', '$S\\ddot{e}M$', '$SiP$']]]
        
    list_third_level_input = []
    count = 0
    count_2 = 0

    #count_x = 0

    list_of_total_formulas_edited = []
    
    dummy_list = []
    
    begin_now = datetime.now()
    print("BEGIN:", begin_now)
    
    

    with open('syllogism_chain_05_08_2026__Beide.csv', 'w') as file:
        writer = csv.writer(file)
    
        for p, formula_1 in enumerate(list_syllogistik_ganzformeln):
            for r, formula_2 in enumerate(list_syllogistik_ganzformeln):

                #for s, formula_3 in enumerate(list_syllogistik_ganzformeln):
                    #for t, formula_4 in enumerate(list_syllogism_total_formulas):
                                                                                                                                            
                
                #if ((p+1) and (r+1)) == (1 or 5 or 7 or 11 or 18 or 20 or 24 or 26):

                first_formula_tri = formula_1[0]  
                second_formula_tri = formula_2[0] 
                third_formula_tri = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'] 
                #fourth_formula_tri = formula_4[2]
                fourth_formula_tri = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'] 
                #fourth_formula_tri = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
                #print(first_formula_tri)
                #print(second_formula_tri)
                #print(third_formula_tri)
                #print(fourth_formula_tri)
            

            
            
                solution_and_contradiction_test = syllogism_contradiction_test_tet(first_formula_tri, second_formula_tri, third_formula_tri)
                            #solution_and_contradiction_test[0].count('u') == 1 --> one 'u' in total-formula
                            #len(error_number) == 0 --> no contradiction
                                                                
                            #if len(error_number) != 0:
                            #    count_x = count_x + 1
                            #    print(error_number)                        
                #print(solution_and_contradiction_test)
                if (solution_and_contradiction_test[0] != 'W') and solution_and_contradiction_test[0] != ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']:
                                                                                                                                                     
                    for solution_comparison in list_syllogistik_ganzformeln:
                        if solution_and_contradiction_test[0] == solution_comparison[0]:
                            #print(solution_and_contradiction_test[0])
                            #print(solution_comparison[2])
                            #print("-----------")
                            count = count + 1   
                            if formula_1[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                
                                if solution_comparison[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "X1", "XXX"])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "X1", "XXX"])
                                else:
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "X1"])
                                
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "X1"])
                                
                            elif formula_2[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                if solution_comparison[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "X2", "XXX"])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "X2", "XXX"])
                                else:
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "X2"])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "X2"])
                                
                                
                            elif formula_1[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}") and \
                                 formula_2[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "XX"])
                                
                                dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], "XX"])
                                
                            else:
                                
                                if solution_comparison[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], " ", "XXX"])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"], " ", "XXX"])
                                else:
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"]])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["1"]])
                            
                            
                            break
                
                #for s, formula_3 in enumerate(list_syllogistik_ganzformeln):
                    #for t, formula_4 in enumerate(list_syllogism_total_formulas):
                                                                                                                                            
                a = first_formula_tri
                b = second_formula_tri
                c = third_formula_tri
                
                
                first_formula_tri = c
                second_formula_tri = a    
                third_formula_tri = b
                #fourth_formula_tri = formula_4[2]
                fourth_formula_tri = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
                #fourth_formula_tri = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
                #print(first_formula_tri)
                #print(second_formula_tri)
                #print(third_formula_tri)
                #print(fourth_formula_tri)
            

            
            
                solution_and_contradiction_test = syllogism_contradiction_test_tet(first_formula_tri, second_formula_tri, third_formula_tri)
                            #solution_and_contradiction_test[0].count('u') == 1 --> one 'u' in total-formula
                            #len(error_number) == 0 --> no contradiction
                                                                
                            #if len(error_number) != 0:
                            #    count_x = count_x + 1
                            #    print(error_number)                        
                #print(solution_and_contradiction_test)
                if (solution_and_contradiction_test[0] != 'W') and solution_and_contradiction_test[0] != ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']:
                                                                                                                                                      
                    for solution_comparison in list_syllogistik_ganzformeln:
                        if solution_and_contradiction_test[0] == solution_comparison[0]:
                            count_2 = count_2 + 1  
                            #print(solution_and_contradiction_test[0])
                            #print(solution_comparison[2])
                            #print("-----------")
                            if formula_1[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                
                                if solution_comparison[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "X2", "XXX"])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "X2", "XXX"])
                                else:
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "X2"])
                                
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "X2"])
                                
                            elif formula_2[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                if solution_comparison[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "X3", "XXX"])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "X3", "XXX"])
                                else:
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "X3"])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "X3"])
                                
                                
                            elif formula_1[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}") and \
                                 formula_2[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "XX"])
                                
                                dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], "XX"])
                                
                            else:
                                
                                if solution_comparison[1][2][2:-2] == ("a" or "e" or "\\tilde{a}" or "\\ddot{e}"):
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], " ", "XXX"])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"], " ", "XXX"])
                                else:
                                    writer.writerow([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"]])
                                    
                                    dummy_list.append([solution_and_contradiction_test[0], [p+1, r+1], [formula_1[1], formula_2[1]], ["2"]])
                            
                            
                            break
                
        
        file.close()
                                                                                                                                          
    end_now = datetime.now()
    print("END:", end_now)

    print("chains#1 without exact syllogism conclusion:", count)
    print("chains#2 without exact syllogism conclusion:", count_2)
    
    count_func(dummy_list, list_syllogistik_ganzformeln)
    count_func_2(dummy_list, list_syllogistik_ganzformeln)
    count_func_3(dummy_list, list_syllogistik_ganzformeln)
    
    count_form = 0
    
    for entry in dummy_list:
        
        if entry[0].count("a") == 1:
            count_form = count_form + 1
    
    print(count_form)
    
def count_func(dummy_list, list_syllogistik_ganzformeln):

    list_syllogisms_count = []
    
    for entry in dummy_list:
        for r, syllogisms in enumerate(list_syllogistik_ganzformeln):
            if entry[0] == syllogisms[0]:
                list_syllogisms_count.append(r)
    
    count_list = []
    
    for entry in list_syllogisms_count:
        count_3 = 0
        for entry_2 in list_syllogisms_count:
            if entry == entry_2:
                #print(entry, count_3)
                count_3 = count_3 + 1
                count_list.append([entry, count_3])
        
    max_count_list = []
    max_count_list_2 = []
    
    count_list.sort(key=lambda x: x[1], reverse=True)
    
    
    
    for entry in count_list:
        #print(entry)
        if (entry[0] not in max_count_list):
            max_count_list.append(entry[0])
            max_count_list_2.append(entry)
            
    max_count_list_2.sort(key=lambda x: x[0])        
    
    for entry in max_count_list_2:
        for r, syllogisms in enumerate(list_syllogistik_ganzformeln):
            if entry[0] == r:
                #print([r+1], [syllogisms], "count: ", [entry[1]])
                print(entry[1])


def count_func_2(dummy_list, list_syllogistik_ganzformeln):


    list_syllogisms_count = []
    
    for entry in dummy_list:
        for r, syllogisms in enumerate(list_syllogistik_ganzformeln):
            
            if entry[1][0] == (r+1):
                list_syllogisms_count.append(r)
    
    count_list = []
    
    for entry in list_syllogisms_count:
        count_3 = 0
        for entry_2 in list_syllogisms_count:
            if entry == entry_2:
                #print(entry, count_3)
                count_3 = count_3 + 1
                count_list.append([entry, count_3])
        
    max_count_list = []
    max_count_list_2 = []
    
    count_list.sort(key=lambda x: x[1], reverse=True)
    
    
    
    for entry in count_list:
        #print(entry)
        if (entry[0] not in max_count_list):
            max_count_list.append(entry[0])
            max_count_list_2.append(entry)
            
    max_count_list_2.sort(key=lambda x: x[0])        
    
    for entry in max_count_list_2:
        for r, syllogisms in enumerate(list_syllogistik_ganzformeln):
            if entry[0] == r:
                #print([r+1], [syllogisms], "count: ", [entry[1]])
                print(entry[1])


def count_func_3(dummy_list, list_syllogistik_ganzformeln):


    list_syllogisms_count = []
    
    for entry in dummy_list:
        for r, syllogisms in enumerate(list_syllogistik_ganzformeln):
            
            if entry[1][1] == r+1:
                list_syllogisms_count.append(r)
    
    count_list = []
    
    for entry in list_syllogisms_count:
        count_3 = 0
        for entry_2 in list_syllogisms_count:
            if entry == entry_2:
                #print(entry, count_3)
                count_3 = count_3 + 1
                count_list.append([entry, count_3])
        
    max_count_list = []
    max_count_list_2 = []
    
    count_list.sort(key=lambda x: x[1], reverse=True)
    
    
    
    for entry in count_list:
        #print(entry)
        if (entry[0] not in max_count_list):
            max_count_list.append(entry[0])
            max_count_list_2.append(entry)
            
    max_count_list_2.sort(key=lambda x: x[0])        
    
    for entry in max_count_list_2:
        for r, syllogisms in enumerate(list_syllogistik_ganzformeln):
            if entry[0] == r:
                #print([r+1], [syllogisms], "count: ", [entry[1]])
                print(entry[1])

    

deduction_of_tetradic_total_formulas_from_triadic_level()