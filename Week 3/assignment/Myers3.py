# Animal Guesser
# Its like 20 questions but with fewer questions and only animals

class Node:
    def __init__(self, is_question, value, left_node=None, right_node=None):
        self.is_question = is_question
        self.value = value
        self.child_left = left_node
        self.child_right = right_node

    def set_left_child(self, left_node):
        self.child_left = left_node

    def set_right_child(self, right_node):
        self.child_right = right_node

    def get_left_child(self):
        return self.child_left

    def get_right_child(self):
        return self.child_right

    # picker is either one or zero. One for left (true), zero for right (false)
    def get_child(self, picker):
        if picker > 0:
            return self.get_left_child()
        else:
            return self.get_right_child()

start_node = Node(True, "Is your animal a herbivore?",
                  #herbivore
                  Node(True, "Is your animal a farm animal?",
                       # is a farm animal
                       Node(True, "Does your animal create milk?",
                            # does create milk
                            Node(False, "I think your animal is a cow!"),
                            # does not create milk
                            Node(False, "I think your animal is a chicken!")),
                       # not a farm animal
                       Node(True, "Is your animal tall?",
                            # tall
                            Node(False, "I think your animal is a giraffe"),
                            #not tall
                            Node(False, "I think your animal is a koala")),),
                  # eats meat
                  Node(True,"Is your animal extinct?",
                       # is extinct
                       Node(True, "Is your animal featured in a multi-part movie and book series?",
                            # is in a movie series
                            Node(False, "I think your animal is a t-rex!"),
                            # is not in a movie series
                            Node(False, "I think your animal is a dodo!")),
                       # not extinct
                       Node(True, "Is your animal critically endangered?",
                            # is critically endangered
                            Node(False, "I think your animal is a red wolf!"),
                            # is not critically endangered
                            Node(False, "I think your animal is a hyena!")),
                    )
                )


def animal_guess():
    has_guessed = False
    active_node = start_node
    while not has_guessed:
        if active_node.is_question:
            try:
                user_input = int(input(active_node.value + " (1 for yes, 0 for no) "))
                if user_input == 1 or user_input == 0:
                    active_node = active_node.get_child(user_input)
                else:
                    print("Invalid input, try again!")
            except ValueError:
                print("Invalid input, try again!")
        else:
            print(active_node.value)
            has_guessed = True

if __name__ == '__main__':
    animal_guess()
