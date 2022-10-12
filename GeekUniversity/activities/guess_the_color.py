from GeekUniversity.utilities.colors import colors

# CLASSES AND OBJECTS


class Funcionario:
    def __init__(self, cor, function, age, outstanding):
        self.cor = cor
        self.function = function
        self.age = age
        self.outstanding = outstanding


class Questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_lst = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n"
]

'''questions1 = [
    Questions(Questions[0], "a"),
    Questions(Questions[1], "c"),
    Questions(Questions[2], "b"),
]'''

questions1 = []

for c, k in enumerate(question_lst):
    questions1.append(Questions(question_lst[c], (input(f'Answer to the question {c + 1}: '))))


for k, c in enumerate(question_lst):
    choice = input(f'{c}Your Answer: ')
    print(colors.green + 'Correct' + colors.reset) if choice == questions1[k].answer else print(colors.red + 'Uncorrect' + colors.reset)
