import re
import long_response as s_long


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
    response('Hello! Welcome to the space chatbot! How can I help you ?', ['hello', 'hi', 'hey'],
             single_response=True)

    response('I\'m doing fine, How can I help you', ['how', 'are', 'you', 'doing'], required_words=['how', 'you',
                                                                                                    'doing'])

    response('3,84,400 Km', ['distance', 'moon'], single_response=True)
    response('3 x 10^8 Km per second', ['speed', 'light'], single_response=True)
    response('Approximately 1.99 x 10^30 kilograms', ['mass', 'sun'], single_response=True)
    response('Approximately 100,000 light-years.', ['diameter', 'milky', 'way', 'galaxy'], single_response=True)
    response('150 million Km', ['distance', 'sun', 'earth'], single_response=True)
    response('Ap', ['distance', 'moon'], single_response=True)
    response('3,84,400 Km', ['distance', 'moon'], single_response=True)
    response('3,84,400 Km', ['distance', 'moon'], single_response=True)
    response('3,84,400 Km', ['distance', 'moon'], single_response=True)
    response('3,84,400 Km', ['distance', 'moon'], single_response=True)
    response(s_long.R_STS, ['sun', 'surface', 'temperature'], single_response=True)




    response('Milkyway galaxy', ['live', 'galaxy', 'name'], required_words=['galaxy'])
    response('Andromeda galaxy', ['neighbour', 'galaxy', 'name'], required_words=['neighbour', 'galaxy'])
    response('1 Million $', ['telescope', 'cost'], required_words=['telescope'])
    response('Alpha Centuri, 4.3 light years away from Earth ', ['closest', 'star'], required_words=['star', 'closest'],
             single_response=True)

    response('Saturn has 83 moons', ['saturn', 'moons'], required_words=['saturn', 'moons'])
    response('Jupiter has around 92 moons', ['jupiter', 'moons'], required_words=['jupiter', 'moons'])
    response('Uranus has 27 moons', ['jupiter', 'moons'], required_words=['uranus', 'moons'])
    response('Neptune has 14 moons', ['neptune', 'moons'], required_words=['neptune', 'moons'])
    response('Phobos and Deimos', ['mars', 'moons'], required_words=['mars', 'moons'])
    response('Sirius (also known as "Dog Star"), 8.6 light years distance from Earth ', ['brightest', 'star'],
             required_words=['brightest', 'star'])
    response('Stephenson 2-18, 20,000 light years away from Earth', ['largest', 'star'], required_words=['largest', 'star'])
    response('Between 100 to 200 Billion galaxies', ['how', 'many', 'galaxies', 'universe'],
             required_words=['how', 'many', 'galaxies'])
    response('approximately 13.8 billion years old', ['old', 'universe'], required_words=['old', 'universe'])

    response('1 Million $', ['telescope', 'cost'], required_words=['telescope'])
    response('1 Million $', ['telescope', 'cost'], required_words=['telescope'])
    response('1 Million $', ['telescope', 'cost'], required_words=['telescope'])
    response('1 Million $', ['telescope', 'cost'], required_words=['telescope'])

    # response('Milkyway galaxy', ['how', 'are', 'you', 'doing'], required_words=['how'])

    response(s_long.R_PLANET, ['planets', 'solar', 'system'], required_words=['planets'])
    response(s_long.R_SN, ['supernova'], required_words=['supernova'])
    response(s_long.R_LY, ['light', 'year'], required_words=['light', 'year'])
    response(s_long.R_NB, ['nebula'], required_words=['nebula'])
    response(s_long.R_SN, ['supernova'], required_words=['supernova'])
    response(s_long.R_BB, ['big', 'bang'], required_words=['big', 'bang'])
    response(s_long.R_S, ['what', 'space', 'technology'], required_words=['space'])
    response(s_long.R_TBH, ['types', 'black', 'hole'], required_words=['types', 'black', 'hole'])
    response(s_long.R_BH, ['black', 'hole'], required_words=['black', 'hole'])
    response(s_long.R_ST, ['total', 'satellites', 'orbits', 'sky', 'earth'], required_words=['satellites', 'orbits',
                                                                                             'earth'])
    response(s_long.R_BB, ['big', 'bang'], required_words=['big', 'bang'])

    response('Glad, I am able to help you :)', ['thank', 'you'], required_words=['thank', 'you'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)  # Optional, just for showing percentage

    return s_long.unknown() if highest_prob_list[best_match] < 1 else best_match


# (2)
def get_response(user_input):
    split_message = re.split(r'\s+|[,.?;:!-]\s*', user_input.lower())  # \s->check space, |->pipeline
    # This essentially removes all the symbols from the messages an allows us just to have the clean words separately
    # user_input = user_input.replace("′", "'").replace("won't", "will not").replace("cannot", "can not")\
    #                        .replace("can't", "can not").replace("n't", " not").replace("what's", "what is")\
    #                        .replace("it's", "it is").replace("'ve", " have").replace("i'm", "i am")\
    #                        .replace("'re", " are").replace("it's", "it is").replace("'s", " own")\
    #                        .replace("%", " percent ").replace("$", " dollar ").replace("€", " euro ")\
    #                        .replace("'ll", " will")

    response = check_all_messages(split_message)
    return response


# Testing the response system (1)
while True:
    print('Bot: ' + get_response(input(r'You: ')))
