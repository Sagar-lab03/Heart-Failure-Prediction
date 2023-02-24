import re
import long_response as long


# Starting.. In brackets there is written steps, how we approached --> like..
# (1) - first step then we do (2) - second step like that...

# (3) Now we'll Create a function that calculates the probability that the message is the corresponding message
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1  # For more accurate sentence

    # Calculates the percentage of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))  # accuracy percentage

    # Now we check that the required words are included or not
    for word in required_words:
        if word not in user_message:
            has_required_words = False  # Bcoz we're missing a required word and this will just prevent us from wrongly
                                        # matching a different sentence
            break

    # Create a return statement of the fn. which returns us the accuracy of each sentence so they can later be compared
    # and return best response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0  # -> lowest possible value


# (4)
def check_all_messages(message):  # create a dictionary so highest prob list is going to equal this dict which is
    # just going to be an empty dict
    highest_prob_list = {}

    # Create a helper fn. which is going to simplify the response creation
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # all this fn. does is adding items to our dictionary which means we have a easier way to create a key and an
    # easier way to insert the value over here

    # Response ------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank You!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_ANS, ['what', 'you', 'can' 'do'], required_words=['you', 'do'])
    response(long.R_PLAY, ['play', 'you', 'games', 'cricket', 'football'], required_words=['play', 'games'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)  # Optional, just for showing percentage

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# (2)
def get_response(user_input):
    split_message = re.split(r'\s+|[,.?;:!-]\s*', user_input.lower())   # \s->check space, |->pipeline
    # This essentially removes all the symbols from the messages an allows us just to have the clean words separately

    response = check_all_messages(split_message)
    return response


# Testing the response system (1)
while True:
    print('Bot: ' + get_response(input(r'You: ')))
