"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [1, 2, 3],
            "answer": 6
        },
        {
            "input": [2, 2, 2, 2, 2, 2],
            "answer": 12
        }
    ],
    "Extra": [

        {"input": [43, -10, 68, 84, 91, 71, -10, -80, 38], "answer": 295},
        {"input": [42], "answer": 42},
        {"input": [96, 26, 54, 21, 4], "answer": 201},
        {"input": [1, 37, -64, 57, -78, 57, 64, -38, -91, 61, 53, -89, 41], "answer": 11},
        {"input": [42, -24, -74, 96, -62, 5, -47], "answer": -64},
        {"input": [-55, -66], "answer": -121},
        {"input": [-30, -53, -2, 73, -27, -62, -49, 17, 99, -10, -31, -73, -67, -31], "answer": -246},
        {"input": [-34, 46, -22, -65, 92, 23, 99, 82], "answer": 221},
        {"input": [37, -22, 65, 65, -68, -84, -66, 82, -8, -53, -10, -73], "answer": -135},
        {"input": [93, 41, -19, -71, 26, -46, 56, -71, -26, 34, 11, -11], "answer": 17},
        {"input": [-53, 32, 7], "answer": -14},
    ]
}
