import my_functions as my_functions
import calculation as calculation
from datetime import datetime

if __name__ == "__main__":
    
    person_andreas = my_functions.build_person("Andreas", "Holzner", "male", 24)
    experiment_andreas = my_functions.build_experiment("Leistungstest", datetime.now(),"Tobias Gasteiger", person_andreas)
    some_list = [1,2,4,5,67,8,9,7,5,4,6,8,9,87,65,4]
    
    print(f"Angelegt Person:\n{person_andreas}\n")
    print(f"Angelegtes Experiment:\n{experiment_andreas}\n")
    print(f"Calculated mean of:\n{some_list} --> {calculation.calc_mean(some_list)}")