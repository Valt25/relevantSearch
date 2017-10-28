import nltk
import collections
import string

def parse_query(query):
    # prepare query list
    query = query.replace('(', '( ')
    query = query.replace(')', ' )')
    query = query.translate(''.maketrans(string.punctuation, ' ' * len(string.punctuation)))
    query = nltk.word_tokenize(query)


    postfix_queue = collections.deque(shunting_yard(query))  # get query in postfix notation as a queue
    return postfix_queue


def shunting_yard(infix_tokens):
    # define precedences
    precedence = {}
    precedence['LOGNOT'] = 3
    precedence['LOGAND'] = 2
    precedence['LOGOR'] = 1
    precedence['('] = 0
    precedence[')'] = 0

    # declare data strucures
    output = []
    operator_stack = []

    is_prev_nonterm = False
    # while there are tokens to be read
    for token in infix_tokens:

        # if left bracket
        if (token == '('):
            operator_stack.append(token)
            is_prev_nonterm = False

        # if right bracket, pop all operators from operator stack onto output until we hit left bracket
        elif (token == ')'):
            operator = operator_stack.pop()
            while operator != '(':
                output.append(operator)
                operator = operator_stack.pop()
            is_prev_nonterm = False
        # if operator, pop operators from operator stack to queue if they are of higher precedence
        elif (token in precedence):
            # if operator stack is not empty
            if (operator_stack):
                current_operator = operator_stack[-1]
                while (operator_stack and precedence[current_operator] > precedence[token]):
                    output.append(operator_stack.pop())
                    if (operator_stack):
                        current_operator = operator_stack[-1]

            operator_stack.append(token)  # add token to stack
            is_prev_nonterm = False
        # else if operands, add to output list
        else:
            output.append(token.lower())
            if (is_prev_nonterm):
                output.append('LOGAND')
            is_prev_nonterm = True


    # while there are still operators on the stack, pop them into the queue
    while (operator_stack):
        output.append(operator_stack.pop())
        # print ('postfix:', output)  # check


    return output


