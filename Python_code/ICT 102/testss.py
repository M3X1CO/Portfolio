questions = [
    "What is Python?,\n a) High-level programming language, \n b) Snake species, \n c) Computer hardware, \n d) Movie title",
    "How do you comment in Python?,\n a) // Comment, \n b) /* Comment */, \n c) # Comment, \n d) <!-- Comment -->",
    "Which of the following is used for a multi-line comment?,\n a) /** Comment */, \n b) /* Comment */, \n c) # Comment, \n d) ''' Comment '''",
    "What is the output of print(3 * 'abc')?,\n a) abc, \n b) abcabc, \n c) 3abc, \n d) Error",
    "How do you check the length of a list named my_list?,\n a) length(my_list), \n b) len(my_list), \n c) count(my_list), \n d) size(my_list)",
    "What does the range() function in Python generate?,\n a) List of numbers, \n b) Range object, \n c) Random values, \n d) Tuple of numbers",
    "Which keyword is used to define a function in Python?,\n a) func, \n b) define, \n c) function, \n d) def",
    "What does the % operator do in Python?,\n a) Exponentiation, \n b) Modulus, \n c) Division, \n d) Multiplication",
    "How do you check if a key exists in a dictionary?,\n a) key_exists(key, dictionary), \n b) is_key_in(key, dictionary), \n c) key in dictionary, \n d) has_key(dictionary, key)",
    "What is the purpose of the __init__ method in a Python class?,\n a) Initialize the class object, \n b) Terminate the class, \n c) Import external libraries, \n d) Define class attributes"
]

answers = ["a", "c", "d", "b", "b", "b", "d", "b", "c", "a"]

my_dict = dict(zip(questions, answers))

right = []
wrong = []


def main():
    for i, (question, answer) in enumerate(my_dict.items(), 1):
        print(f"{i}. {question}")
        user_answer = input("Your Answer: ").lower()
        if user_answer == answer:
            right.append(i)
        else:
            wrong.append(i)

    print("\nResults:")
    print(f"Correct Answers: {', '.join(map(str, right))}")
    print(f"Incorrect Answers: {', '.join(map(str, wrong))}")


if __name__ == "__main__":
    main()
