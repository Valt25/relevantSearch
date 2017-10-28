import nltk

from IndexCreator.Creator import import_index


def query_process(postfix_queue):
    results_stack = []
    stemmer = nltk.stem.porter.PorterStemmer()  # instantiate stemmer
    dictionary = import_index()._tokens

    while postfix_queue:
        token = postfix_queue.popleft()
        result = []  # the evaluated result at each stage
        # if operand, add postings list for term to results stack
        if (token != 'LOGAND' and token != 'LOGOR' and token != 'LOGNOT'):
            token = stemmer.stem(token)  # stem the token
            # default empty list if not in dictionary
            if (token in dictionary):
                result = dictionary[token]

        # else if AND operator
        elif (token == 'LOGAND'):
            right_operand = results_stack.pop()
            left_operand = results_stack.pop()
            # print(left_operand, 'AND', left_operand) # check
            result = boolean_AND(left_operand, right_operand)  # evaluate AND

        # else if OR operator
        elif (token == 'LOGOR'):
            right_operand = results_stack.pop()
            left_operand = results_stack.pop()
            # print(left_operand, 'OR', left_operand) # check
            result = boolean_OR(left_operand, right_operand)  # evaluate OR

        # else if NOT operator
        elif (token == 'LOGNOT'):
            right_operand = results_stack.pop()
            # print('NOT', right_operand) # check
            result = boolean_NOT(dictionary, right_operand)  # evaluate NOT

        # push evaluated result back to stack
        results_stack.append(result)
        # print ('result', result) # check

    # NOTE: at this point results_stack should only have one item and it is the final result
    if len(results_stack) != 1: print("ERROR: results_stack. Please check valid query")  # check for errors
    return results_stack.pop()


def boolean_AND(left_operand, right_operand):
    result = []
    left_pointer = 0
    right_pointer = 0

    while (left_pointer < len(left_operand)) and (right_pointer < len(right_operand)):
        left_item = left_operand[left_pointer]
        right_item = right_operand[right_pointer]

        if (left_item == right_item):
            result.append(left_item)
            right_pointer += 1
            left_pointer += 1

        elif left_item > right_item:
            right_pointer += 1

        else:
            left_pointer += 1

    return result


def boolean_OR(left_operand, right_operand):
    result = []
    left_pointer = 0
    right_pointer = 0

    while (left_pointer < len(left_operand)) or (right_pointer < len(right_operand)):
        if (left_pointer < len(left_operand)) and (right_pointer < len(right_operand)):
            left_item = left_operand[left_pointer]
            right_item = right_operand[right_pointer]

            if left_item == right_item:
                result.append(left_item)
                left_pointer += 1
                right_pointer += 1

            elif left_item > right_item:
                result.append(right_item)
                right_pointer += 1

            else:
                result.append(left_item)
                left_pointer += 1
        elif right_pointer >= len(right_operand):
            result.append(left_operand[left_pointer])
            left_pointer += 1

        else:
            result.append(right_operand[right_pointer])
            right_pointer += 1

    return result


def boolean_NOT(dictionary, operand):
    doc_IDs = get_doc_IDs(dictionary)
    operand_pointer = 0
    result = []
    for item in doc_IDs:
        if (item != operand[operand_pointer]):
            result.append(item)
        elif operand_pointer + 1 < len(operand):
            operand_pointer += 1
    return result


def get_doc_IDs(dictionary):
    result = []
    for token, doc_list in dictionary.items():
        result = boolean_OR(result, doc_list)
    result.sort()
    return result