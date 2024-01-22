import random
compliment_file = "compliment.txt"
oracle_file = "oracle.txt"
color_file = "color.txt"
animal_file = "animal.txt"
epitet_file = "epitet.txt"
action_file = "action.txt"
def get_compliment_line(compliment_file):
    with open(compliment_file, 'r', encoding='utf-8') as file:
        list_of_lines = file.readlines()

        random_line_number = random.randint(0, len(list_of_lines) - 1)
        return list_of_lines[random_line_number]

#random_line = get_compliment_line(compliment_file)
#print(f"Бодічка, {random_line}")

def get_oracle_line(oracle_file):
    with open(oracle_file, 'r', encoding='utf-8') as file:
        list_of_lines = file.readlines()

        random_line_number = random.randint(0, len(list_of_lines) - 1)
        return list_of_lines[random_line_number]


def get_epitet_line(epitet_file):
    with open(epitet_file, 'r', encoding='utf-8') as file:
        list_of_lines = file.readlines()

        random_line_number = random.randint(0, len(list_of_lines) - 1)
        return list_of_lines[random_line_number]


def get_color_line(color_file):
    with open(color_file, 'r', encoding='utf-8') as file:
        list_of_lines = file.readlines()

        random_line_number = random.randint(0, len(list_of_lines) - 1)
        return list_of_lines[random_line_number]


def get_animal_line(animal_file):
    with open(animal_file, 'r', encoding='utf-8') as file:
        list_of_lines = file.readlines()

        random_line_number = random.randint(0, len(list_of_lines) - 1)
        return list_of_lines[random_line_number]


def get_action_line(action_file):
    with open(action_file, 'r', encoding='utf-8') as file:
        list_of_lines = file.readlines()

        random_line_number = random.randint(0, len(list_of_lines) - 1)
        return list_of_lines[random_line_number]

