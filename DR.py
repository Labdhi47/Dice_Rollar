import random
x = "y"

while x == "y":
    random_number = random.randint(1, 6)

    if random_number == 1:
        print("[         ]")
        print("[    0    ]")
        print("[         ]")

    elif random_number == 2:
        print("[  0      ]")
        print("[         ]")
        print("[      0  ]")

    elif random_number == 3:
        print("[ 0       ]")
        print("[    0    ]")
        print("[       0 ]")

    elif random_number == 4:
        print("[ 0     0 ]")
        print("[         ]")
        print("[ 0     0 ]")

    elif random_number == 5:
        print("[ 0     0 ]")
        print("[    0    ]")
        print("[ 0     0 ]")

    elif random_number == 6:
        print("[  0   0  ]")
        print("[  0   0  ]")
        print("[  0   0  ]")

    x = input("Press y to roll again and Press any other key for Exit:")
