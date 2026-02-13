from datetime import datetime
import csv

def total_formula_deduction_first_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[0] == "n":    #caluculates potential "n"-values of first value
        return("n")
    elif second_formula[0] == "n":
        return("n")
    elif third_formula[0] == "n":
        return("n")
    elif fourth_formula[0] == "n":
        return("n")
    else: #calculates potential "u"-values of first value
        return("u")

def total_formula_deduction_first_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[0] == "a" and second_formula[1] == "n":    #calculates potential "a"-values of first value
        return("a")
    elif first_formula[0] == "a" and third_formula[1] == "n":
        return("a")
    elif first_formula[0] == "a" and fourth_formula[1] == "n":
        return("a")
    elif second_formula[0] == "a" and first_formula[2] == "n":
        return("a")
    elif second_formula[0] == "a" and third_formula[2] == "n":
        return("a")
    elif second_formula[0] == "a" and fourth_formula[4] == "n":
        return("a")
    elif third_formula[0] == "a" and first_formula[1] == "n":
        return("a")
    elif third_formula[0] == "a" and second_formula[2] == "n":
        return("a")
    elif third_formula[0] == "a" and fourth_formula[2] == "n":
        return("a")
    elif fourth_formula[0] == "a" and first_formula[4] == "n":
        return("a")
    elif fourth_formula[0] == "a" and second_formula[4] == "n":
        return("a")
    elif fourth_formula[0] == "a" and third_formula[4] == "n":
        return("a")
    else: #calculates potential "u"-values of first value
        return("u")

def total_formula_deduction_second_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[0] == "n":    #caluculates potential "n"-values of second value
        return("n")
    elif second_formula[1] == "n":
        return("n")
    elif third_formula[1] == "n":
        return("n")
    elif fourth_formula[1] == "n":
        return("n")
    else: #calculates potential "u"-values of second value
        return("u")

def total_formula_deduction_second_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[0] == "a" and second_formula[0] == "n":    #calculates potential "a"-values of second value
        return("a")
    elif first_formula[0] == "a" and third_formula[0] == "n":
        return("a")
    elif first_formula[0] == "a" and fourth_formula[0] == "n":
        return("a")
    elif second_formula[1] == "a" and first_formula[2] == "n":
        return("a")
    elif second_formula[1] == "a" and third_formula[3] == "n":
        return("a")
    elif second_formula[1] == "a" and fourth_formula[5] == "n":
        return("a")
    elif third_formula[1] == "a" and first_formula[1] == "n":
        return("a")
    elif third_formula[1] == "a" and second_formula[3] == "n":
        return("a")
    elif third_formula[1] == "a" and fourth_formula[3] == "n":
        return("a")
    elif fourth_formula[1] == "a" and first_formula[4] == "n":
        return("a")
    elif fourth_formula[1] == "a" and second_formula[5] == "n":
        return("a")
    elif fourth_formula[1] == "a" and third_formula[5] == "n":
        return("a")
    else: #calculates potential "u"-values of second value
        return("u")

def total_formula_deduction_third_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[1] == "n":    #caluculates potential "n"-values of third value
        return("n")
    elif second_formula[2] == "n":
        return("n")
    elif third_formula[0] == "n":
        return("n")
    elif fourth_formula[2] == "n":
        return("n")
    else: #calculates potential "u"-values of third value
        return("u")

def total_formula_deduction_third_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[1] == "a" and second_formula[3] == "n":    #calculates potential "a"-values of third value
        return("a")
    elif first_formula[1] == "a" and third_formula[1] == "n":
        return("a")
    elif first_formula[1] == "a" and fourth_formula[3] == "n":
        return("a")
    elif second_formula[2] == "a" and first_formula[3] == "n":
        return("a")
    elif second_formula[2] == "a" and third_formula[2] == "n":
        return("a")
    elif second_formula[2] == "a" and fourth_formula[6] == "n":
        return("a")
    elif third_formula[0] == "a" and first_formula[0] == "n":
        return("a")
    elif third_formula[0] == "a" and second_formula[0] == "n":
        return("a")
    elif third_formula[0] == "a" and fourth_formula[0] == "n":
        return("a")
    elif fourth_formula[2] == "a" and first_formula[5] == "n":
        return("a")
    elif fourth_formula[2] == "a" and second_formula[6] == "n":
        return("a")
    elif fourth_formula[2] == "a" and third_formula[4] == "n":
        return("a")
    else: #calculates potential "u"-values of third value
        return("u")

def total_formula_deduction_fourth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[1] == "n":    #caluculates potential "n"-values of fourth value
        return("n")
    elif second_formula[3] == "n":
        return("n")
    elif third_formula[1] == "n":
        return("n")
    elif fourth_formula[3] == "n":
        return("n")
    else: #calculates potential "u"-values of fourth value
        return("u")

def total_formula_deduction_fourth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[1] == "a" and second_formula[2] == "n":    #calculates potential "a"-values of fourth value
        return("a")
    elif first_formula[1] == "a" and third_formula[0] == "n":
        return("a")
    elif first_formula[1] == "a" and fourth_formula[2] == "n":
        return("a")
    elif second_formula[3] == "a" and first_formula[3] == "n":
        return("a")
    elif second_formula[3] == "a" and third_formula[3] == "n":
        return("a")
    elif second_formula[3] == "a" and fourth_formula[7] == "n":
        return("a")
    elif third_formula[1] == "a" and first_formula[0] == "n":
        return("a")
    elif third_formula[1] == "a" and second_formula[1] == "n":
        return("a")
    elif third_formula[1] == "a" and fourth_formula[1] == "n":
        return("a")
    elif fourth_formula[3] == "a" and first_formula[5] == "n":
        return("a")
    elif fourth_formula[3] == "a" and second_formula[7] == "n":
        return("a")
    elif fourth_formula[3] == "a" and third_formula[5] == "n":
        return("a")
    else: #calculates potential "u"-values of fourth value
        return("u")

def total_formula_deduction_fifth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[2] == "n":    #caluculates potential "n"-values of fifth value
        return("n")
    elif second_formula[0] == "n":
        return("n")
    elif third_formula[2] == "n":
        return("n")
    elif fourth_formula[4] == "n":
        return("n")
    else: #calculates potential "u"-values of fifth value
        return("u")

def total_formula_deduction_fifth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[2] == "a" and second_formula[1] == "n":    #calculates potential "a"-values of fifth value
        return("a")
    elif first_formula[2] == "a" and third_formula[3] == "n":
        return("a")
    elif first_formula[2] == "a" and fourth_formula[5] == "n":
        return("a")
    elif second_formula[0] == "a" and first_formula[0] == "n":
        return("a")
    elif second_formula[0] == "a" and third_formula[0] == "n":
        return("a")
    elif second_formula[0] == "a" and fourth_formula[0] == "n":
        return("a")
    elif third_formula[2] == "a" and first_formula[3] == "n":
        return("a")
    elif third_formula[2] == "a" and second_formula[2] == "n":
        return("a")
    elif third_formula[2] == "a" and fourth_formula[6] == "n":
        return("a")
    elif fourth_formula[4] == "a" and first_formula[6] == "n":
        return("a")
    elif fourth_formula[4] == "a" and second_formula[4] == "n":
        return("a")
    elif fourth_formula[4] == "a" and third_formula[6] == "n":
        return("a")
    else: #calculates potential "u"-values of fifth value
        return("u")

def total_formula_deduction_sixth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[2] == "n":    #caluculates potential "n"-values of sixth value
        return("n")
    elif second_formula[1] == "n":
        return("n")
    elif third_formula[3] == "n":
        return("n")
    elif fourth_formula[5] == "n":
        return("n")
    else: #calculates potential "u"-values of sixth value
        return("u")
    
def total_formula_deduction_sixth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[2] == "a" and second_formula[0] == "n":    #calculates potential "a"-values of sixth value
        return("a")
    elif first_formula[2] == "a" and third_formula[2] == "n":
        return("a")
    elif first_formula[2] == "a" and fourth_formula[4] == "n":
        return("a")
    elif second_formula[1] == "a" and first_formula[0] == "n":
        return("a")
    elif second_formula[1] == "a" and third_formula[1] == "n":
        return("a")
    elif second_formula[1] == "a" and fourth_formula[1] == "n":
        return("a")
    elif third_formula[3] == "a" and first_formula[3] == "n":
        return("a")
    elif third_formula[3] == "a" and second_formula[3] == "n":
        return("a")
    elif third_formula[3] == "a" and fourth_formula[7] == "n":
        return("a")
    elif fourth_formula[5] == "a" and first_formula[6] == "n":
        return("a")
    elif fourth_formula[5] == "a" and second_formula[5] == "n":
        return("a")
    elif fourth_formula[5] == "a" and third_formula[7] == "n":
        return("a")
    else: #calculates potential "u"-values of sixth value
        return("u")

def total_formula_deduction_seventh_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[3] == "n":    #caluculates potential "n"-values of sixth value
        return("n")
    elif second_formula[2] == "n":
        return("n")
    elif third_formula[2] == "n":
        return("n")
    elif fourth_formula[6] == "n":
        return("n")
    else: #calculates potential "u"-values of sixth value
        return("u")

def total_formula_deduction_seventh_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[3] == "a" and second_formula[3] == "n":    #calculates potential "a"-values of sixth value
        return("a")
    elif first_formula[3] == "a" and third_formula[3] == "n":
        return("a")
    elif first_formula[3] == "a" and fourth_formula[7] == "n":
        return("a")
    elif second_formula[2] == "a" and first_formula[1] == "n":
        return("a")
    elif second_formula[2] == "a" and third_formula[0] == "n":
        return("a")
    elif second_formula[2] == "a" and fourth_formula[2] == "n":
        return("a")
    elif third_formula[2] == "a" and first_formula[2] == "n":
        return("a")
    elif third_formula[2] == "a" and second_formula[0] == "n":
        return("a")
    elif third_formula[2] == "a" and fourth_formula[4] == "n":
        return("a")
    elif fourth_formula[6] == "a" and first_formula[7] == "n":
        return("a")
    elif fourth_formula[6] == "a" and second_formula[6] == "n":
        return("a")
    elif fourth_formula[6] == "a" and third_formula[6] == "n":
        return("a")
    else: #calculates potential "u"-values of sixth value
        return("u")

def total_formula_deduction_eighth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[3] == "n":    #caluculates potential "n"-values of eighth value
        return("n")
    elif second_formula[3] == "n":
        return("n")
    elif third_formula[3] == "n":
        return("n")
    elif fourth_formula[7] == "n":
        return("n")
    else: #calculates potential "u"-values of eighth value
        return("u")

def total_formula_deduction_eighth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[3] == "a" and second_formula[2] == "n":    #calculates potential "a"-values of eighth value
        return("a")
    elif first_formula[3] == "a" and third_formula[2] == "n":
        return("a")
    elif first_formula[3] == "a" and fourth_formula[6] == "n":
        return("a")
    elif second_formula[3] == "a" and first_formula[1] == "n":
        return("a")
    elif second_formula[3] == "a" and third_formula[1] == "n":
        return("a")
    elif second_formula[3] == "a" and fourth_formula[3] == "n":
        return("a")
    elif third_formula[3] == "a" and first_formula[2] == "n":
        return("a")
    elif third_formula[3] == "a" and second_formula[1] == "n":
        return("a")
    elif third_formula[3] == "a" and fourth_formula[5] == "n":
        return("a")
    elif fourth_formula[7] == "a" and first_formula[7] == "n":
        return("a")
    elif fourth_formula[7] == "a" and second_formula[7] == "n":
        return("a")
    elif fourth_formula[7] == "a" and third_formula[7] == "n":
        return("a")
    else: #calculates potential "u"-values of eighth value
        return("u")
    

def total_formula_deduction_ninth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[4] == "n":    #caluculates potential "n"-values of ninth value
        return("n")
    elif second_formula[4] == "n":
        return("n")
    elif third_formula[4] == "n":
        return("n")
    elif fourth_formula[0] == "n":
        return("n")
    else: #calculates potential "u"-values of ninth value
        return("u")

def total_formula_deduction_ninth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[4] == "a" and second_formula[5] == "n":    #calculates potential "a"-values of ninth value
        return("a")
    elif first_formula[4] == "a" and third_formula[5] == "n":
        return("a")
    elif first_formula[4] == "a" and fourth_formula[1] == "n":
        return("a")
    elif second_formula[4] == "a" and first_formula[6] == "n":
        return("a")
    elif second_formula[4] == "a" and third_formula[6] == "n":
        return("a")
    elif second_formula[4] == "a" and fourth_formula[4] == "n":
        return("a")
    elif third_formula[4] == "a" and first_formula[5] == "n":
        return("a")
    elif third_formula[4] == "a" and second_formula[6] == "n":
        return("a")
    elif third_formula[4] == "a" and fourth_formula[2] == "n":
        return("a")
    elif fourth_formula[0] == "a" and first_formula[0] == "n":
        return("a")
    elif fourth_formula[0] == "a" and second_formula[0] == "n":
        return("a")
    elif fourth_formula[0] == "a" and third_formula[0] == "n":
        return("a")
    else: #calculates potential "u"-values of ninth value
        return("u")

def total_formula_deduction_tenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[4] == "n":    #caluculates potential "n"-values of tenth value
        return("n")
    elif second_formula[5] == "n":
        return("n")
    elif third_formula[5] == "n":
        return("n")
    elif fourth_formula[1] == "n":
        return("n")
    else: #calculates potential "u"-values of tenth value
        return("u")

def total_formula_deduction_tenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[4] == "a" and second_formula[4] == "n":    #calculates potential "a"-values of tenth value
        return("a")
    elif first_formula[4] == "a" and third_formula[4] == "n":
        return("a")
    elif first_formula[4] == "a" and fourth_formula[0] == "n":
        return("a")
    elif second_formula[5] == "a" and first_formula[6] == "n":
        return("a")
    elif second_formula[5] == "a" and third_formula[7] == "n":
        return("a")
    elif second_formula[5] == "a" and fourth_formula[5] == "n":
        return("a")
    elif third_formula[5] == "a" and first_formula[5] == "n":
        return("a")
    elif third_formula[5] == "a" and second_formula[7] == "n":
        return("a")
    elif third_formula[5] == "a" and fourth_formula[3] == "n":
        return("a")
    elif fourth_formula[1] == "a" and first_formula[0] == "n":
        return("a")
    elif fourth_formula[1] == "a" and second_formula[1] == "n":
        return("a")
    elif fourth_formula[1] == "a" and third_formula[1] == "n":
        return("a")
    else: #calculates potential "u"-values of tenth value
        return("u")

def total_formula_deduction_eleventh_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[5] == "n":    #caluculates potential "n"-values of eleventh value
        return("n")
    elif second_formula[6] == "n":
        return("n")
    elif third_formula[4] == "n":
        return("n")
    elif fourth_formula[2] == "n":
        return("n")
    else: #calculates potential "u"-values of eleventh value
        return("u")

def total_formula_deduction_eleventh_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[5] == "a" and second_formula[7] == "n":    #calculates potential "a"-values of eleventh value
        return("a")
    elif first_formula[5] == "a" and third_formula[5] == "n":
        return("a")
    elif first_formula[5] == "a" and fourth_formula[3] == "n":
        return("a")
    elif second_formula[6] == "a" and first_formula[7] == "n":
        return("a")
    elif second_formula[6] == "a" and third_formula[6] == "n":
        return("a")
    elif second_formula[6] == "a" and fourth_formula[6] == "n":
        return("a")
    elif third_formula[4] == "a" and first_formula[4] == "n":
        return("a")
    elif third_formula[4] == "a" and second_formula[4] == "n":
        return("a")
    elif third_formula[4] == "a" and fourth_formula[0] == "n":
        return("a")
    elif fourth_formula[2] == "a" and first_formula[1] == "n":
        return("a")
    elif fourth_formula[2] == "a" and second_formula[2] == "n":
        return("a")
    elif fourth_formula[2] == "a" and third_formula[0] == "n":
        return("a")
    else: #calculates potential "u"-values of eleventh value
        return("u")

def total_formula_deduction_twelveth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[5] == "n":    #caluculates potential "n"-values of twelveth value
        return("n")
    elif second_formula[7] == "n":
        return("n")
    elif third_formula[5] == "n":
        return("n")
    elif fourth_formula[3] == "n":
        return("n")
    else: #calculates potential "u"-values of twelveth value
        return("u")

def total_formula_deduction_twelveth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[5] == "a" and second_formula[6] == "n":    #calculates potential "a"-values of twelveth value
        return("a")
    elif first_formula[5] == "a" and third_formula[4] == "n":
        return("a")
    elif first_formula[5] == "a" and fourth_formula[2] == "n":
        return("a")
    elif second_formula[7] == "a" and first_formula[7] == "n":
        return("a")
    elif second_formula[7] == "a" and third_formula[7] == "n":
        return("a")
    elif second_formula[7] == "a" and fourth_formula[7] == "n":
        return("a")
    elif third_formula[5] == "a" and first_formula[4] == "n":
        return("a")
    elif third_formula[5] == "a" and second_formula[5] == "n":
        return("a")
    elif third_formula[5] == "a" and fourth_formula[1] == "n":
        return("a")
    elif fourth_formula[3] == "a" and first_formula[1] == "n":
        return("a")
    elif fourth_formula[3] == "a" and second_formula[3] == "n":
        return("a")
    elif fourth_formula[3] == "a" and third_formula[1] == "n":
        return("a")
    else: #calculates potential "u"-values of twelveth value
        return("u")

def total_formula_deduction_thirdteenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[6] == "n":    #caluculates potential "n"-values of thirdteenth value
        return("n")
    elif second_formula[4] == "n":
        return("n")
    elif third_formula[6] == "n":
        return("n")
    elif fourth_formula[4] == "n":
        return("n")
    else: #calculates potential "u"-values of thirdteenth value
        return("u")

def total_formula_deduction_thirdteenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[6] == "a" and second_formula[5] == "n":    #calculates potential "a"-values of thirdteenth value
        return("a")
    elif first_formula[6] == "a" and third_formula[7] == "n":
        return("a")
    elif first_formula[6] == "a" and fourth_formula[5] == "n":
        return("a")
    elif second_formula[4] == "a" and first_formula[4] == "n":
        return("a")
    elif second_formula[4] == "a" and third_formula[4] == "n":
        return("a")
    elif second_formula[4] == "a" and fourth_formula[0] == "n":
        return("a")
    elif third_formula[6] == "a" and first_formula[7] == "n":
        return("a")
    elif third_formula[6] == "a" and second_formula[6] == "n":
        return("a")
    elif third_formula[6] == "a" and fourth_formula[6] == "n":
        return("a")
    elif fourth_formula[4] == "a" and first_formula[2] == "n":
        return("a")
    elif fourth_formula[4] == "a" and second_formula[0] == "n":
        return("a")
    elif fourth_formula[4] == "a" and third_formula[2] == "n":
        return("a")
    else: #calculates potential "u"-values of thirdteenth value
        return("u")

def total_formula_deduction_fourteenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[6] == "n":    #caluculates potential "n"-values of fourteenth value
        return("n")
    elif second_formula[5] == "n":
        return("n")
    elif third_formula[7] == "n":
        return("n")
    elif fourth_formula[5] == "n":
        return("n")
    else: #calculates potential "u"-values of fourteenth value
        return("u")

def total_formula_deduction_fourteenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[6] == "a" and second_formula[4] == "n":    #calculates potential "a"-values of fourteenth value
        return("a")
    elif first_formula[6] == "a" and third_formula[6] == "n":
        return("a")
    elif first_formula[6] == "a" and fourth_formula[4] == "n":
        return("a")
    elif second_formula[5] == "a" and first_formula[4] == "n":
        return("a")
    elif second_formula[5] == "a" and third_formula[5] == "n":
        return("a")
    elif second_formula[5] == "a" and fourth_formula[1] == "n":
        return("a")
    elif third_formula[7] == "a" and first_formula[7] == "n":
        return("a")
    elif third_formula[7] == "a" and second_formula[7] == "n":
        return("a")
    elif third_formula[7] == "a" and fourth_formula[7] == "n":
        return("a")
    elif fourth_formula[5] == "a" and first_formula[2] == "n":
        return("a")
    elif fourth_formula[5] == "a" and second_formula[1] == "n":
        return("a")
    elif fourth_formula[5] == "a" and third_formula[3] == "n":
        return("a")
    else: #calculates potential "u"-values of fourteenth value
        return("u")

def total_formula_deduction_fifteenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[7] == "n":    #caluculates potential "n"-values of fifthteenth value
        return("n")
    elif second_formula[6] == "n":
        return("n")
    elif third_formula[6] == "n":
        return("n")
    elif fourth_formula[6] == "n":
        return("n")
    else: #calculates potential "u"-values of fifthteenth value
        return("u")

def total_formula_deduction_fifteenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[7] == "a" and second_formula[7] == "n":    #calculates potential "a"-values of fifthteenth value
        return("a")
    elif first_formula[7] == "a" and third_formula[7] == "n":
        return("a")
    elif first_formula[7] == "a" and fourth_formula[7] == "n":
        return("a")
    elif second_formula[6] == "a" and first_formula[5] == "n":
        return("a")
    elif second_formula[6] == "a" and third_formula[4] == "n":
        return("a")
    elif second_formula[6] == "a" and fourth_formula[2] == "n":
        return("a")
    elif third_formula[6] == "a" and first_formula[6] == "n":
        return("a")
    elif third_formula[6] == "a" and second_formula[4] == "n":
        return("a")
    elif third_formula[6] == "a" and fourth_formula[4] == "n":
        return("a")
    elif fourth_formula[6] == "a" and first_formula[3] == "n":
        return("a")
    elif fourth_formula[6] == "a" and second_formula[2] == "n":
        return("a")
    elif fourth_formula[6] == "a" and third_formula[2] == "n":
        return("a")
    else: #calculates potential "u"-values of fifthteenth value
        return("u")

def total_formula_deduction_sixteenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[7] == "n":    #caluculates potential "n"-values of sixteenth value
        return("n")
    elif second_formula[7] == "n":
        return("n")
    elif third_formula[7] == "n":
        return("n")
    elif fourth_formula[7] == "n":
        return("n")
    else: #calculates potential "u"-values of sixteenth value
        return("u")

def total_formula_deduction_sixteenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[7] == "a" and second_formula[6] == "n":    #calculates potential "a"-values of sixteenth value
        return("a")
    elif first_formula[7] == "a" and third_formula[6] == "n":
        return("a")
    elif first_formula[7] == "a" and fourth_formula[6] == "n":
        return("a")
    elif second_formula[7] == "a" and first_formula[5] == "n":
        return("a")
    elif second_formula[7] == "a" and third_formula[5] == "n":
        return("a")
    elif second_formula[7] == "a" and fourth_formula[3] == "n":
        return("a")
    elif third_formula[7] == "a" and first_formula[6] == "n":
        return("a")
    elif third_formula[7] == "a" and second_formula[5] == "n":
        return("a")
    elif third_formula[7] == "a" and fourth_formula[5] == "n":
        return("a")
    elif fourth_formula[7] == "a" and first_formula[3] == "n":
        return("a")
    elif fourth_formula[7] == "a" and second_formula[3] == "n":
        return("a")
    elif fourth_formula[7] == "a" and third_formula[3] == "n":
        return("a")
    else: #calculates potential "u"-values of sixteenth value
        return("u")

def syllogism_contradiction_test_tet( first_formula, second_formula, third_formula, fourth_formula):

    conclusion = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    conclusion[16] = total_formula_deduction_ninth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[17] = total_formula_deduction_ninth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[16] == 'n' or conclusion[0] == 'n') and conclusion[17] == 'a':
        return ('W')
    conclusion[18] = total_formula_deduction_tenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[19] = total_formula_deduction_tenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[18] == 'n' or conclusion[2] == 'n') and conclusion[19] == 'a':
        return ('W')
    conclusion[20] = total_formula_deduction_eleventh_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[21] = total_formula_deduction_eleventh_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[20] == 'n' or conclusion[4] == 'n') and conclusion[21] == 'a':
        return ('W')
    conclusion[22] = total_formula_deduction_twelveth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[23] = total_formula_deduction_twelveth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[22] == 'n' or conclusion[6] == 'n') and conclusion[23] == 'a':
        return ('W')
    conclusion[24] = total_formula_deduction_thirdteenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[25] = total_formula_deduction_thirdteenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[24] == 'n' or conclusion[8] == 'n') and conclusion[25] == 'a':
        return ('W')
    conclusion[26] = total_formula_deduction_fourteenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[27] = total_formula_deduction_fourteenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[26] == 'n' or conclusion[10] == 'n') and conclusion[27] == 'a':
        return ('W')
    conclusion[28] = total_formula_deduction_fifteenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[29] = total_formula_deduction_fifteenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[28] == 'n' or conclusion[12] == 'n') and conclusion[29] == 'a':
        return ('W')
    conclusion[30] = total_formula_deduction_sixteenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[31] = total_formula_deduction_sixteenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[30] == 'n' or conclusion[14] == 'n') and conclusion[31] == 'a':
        return ('W')
    conclusion[0] = total_formula_deduction_first_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[1] = total_formula_deduction_first_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[0] == 'n' or conclusion[16] == 'n') and conclusion[1] == 'a':
        return ('W')
    conclusion[2] = total_formula_deduction_second_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[3] = total_formula_deduction_second_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[2] == 'n' or conclusion[18] == 'n') and conclusion[3] == 'a':
        return ('W')
    conclusion[4] = total_formula_deduction_third_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[5] = total_formula_deduction_third_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[4] == 'n' or conclusion[20] == 'n') and conclusion[5] == 'a':
        return ('W')
    conclusion[6] = total_formula_deduction_fourth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[7] = total_formula_deduction_fourth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[6] == 'n' or conclusion[22] == 'n') and conclusion[7] == 'a':
        return ('W')
    conclusion[8] = total_formula_deduction_fifth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[9] = total_formula_deduction_fifth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[8] == 'n' or conclusion[24] == 'n') and conclusion[9] == 'a':
        return ('W')
    conclusion[10] = total_formula_deduction_sixth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[11] = total_formula_deduction_sixth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[10] == 'n' or conclusion[26] == 'n') and conclusion[11] == 'a':
        return ('W')
    conclusion[12] = total_formula_deduction_seventh_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[13] = total_formula_deduction_seventh_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[12] == 'n' or conclusion[28] == 'n') and conclusion[13] == 'a':
        return ('W')
    conclusion[14] = total_formula_deduction_eighth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[15] = total_formula_deduction_eighth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if (conclusion[14] == 'n' or conclusion[30] == 'n') and conclusion[15] == 'a':
        return ('W')
    


    conclusion_solution = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    for i in range(16):

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
    
    list_formulas_names = [[['a', 'u', 'n', 'u', 'n', 'n', 'n', 'a'], ['$MaP$', '$SaM$', '$SaP$']] ,\
[['n', 'a', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$SeM$', '$S\\tilde{o}P$']] ,\
[['a', 'u', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$SiM$', '$SiP$']] ,\
[['a', 'n', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$S\\tilde{a}M$', '$SiP$']] ,\
[['u', 'a', 'u', 'n', 'n', 'n', 'a', 'n'], ['$MaP$', '$S\\ddot{e}M$', '$SS\\ddot{e}P$']] ,\
[['u', 'a', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$S\\tilde{o}M$', '$S\\tilde{o}P$']] ,\
[['n', 'n', 'n', 'a', 'a', 'u', 'n', 'u'], ['$MeP$', '$SaM$', '$SeP$']] ,\
[['n', 'n', 'u', 'u', 'n', 'a', 'u', 'u'], ['$MeP$', '$SeM$', '$S\\ddot{\\imath}P$']] ,\
[['n', 'n', 'u', 'u', 'a', 'u', 'u', 'u'], ['$MeP$', '$SiM$', '$SoP$']] ,\
[['n', 'n', 'u', 'u', 'a', 'n', 'u', 'u'], ['$MeP$', '$S\\tilde{a}M$', '$SoP$']] ,\
[['n', 'n', 'a', 'n', 'u', 'a', 'u', 'n'], ['$MeP$', '$S\\ddot{e}M$', '$S\\tilde{a}P$']] ,\
[['n', 'n', 'u', 'u', 'u', 'a', 'u', 'u'], ['$MeP$', '$S\\tilde{o}M$', '$S\\ddot{\\imath}P$']] ,\
[['n', 'a', 'u', 'u', 'n', 'u', 'u', 'u'], ['$MiP$', '$SeM$', '$S\\tilde{o}P$']] ,\
[['a', 'n', 'u', 'u', 'u', 'n', 'u', 'u'], ['$MiP$', '$S\\tilde{a}M$', '$SiP$']] ,\
[['n', 'u', 'u', 'u', 'n', 'a', 'u', 'u'], ['$MoP$', '$SeM$', '$S\\ddot{\\imath}P$']] ,\
[['u', 'n', 'u', 'u', 'a', 'n', 'u', 'u'], ['$MoP$', '$S\\tilde{a}M$', '$SoP$']] ,\
[['u', 'u', 'n', 'n', 'u', 'u', 'n', 'a'], ['$M\\tilde{a}P$', '$SaM$', '$S\\ddot{\\imath}P$']] ,\
[['n', 'a', 'n', 'n', 'n', 'u', 'a', 'u'], ['$M\\tilde{a}P$', '$SeM$', '$SeP$']] ,\
[['u', 'u', 'n', 'n', 'u', 'u', 'a', 'u'], ['$M\\tilde{a}P$', '$SoM$', '$SoP$']] ,\
[['a', 'n', 'n', 'n', 'u', 'n', 'u', 'a'], ['$M\\tilde{a}P$', '$S\\tilde{a}M$', '$S\\tilde{a}P$']] ,\
[['u', 'u', 'n', 'n', 'u', 'u', 'a', 'n'], ['$M\\tilde{a}P$', '$S\\ddot{e}M$', '$SoP$']] ,\
[['u', 'u', 'n', 'n', 'u', 'u', 'u', 'a'], ['$M\\tilde{a}P$', '$S\\ddot{\\imath}M$', '$S\\ddot{\\imath}P$']] ,\
[['u', 'u', 'n', 'a', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$SaM$', '$S\\tilde{o}P$']] ,\
[['n', 'u', 'a', 'u', 'n', 'a', 'n', 'n'], ['$M\\ddot{e}P$', '$SeM$', '$SaP$']] ,\
[['u', 'u', 'a', 'u', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$SoM$', '$SiP$']] ,\
[['u', 'n', 'u', 'a', 'a', 'n', 'n', 'n'], ['$M\\ddot{e}P$', '$S\\tilde{a}M$', '$SS\\ddot{e}P$']] ,\
[['u', 'u', 'a', 'n', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$S\\ddot{e}M$', '$SiP$']] ,\
[['u', 'u', 'u', 'a', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$S\\ddot{\\imath}M$', '$S\\tilde{o}P$']] ,\
[['u', 'u', 'n', 'u', 'u', 'u', 'n', 'a'], ['$M\\ddot{\\imath}P$', '$SaM$', '$S\\ddot{\\imath}P$']] ,\
[['u', 'u', 'u', 'n', 'u', 'u', 'a', 'n'], ['$M\\ddot{\\imath}P$', '$S\\ddot{e}M$', '$SoP$']] ,\
[['u', 'u', 'n', 'a', 'u', 'u', 'n', 'u'], ['$M\\tilde{o}P$', '$SaM$', '$S\\tilde{o}P$']] ,\
[['u', 'u', 'a', 'n', 'u', 'u', 'u', 'n'], ['$M\\tilde{o}P$', '$S\\ddot{e}M$', '$SiP$']]]
    new_formula_4_list= []
    new_formula_B_list = []
    new_formula_2_list = []

    for formulas_names in list_formulas_names:
        if formulas_names[0] == formula:
            #print(formula_list_name[0])
            if index_premis_circumstance == 2:
                for x1, premis in enumerate(formulas_names[1]):
                    new_formula_A = premis[:].replace("S", "X")
                    new_formula_2 = new_formula_A.replace("P", "Q")
                    new_formula_3 = new_formula_2.replace("M", "P")
                    new_formula_4 = new_formula_3.replace("X", "M")
                    new_formula_4_list.append(new_formula_4)
                return [new_formula_4_list]
            #"$C$\textbullet$D$\textbullet$E$"
            elif index_premis_circumstance == 1:
                for x2, premis_2 in enumerate(formulas_names[1]):
                    new_formula_B = premis_2[:].replace("P", "Q")
                    new_formula_B_list.append(new_formula_B)
                return [new_formula_B_list]
            #"$B$\textbullet$C$\textbullet$E$"
            elif index_premis_circumstance == 3:
                for x3, premis_3 in enumerate(formulas_names[1]):
                    new_formula_C = formulas_names[1][0][:].replace("P", "Q")
                    new_formula_2 = new_formula_C.replace("M", "P")
                    new_formula_2_list.append(new_formula_2)
                return [new_formula_2_list]
            #"$B$\textbullet$D$\textbullet$E$"
            elif index_premis_circumstance == 4:
                return [formulas_names[1]]
            #"$B$\textbullet$C$\textbullet$D$"
    


"""def replace_total_formulas_fn( total_formula_old, *args):


    for j in range(8):
        if total_formula_old[j] == 'u':
            total_formula_old[j] = 'a'    
            total_formula_new_A = total_formula_old[:]
            total_formula_old[j] = 'n'
            total_formula_new_N = total_formula_old[:]
            
            return(total_formula_new_A, total_formula_new_N, j+1)
    
    return(0)"""

                                        
def deduction_of_tetradic_total_formulas_from_triadic_level( *args):
    #~4 billion Possibilitys from triadic possibilitys to tetradic possibilitys:
    #21 places = 12 sec
    #22 places = 24 sec
    #32 places = 6.8 h (calculated approximatly)
    #BEGIN: 2025-02-06 22:46:15.554045
    #END: 2025-02-07 05:24:23.855997
    
    list_q = [[['a', 'a', 'u', 'u', 'n', 'n', 'a', 'a'], 1] ,\
            [['n', 'n', 'a', 'a', 'a', 'a', 'u', 'u'], 1] ,\
            [['a', 'a', 'u', 'u', 'u', 'u', 'u', 'u'], 1] ,\
            [['u', 'u', 'u', 'u', 'a', 'a', 'u', 'u'], 1] ,\
            [['a', 'a', 'n', 'n', 'u', 'u', 'a', 'a'], 1] ,\
            [['u', 'u', 'a', 'a', 'a', 'a', 'n', 'n'], 1] ,\
            [['u', 'u', 'u', 'u', 'u', 'u', 'a', 'a'], 1] ,\
            [['u', 'u', 'a', 'a', 'u', 'u', 'u', 'u'], 1] ,\
            [['a', 'u', 'n', 'a', 'a', 'u', 'n', 'a'], 2] ,\
            [['n', 'a', 'a', 'u', 'n', 'a', 'a', 'u'], 2] ,\
            [['a', 'u', 'u', 'u', 'a', 'u', 'u', 'u'], 2] ,\
            [['u', 'u', 'a', 'u', 'u', 'u', 'a', 'u'], 2] ,\
            [['a', 'n', 'u', 'a', 'a', 'n', 'u', 'a'], 2] ,\
            [['u', 'a', 'a', 'n', 'u', 'a', 'a', 'n'], 2] ,\
            [['u', 'u', 'u', 'a', 'u', 'u', 'u', 'a'], 2] ,\
            [['u', 'a', 'u', 'u', 'u', 'a', 'u', 'u'], 2] ,\
            [['a', 'u', 'a', 'u', 'n', 'a', 'n', 'a'], 3] ,\
            [['n', 'a', 'n', 'a', 'a', 'u', 'a', 'u'], 3] ,\
            [['a', 'u', 'a', 'u', 'u', 'u', 'u', 'u'], 3] ,\
            [['u', 'u', 'u', 'u', 'a', 'u', 'a', 'u'], 3] ,\
            [['a', 'n', 'a', 'n', 'u', 'a', 'u', 'a'], 3] ,\
            [['u', 'a', 'u', 'a', 'a', 'n', 'a', 'n'], 3] ,\
            [['u', 'u', 'u', 'u', 'u', 'a', 'u', 'a'], 3] ,\
            [['u', 'a', 'u', 'a', 'u', 'u', 'u', 'u'], 3]]

    list_syllogism_total_formulas_1 = [[['a', 'a', 'u', 'u', 'n', 'n', 'a', 'a'], 'MaP'] ,\
                                    [['n', 'n', 'a', 'a', 'a', 'a', 'u', 'u'], 'MeP'] ,\
                                    [['a', 'a', 'u', 'u', 'u', 'u', 'u', 'u'], 'MiP'] ,\
                                    [['u', 'u', 'u', 'u', 'a', 'a', 'u', 'u'], 'MoP'] ,\
                                    [['a', 'a', 'n', 'n', 'u', 'u', 'a', 'a'], 'MãP'] ,\
                                    [['u', 'u', 'a', 'a', 'a', 'a', 'n', 'n'], 'MëP'] ,\
                                    [['u', 'u', 'u', 'u', 'u', 'u', 'a', 'a'], 'MïP'] ,\
                                    [['u', 'u', 'a', 'a', 'u', 'u', 'u', 'u'], 'MõP']]
    list_syllogism_total_formulas_2= [[['a', 'u', 'n', 'a', 'a', 'u', 'n', 'a'], 'SaM'] ,\
                                    [['n', 'a', 'a', 'u', 'n', 'a', 'a', 'u'], 'SeM'] ,\
                                    [['a', 'u', 'u', 'u', 'a', 'u', 'u', 'u'], 'SiM'] ,\
                                    [['u', 'u', 'a', 'u', 'u', 'u', 'a', 'u'], 'SoM'] ,\
                                    [['a', 'n', 'u', 'a', 'a', 'n', 'u', 'a'], 'SãM'] ,\
                                    [['u', 'a', 'a', 'n', 'u', 'a', 'a', 'n'], 'SëM'] ,\
                                    [['u', 'u', 'u', 'a', 'u', 'u', 'u', 'a'], 'SïM'] ,\
                                    [['u', 'a', 'u', 'u', 'u', 'a', 'u', 'u'], 'SõM']]
    list_syllogism_total_formulas_3 = [[['a', 'u', 'a', 'u', 'n', 'a', 'n', 'a'], 'SaP'] ,\
                                    [['n', 'a', 'n', 'a', 'a', 'u', 'a', 'u'], 'SeP'] ,\
                                    [['a', 'u', 'a', 'u', 'u', 'u', 'u', 'u'], 'SiP'] ,\
                                    [['u', 'u', 'u', 'u', 'a', 'u', 'a', 'u'], 'SoP'] ,\
                                    [['a', 'n', 'a', 'n', 'u', 'a', 'u', 'a'], 'SãP'] ,\
                                    [['u', 'a', 'u', 'a', 'a', 'n', 'a', 'n'], 'SëP'] ,\
                                    [['u', 'u', 'u', 'u', 'u', 'a', 'u', 'a'], 'SïP'] ,\
                                    [['u', 'a', 'u', 'a', 'u', 'u', 'u', 'u'], 'SõP']]
    

    liat_scheise = [[['a', 'u', 'n', 'u', 'n', 'n', 'n', 'a'], ['$MaP$', '$SaM$', '$SaP$']] ,\
[['n', 'a', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$SeM$', '$S\\tilde{o}P$']] ,\
[['a', 'u', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$SiM$', '$SiP$']] ,\
[['a', 'n', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$S\\tilde{a}M$', '$SiP$']] ,\
[['u', 'a', 'u', 'n', 'n', 'n', 'a', 'n'], ['$MaP$', '$S\\ddot{e}M$', '$SS\\ddot{e}P$']] ,\
[['u', 'a', 'u', 'u', 'n', 'n', 'u', 'u'], ['$MaP$', '$S\\tilde{o}M$', '$S\\tilde{o}P$']] ,\
[['n', 'n', 'n', 'a', 'a', 'u', 'n', 'u'], ['$MeP$', '$SaM$', '$SeP$']] ,\
[['n', 'n', 'u', 'u', 'n', 'a', 'u', 'u'], ['$MeP$', '$SeM$', '$S\\ddot{\\imath}P$']] ,\
[['n', 'n', 'u', 'u', 'a', 'u', 'u', 'u'], ['$MeP$', '$SiM$', '$SoP$']] ,\
[['n', 'n', 'u', 'u', 'a', 'n', 'u', 'u'], ['$MeP$', '$S\\tilde{a}M$', '$SoP$']] ,\
[['n', 'n', 'a', 'n', 'u', 'a', 'u', 'n'], ['$MeP$', '$S\\ddot{e}M$', '$S\\tilde{a}P$']] ,\
[['n', 'n', 'u', 'u', 'u', 'a', 'u', 'u'], ['$MeP$', '$S\\tilde{o}M$', '$S\\ddot{\\imath}P$']] ,\
[['n', 'a', 'u', 'u', 'n', 'u', 'u', 'u'], ['$MiP$', '$SeM$', '$S\\tilde{o}P$']] ,\
[['a', 'n', 'u', 'u', 'u', 'n', 'u', 'u'], ['$MiP$', '$S\\tilde{a}M$', '$SiP$']] ,\
[['n', 'u', 'u', 'u', 'n', 'a', 'u', 'u'], ['$MoP$', '$SeM$', '$S\\ddot{\\imath}P$']] ,\
[['u', 'n', 'u', 'u', 'a', 'n', 'u', 'u'], ['$MoP$', '$S\\tilde{a}M$', '$SoP$']] ,\
[['u', 'u', 'n', 'n', 'u', 'u', 'n', 'a'], ['$M\\tilde{a}P$', '$SaM$', '$S\\ddot{\\imath}P$']] ,\
[['n', 'a', 'n', 'n', 'n', 'u', 'a', 'u'], ['$M\\tilde{a}P$', '$SeM$', '$SeP$']] ,\
[['u', 'u', 'n', 'n', 'u', 'u', 'a', 'u'], ['$M\\tilde{a}P$', '$SoM$', '$SoP$']] ,\
[['a', 'n', 'n', 'n', 'u', 'n', 'u', 'a'], ['$M\\tilde{a}P$', '$S\\tilde{a}M$', '$S\\tilde{a}P$']] ,\
[['u', 'u', 'n', 'n', 'u', 'u', 'a', 'n'], ['$M\\tilde{a}P$', '$S\\ddot{e}M$', '$SoP$']] ,\
[['u', 'u', 'n', 'n', 'u', 'u', 'u', 'a'], ['$M\\tilde{a}P$', '$S\\ddot{\\imath}M$', '$S\\ddot{\\imath}P$']] ,\
[['u', 'u', 'n', 'a', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$SaM$', '$S\\tilde{o}P$']] ,\
[['n', 'u', 'a', 'u', 'n', 'a', 'n', 'n'], ['$M\\ddot{e}P$', '$SeM$', '$SaP$']] ,\
[['u', 'u', 'a', 'u', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$SoM$', '$SiP$']] ,\
[['u', 'n', 'u', 'a', 'a', 'n', 'n', 'n'], ['$M\\ddot{e}P$', '$S\\tilde{a}M$', '$SS\\ddot{e}P$']] ,\
[['u', 'u', 'a', 'n', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$S\\ddot{e}M$', '$SiP$']] ,\
[['u', 'u', 'u', 'a', 'u', 'u', 'n', 'n'], ['$M\\ddot{e}P$', '$S\\ddot{\\imath}M$', '$S\\tilde{o}P$']] ,\
[['u', 'u', 'n', 'u', 'u', 'u', 'n', 'a'], ['$M\\ddot{\\imath}P$', '$SaM$', '$S\\ddot{\\imath}P$']] ,\
[['u', 'u', 'u', 'n', 'u', 'u', 'a', 'n'], ['$M\\ddot{\\imath}P$', '$S\\ddot{e}M$', '$SoP$']] ,\
[['u', 'u', 'n', 'a', 'u', 'u', 'n', 'u'], ['$M\\tilde{o}P$', '$SaM$', '$S\\tilde{o}P$']] ,\
[['u', 'u', 'a', 'n', 'u', 'u', 'u', 'n'], ['$M\\tilde{o}P$', '$S\\ddot{e}M$', '$SiP$']]]

    

    list_third_level_input = []
    count = 0

    #count_x = 0

    list_of_total_formulas_edited = []
    
    dummy_list = []
    
    begin_now = datetime.now()
    print("BEGIN:", begin_now)

    with open('syllogism 768.csv', 'w') as file:
        writer = csv.writer(file)
    
        for p, formula_1 in enumerate(liat_scheise):
            for r, formula_2 in enumerate(liat_scheise):
                #for s, formula_3 in enumerate(list_syllogism_total_formulas_3):
                    #for t, formula_4 in enumerate(list_syllogism_total_formulas):
                third_formula_tri = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
                fourth_formula_tri = ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u']  
                
                
                first_formula_tri = formula_1[0]
                second_formula_tri =  formula_2[0]
                #third_formula_tri = formula_3[0]
                solution_and_contradiction_test = syllogism_contradiction_test_tet(first_formula_tri,second_formula_tri,third_formula_tri, fourth_formula_tri)
                
                variable = 1
                if (solution_and_contradiction_test[0] != 'W') and solution_and_contradiction_test[0] != ['u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u', 'u'] and solution_and_contradiction_test[0].count('a') >= 1 :
                    first_formula = triadic_name_fn(first_formula_tri, 1)
                    second_formula = triadic_name_fn(second_formula_tri, 2)
                    third_formula = triadic_name_fn(third_formula_tri, 3)
                    fourth_formula = triadic_name_fn(fourth_formula_tri, 4)
                    
                    writer.writerow([solution_and_contradiction_test[0], first_formula, second_formula, p, r])

#solution_and_contradiction_test[0].count('u') == 1 --> one 'u' in total-formula
                #len(error_number) == 0 --> no contradiction
                                                    
                #if len(error_number) != 0:
                #    count_x = count_x + 1
                #    print(error_number)                        
    #print(solution_and_contradiction_test)
    
                 
        
        mid_now = datetime.now()
        print("MID:", mid_now)
        
            
        file.close()    
                                                                                                                                          
    end_now = datetime.now()
    print("END:", end_now)




    

deduction_of_tetradic_total_formulas_from_triadic_level()