def get_summ(one, two, delimiter='&'):
    summ = f'{str(one.capitalize())}{delimiter}{str(two.capitalize())}'
    print(summ)

get_summ("Learn", "python")