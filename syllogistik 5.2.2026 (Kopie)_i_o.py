from datetime import datetime
import csv

with open('syllogism GANZFORMELN.csv') as orders_file:
    reader = csv.reader(orders_file, delimiter=',')
    
    deducable_tetradic_formula_list = list(reader)


    deducable_tetradic_formula_copy = deducable_tetradic_formula_list[:]
    copy = deducable_tetradic_formula_copy[:]

    count_acc = 0
    deleted_doubles_1 = []
    for order in deducable_tetradic_formula_copy:
        
        if order[0] not in deleted_doubles_1:
            deleted_doubles_1.append(order[0])
            count_acc = count_acc + 1
                
    #for n, entry in enumerate(deleted_doubles_1):
    print(count_acc)

orders_file.close()
