# チャレンジ問題　p.69

#1
##def squared(i):
##    try:
##        return i ** 2
##    except(ZeroDivisionError, ValueError):
##        print("INvalid input.")
##    """
##    Takes an int and returns it multiplied by 2.
##    :param i: int.
##    :return x multiplied by 2.
##    """
##print(squared(3))

#2
##def string(s):
##    """
##    Prints the string passed in.
##    :param s: str. 
##    """
##    print(s)
##string(" あいうえお")


#3
##def add_multi(v, w, x, y=100, z=200,):
##    """
##    Return the result of the addition
##    of three required params and two optional params.
##    :param v: int.
##    :param w: int.
##    :param x: int.
##    :param y: int.
##    :param z: int.
##    :return: int.
##    """
##    return v + w + x + y + z
##result = add_multi(1, 2, 3)

#4
##def half(i):
##    return i / 2
##n = int(half(4))
##def fourth(k):
##    return k * 4
##l = fourth(n)
##print(l)

##def divide(x):
##    return x / 2
##def multiply(x):
##    return x * 4
##y = divide(4)
##z = multiply(y)
##print(z)

#5
##def convert(string):
##    """
##    Converts passed in str to int.
##    :param string: str.
##    :return: string converted to int 
##    """
##    try:
##        return float(string)
##    except ValueError:
##        print("Could not convert the string to a float")
##print(convert("aa"))
    
#6  上に書いた
#    関数の目的　必要な引数の種類


##p.87

##1
##my_favorite_musician = [" 放課後ティータイム","fripSide"," 感覚ピエロ"]



##2
##place = [(36.04, 138.11), (34.68, 135.53)]

##3
##my_feature = {
##    "height":  168,
##    "weight": 50,
##    "favorite_color": "white",
##    "favorite_artist": "fripSide",
##    }


##4
##answer = input("type height or weight or favorite color or favorite artist:")
##if answer in my_feature:
##    result = my_feature[answer]
##    print(result)


## my_favorite_musician_music = {
##    " 放課後ティータイム": " ふわふわ時間",
##    "fripSide": "only my railgun",
##    "感覚ピエロ": " ハルカミライ",
##     }


##p.102

##1
##name = "カミュ"
##print(name[0]) 
##print(name[1])
##print(name[2])

##2
##write = input("What?")
##send = input("Who?")
##r = " 私は昨日{}を書いて、{}に送った。".format(write, send)
##print(r)


##3
##r = "aldous Huxly was born in 1849.".title()
##print(r)

##4   
##a = "どこで？　誰が？　いつ？"
##print(a.split("　"))

##5
##sentence = ["The", "fox", "jumped", "over", "the", "fence", "."]
##print(" ".join(sentence).replace(" .", "."))

##6
##sentence = "A screaming comes across the sky."
##print(sentence.replace("s", "$"))

##7
##print("Hemingway".index("m"))

##8

##print("'I think therefore I am.'")


##9
##print("three" + " three" + " three")
##print("three " * 3)

##10
##sentence = " 四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
##sentence_list = sentence.split("を")
##print(sentence_list[0])


##p.116

##1
##list = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
##for i in list:
##    print(i)

##2
##for i in range(25, 51):
##    print(i)
##i = 25
##while 25 <= i <= 50:
##    print(i)
##    i += 1

##3
##n = 0
##for i in list:
##    i = str(i)
##    print(str(n) +":" + i)
##    n += 1
##
##shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
##for index, show in enumerate(shows):
##    print(index)
##    print(show)

##4
##correct_num = [8, 16, 26, 31, 77]
##your_num = input("Type a number from 0 to 100. If you quit this game, type q.")
##int_your_num = int(your_num)
##if int_your_num in correct_num:
##    print("That's correct!")
##elif your_num = q:/
##    print("This game is end.")
##    break
##else:
##    print("That's not correct.")
##    your_num = input("Type a number from 0 to 100. If you quit this game, type q.")

##correct_nums = [8, 16, 26, 31, 77]
##
##while True:
##    answer = input("Guess a number or type q to quit.")
##    if answer == "q":
##        print("END")
##        break
##    if int(answer) in correct_nums:
##        print("You guessed correctly!")
##        break
##    else:
##        print("You guessed incorrectly!")
##    try:
##        answer = int(answer)
##    except ValueError:
##        print("Please type a number or q to quit.")

##numbers = [11, 32, 33, 15, 1]
##
##while True:
##    answer = input("Guess a number or type q to quit.")
##    if answer == "q":
##        break
##    try:
##        answer = int(answer)
##    except ValueError:
##        print("please type a number or q to quit.")
##    if answer in numbers:
##        print("You guessed correctly!")
##    else:
##        print("You guessed incorrectly!")
        
##5

##list1 = [8, 19, 148, 4]
##list2 = [9, 1, 33, 83]
##new_list = []
##for item1 in list1:
##    for item2 in list2:
##        new_list.append(item1 + item2)
##
##print(new_list)


##p.123

##1
##import statistics
##date = [1, 2, 33, 912, 2212, 1234, 13, 0, 0]
##print(statistics.mode(date))


##2
##import cubed
##result = cubed.cube_it(3)
##print(result)

##with open("cubed.py", "w") as f:
##    f.write("Hi from Python!")
##
##with open("cubed.py", "r") as f:
##    print(f.read())

##p.132

##2
##answer = input("Do you like python?:")
##with open("answer.py","w") as f:
##    f.write(answer)

##3,4
##import csv
##movies = [["トップガン", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
##with open("movies.csv", "w",) as csvfile:
##    spamwriter = csv.writer(csvfile, delimiter =",")
##    for movie_list in movies:
##        spamwriter.writerow(movie_list)

##print(list("list" * 3))

##import random
##
##def hangman():
##    words = ["cat", "dog", "dragon", "hamster", "ant", "butterfly", "beetle"]
##    k = random.randint(0, len(words) - 1)
##    word = words[k]
##    wrong = 0
##    stages = ["",
##             "________        ",
##             "|               ",
##             "|        |      ",
##             "|        0      ",
##             "|       /|\     ",
##             "|       / \     ",
##             "|               "
##              ]
##    rletters = list(word)
##    board = ["__"] * len(word)
##    win = False
##    print("Welcome to Hangman")
##    while wrong < len(stages) - 1:
##        print("\n")
##        msg = "Guess a letter"
##        char = input(msg)
##        if char in rletters:
##            cind = rletters \
##                   .index(char)
##            board[cind] = char
##            rletters[cind] = '$'
##        else:
##            wrong += 1
##        print((" ".join(board)))
##        e = wrong + 1
##        print("\n"
##              .join(stages[0: e]))
##        if "__" not in board:
##            print("You win!")
##            print(" ".join(board))
##            win = True
##            break
##    if not win:
##        print("\n"
##              .join(stages[0: \
##              wrong]))
##        print("You lose! It was {}."
##              .format(word))
##
##hangman()


##p.156
##1
##class Apple:
##    def __init__(self, w, c, sw, se)
##        self.weight = w
##        self.color = c
##        self.sweet = sw
##        self.seze = se
##2
##import math
##
##class Circle:
##    def __init__(self, r):
##        self.radious = r
##    def area(self):
##        return self.radious ** 2 * math.pi
##circle1 = Circle(10)
##print(circle1.area())
##3
##class Triangle:
##    def __init__(self, b, h):
##        self.bottom = b
##        self.height = h
##
##    def area(self):
##        return self.bottom * self.height / 2
##
##a_triangle = Triangle(10, 4)
##print(a_triangle.area())
##4
##class Hexagon:
##    def __init__(self, s):
##        self.side = s
##    def calculate_parimeter(self):
##        return self.side * 6
##a_hexagon = Hexagon(3)
##print(a_hexagon.calculate_parimeter())

##p.169
##1
##class Rectangle:
##    def __init__(self, w, h):
##        self.width = w
##        self.height = h
##    def calculate_perimeter(self):
##        return (self.width + self.height) * 2
##        
##class Square:
##    def __init__(self, s):
##        self.side = s
##    def calculate_perimeter(self):
##        return self.side * 4
##
##
##a_rectangle = Rectangle(10, 3)
##a_square = Square(5)
##print(a_rectangle.calculate_perimeter())
##print(a_square.calculate_perimeter())

##2
##class Square:
##    def __init__(self, w, h):
##        self.width = w
##        self.height = h
##        
##    def calculate_perimeter(self):
##        return (self.width + self.height) * 2
##    
##    def change_size(self, wp):
##        self.width_plus = wp
##        self.width += self.width_plus
##        
##a_square = Square(10, 10)
##print(a_square.width)
##
##a_square.change_size(5)
##print(a_square.width)
##3

##class Shape:
##    def what_am_i(self):
##        print("I am a shape.")
##
##class Rectangle(Shape):
####    def __init__(self, w, h):
####        self.width = w
####        self.height = h
####    def calculate_perimeter(self):
####        return (self.width + self.height) * 2
##    pass
##        
##class Square(Shape):
####    def __init__(self, s):
####        self.side = s
####    def calculate_perimeter(self):
####        return self.side * 4
##    pass
##    
##a_rectangle = Rectangle()
##a_square = Square()
##
##a_rectangle.what_am_i()
##a_square.what_am_i()

##4
##class Horse:
##    def __init__(self, name, owner):
##        self.name = name
##        self.owner = owner
##
##class Rider:
##    def __init__(self, name):
##        self.name = name
##        
##kt = Rider("kota")
##print(kt.name)
##a_horse = Horse("bolt", kt)
##print(a_horse.owner.name)

##p.177
##1
##class Square:
##    square_list = []
##
##    def __init__(self, s):
##        self.side = s
##        self.square_list.append((self.side))
##        
##                                
##
##a_square = Square(10)
##b_square = Square(8)       
##c_square = Square(5)
##
##print(Square.square_list)


##2
    
##class Square:
##    square_list = []
##    
##    def __init__(self, s):
##        self.side = s
##        self.square_list.append((self.side))
##
##a_square = Square(10)
##b_square = Square(8)       
##c_square = Square(5)
##
####print(Square.square_list)
##
##for l in Square.square_list:
##    print("{} by {} by {} by {}".format(l, l, l, l))

##def compare(obj1, obj2):
##    return obj1 is obj2
##
##print(compare(1, 2))
##print(compare(1, 1))

# list = [(10, 2), (2, 3), (2, 2)]
# item1 = list[1]

# print(item1)

# print()



# War Game
# from random import shuffle
# # カードを表すクラス
# class Card:
#     # クラス変数
#     suits = ["spades", "hearts", "diamonds", "clubs"]
#     values = ["None", "None","2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "KIng", "Ace"]

#     def __init__(self, s, v):
#         self.suit = s
#         self.value = v

#     def __repr__(self):
#         s = self.values[self.value] + " of " + self.suits[self.suit]
#         return s

# # デッキを表すクラス
# class Deck:
#     def __init__(self):
#         self.cards = []
#         for i in range(2, 15):
#             for j in range(0, 4):
#                 self.cards.append((i, j))
# # self.cards = [(3, 0). (4, 1) (2, 2), ....]
#         shuffle(self.cards)

#     def rm_card(self):
#         # if len(self.cards) == 0:
#         #     return None
#         return self.cards.pop()
# # print(Deck().rm_card())

# # プレイヤーを表すクラス
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.wins = 0
#         # self.card = None
    
# # ゲームを表すクラス
# class Game:
#     def __init__(self):
#         name1 = input("プレイヤー1の名前")
#         name2 = input("プレイヤー2の名前")
# # Deckオブジェクトを作ってインスタンス変数deckに格納
#         self.deck = Deck()
# # 入力されたプレイヤーの名前をp1,p2に格納
#         self.p1 = Player(name1)
#         self.p2 = Player(name2)

#     def wins(self, winner):
#         w = "このラウンドは {} が勝ちました"
#         w = w.format(winner)
#         print(w)

#     def draw(self, p1n, p1c, p2n, p2c):
#         d = "{} は {}、 {} は {} を引きました"
#         d = d.format(p1n, p1c, p2n, p2c)
#         print(d)

#     def play_game(self):
#         # ?
#         cards = self.deck.cards
#         print("戦争を始めます！")
#         while len(cards) >= 2:
#             response = input("q で終了、それ以外のキーでPlay")
#             if response == "q":
#                 break
#             p1c = self.deck.rm_card()
#             p2c = self.deck.rm_card()
#             p1n = self.p1.name
#             p2n = self.p2.name
#             self.draw(p1n, p1c, p2n, p2c)
#             if p1c > p2c:
#                 self.p1.wins += 1
#                 self.wins(self.p1.name)
#             else:
#                 self.p2.wins += 1
#                 self.wins(self.p2.name)

#         win = self.winner(self.p1, self.p2)
#         print("ゲーム終了、{} の勝利です".format(win))

#     def winner(self, p1, p2):
#         if p1.wins > p2.wins:
#             return p1.name
#         if p1.wins < p2.wins:
#             return p2.name
#         return "引き分け"

# game = Game()
# game.play_game()
# import re

# # text = "Arizona 479, 501, 870. California 209, 213, 650."
# # nums = re.findall("\d", text, re.IGNORECASE)
# # print(nums)

# text = "The ghost that says boo haunts the loo"
# t = re.findall(".oo", text, re.IGNORECASE)
# print(t)

# import re


# text = """Giraffes have aroused
#  the curiosity of __PLURAL_NOUN__
#  since earliest times. The
#  giraffe is the tallest of all
#  living __PLURAL_NOUN__, but
#  scientists are unable to
#  explain how it got its long
#  __PART_OF_THE_BODY__. The
#  giraffe's tremendous height,
#  which might reach __NUMBER__
#  __PLURAL_NOUN__, comes from
#  it legs and __BODYPART__.
# """


# def mad_libs(mls):
#     """
#     :param mls: String
#     with parts the user
#     should fill out surrounded
#     by double underscores.
#     Underscores cannot
#     be inside hint e.g., no
#     __hint_hint__ only
#     __hint__.
#     """
#     hints = re.findall("__.*?__", mls)
#     if hints is not None:
#         for word in hints:
#             q = "Enter a {}".format(word)
#             new = input(q)
#             mls = mls.replace(word, new, 1)
#         print('\n')
#         mls = mls.replace("\n", "")
#         print(mls)
#     else:
#         print("invalid mls")

# mad_libs(text)

# class Stack:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return self.items == []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[-1]

#     def size(self):
#         return len(self.items)


# stack = Stack()
# stack.size()
# for c in "yesterday":
#     stack.push(c)

# reverse = ""
# while stack.size():
#     reverse += stack.pop()

# print(reverse)

# stack = Stack()

# for i in range(1, 6):
#     stack.push(i)

# reverse = []

# for c in range(len(stack.items)):
#     reverse.append(stack.pop())

# print(reverse)

# for i in range(1, 101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0 and i % 15 != 0:
#         print("Fizz")
#     elif i % 5 == 0 and i % 15 != 0:
#         print("Buzz")
#     else:
#         print(i) 





















