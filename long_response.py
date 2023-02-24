import random

# 2) Adding very long response
R_EATING = "I don't like eating anything because I'm a bot obviously! :)"
R_ANS = "I'm a normal chatbot so I'll answer normal query but not other than this.. I apologize for that ! :("
R_PLAY = "If you want, I can play games like child level.. Haha but definetely you feel fun :)"

# 1)
def unknown():
    response = ['Could you re-phrase that?',
                "....",
                "Sounds about right",
                "What does that mean?"][random.randrange(4)]  # 4-> bcoz here in this file we have 4 response..
                                                              # if there is 7 response than randrange(7)
    return response
