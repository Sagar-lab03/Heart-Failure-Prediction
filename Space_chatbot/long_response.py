import random

# 2) Adding very long response
R_PLANET = "Total 9 planets.. Venus, Mercury, Earth, Mars, Jupyter, Saturn, Uranus, Neptune and Pluto"
R_ANS = "I'm a normal chatbot for general space information.. so I'll answer normal space query."
R_LY = "A light-year is the distance that light travels in one year, which is approximately 5.88 trillion miles " \
       "(9.46 trillion kilometers)."
R_SN = "A supernova is a powerful and luminous explosion that occurs when a star has exhausted its nuclear fuel" \
       " and its core collapses, resulting in a massive shock wave that blows off the outer layers of the star."
R_BH = "A black hole is a region of spacetime where gravity is so strong that nothing, not even light, can escape " \
       "from it."
R_ST = "A star is a luminous sphere of plasma held together by its own gravity."
R_BB = "The Big Bang is the most widely accepted scientific theory about the origin of the universe."
R_S = "Space is defined as a boundless, three-dimensional continuum where objects can have relative positions, " \
      "directions and size."
R_ST = "There are 8,261 satellites orbiting the Earth as on January 2023, out of which only 4,852 satellites are active"
R_STS = "The temperature on the surface of the Sun is approximately 5,500 degrees Celsius (9,932 degrees Fahrenheit)"

R_NB = "A nebula is a cloud of gas and dust in outer space, visible in the night sky either as an indistinct bright" \
       " patch or as a dark silhouette against other luminous matter."
R_TBH = "Mainly, there are 3 types of Black Hole.. \n" \
        "1. Reissnar-Nordstrom Black hole \n" \
        "2. Karl Schwarzschild Black hole \n" \
        "3. Kerr Black hole"


# 1)
def unknown():
    response = ['Could you re-phrase that?',
                "I know only about general space information, sorry I don't about this..",
                ][random.randrange(2)]  # 2-> bcoz here in this file we have 2 response..
    # if there is 7 response than randrange(7)
    return response
