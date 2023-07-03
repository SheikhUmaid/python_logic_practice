


def common_elements(list1: list, list2: list):
    common_list = []
    for i in list1:
        for j in list2:
            if i == j:
                common_list.append(i)
                break
    return common_list


print(common_elements(['apple', 'banana', 'orange'], ['orange', 'kiwi', 'grape']))





