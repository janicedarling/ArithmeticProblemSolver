import parser


# Step 1: Read questions from file
def main():
    # Load questions from file
    with open('data/q1.txt', 'r') as fi:
        questions = fi.readlines()
        for question in questions:
            pass
            # Simplify problem
        word_problem = parser.parse(questions[5])


if __name__ == '__main__':
    main()