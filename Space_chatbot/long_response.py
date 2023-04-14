import random

# 2) Adding very long response
R_PLANET = "Total 9 planets.. Venus, Mercury, Earth, Mars, Jupyter, Saturn, Uranus, Neptune and Pluto"
R_ANS = "I'm a normal chatbot for general space information.. so I'll answer normal space query."
R_SN = "A supernova is a powerful and luminous explosion that occurs when a star has exhausted its nuclear fuel" \
       " and its core collapses, resulting in a massive shock wave that blows off the outer layers of the star."
R_BH = "A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape " \
       "from it."
R_ST = "A star is a luminous sphere of plasma held together by its own gravity."
R_BB = "The Big Bang is the most widely accepted scientific theory about the origin of the universe."
R_S = "Space is defined as a boundless, three-dimensional continuum where objects can have relative positions, " \
      "directions and size."
R_NB = "A nebula is a cloud of gas and dust in outer space, visible in the night sky either as an indistinct bright" \
       " patch or as a dark silhouette against other luminous matter."

# 1)
def unknown():
    response = ['Could you re-phrase that?',
                "I know only about general space information, sorry i cannot do this",
                ][random.randrange(2)]  # 4-> bcoz here in this file we have 4 response..
                                                              # if there is 7 response than randrange(7)
    return response
