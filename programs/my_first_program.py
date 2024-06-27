from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Performing addition
    sum_ints = my_int1 + my_int2

    # Performing multiplication
    product_ints = my_int1 * my_int2

    # Conditional operation
    condition = my_int1 > my_int2
    max_int = If(condition, my_int1, my_int2)

    # Another conditional operation
    condition2 = my_int1 == my_int2
    equal_int = If(condition2, SecretInteger(1), SecretInteger(0))

    return [
        Output(sum_ints, "sum_output", party1),
        Output(product_ints, "product_output", party1),
        Output(max_int, "max_output", party1),
        Output(equal_int, "equal_output", party1)
    ]

def complex_nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Inputs from different parties
    int1_party1 = SecretInteger(Input(name="int1_party1", party=party1))
    int2_party1 = SecretInteger(Input(name="int2_party1", party=party1))
    int1_party2 = SecretInteger(Input(name="int1_party2", party=party2))
    int2_party2 = SecretInteger(Input(name="int2_party2", party=party2))

    # Performing arithmetic operations
    sum_party1 = int1_party1 + int2_party1
    sum_party2 = int1_party2 + int2_party2
    total_sum = sum_party1 + sum_party2

    product_party1 = int1_party1 * int2_party1
    product_party2 = int1_party2 * int2_party2
    total_product = product_party1 * product_party2

    # Conditional operations
    condition1 = int1_party1 > int2_party1
    max_party1 = If(condition1, int1_party1, int2_party1)

    condition2 = int1_party2 > int2_party2
    max_party2 = If(condition2, int1_party2, int2_party2)

    # Combining results
    combined_max = max_party1 + max_party2

    # More complex conditional
    combined_condition = (int1_party1 + int2_party1) > (int1_party2 + int2_party2)
    final_result = If(combined_condition, total_sum, total_product)

    return [
        Output(total_sum, "total_sum_output", party1),
        Output(total_product, "total_product_output", party1),
        Output(max_party1, "max_party1_output", party1),
        Output(max_party2, "max_party2_output", party2),
        Output(combined_max, "combined_max_output", party1),
        Output(final_result, "final_result_output", party1)
    ]
