# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(participants_first_group, participants_second_group, sep=','):
    first_group = participants_first_group.split(sep)
    second_group = participants_second_group.split(sep)
    common_participant_list = []
    for participants in first_group:
        if participants in second_group:
            common_participant_list.append(participants)
            common_participant_list.sort()
    return common_participant_list
print(find_common_participants(participants_first_group, participants_second_group, sep='#'))

# TODO Провеьте работу функции с разделителем отличным от запятой
