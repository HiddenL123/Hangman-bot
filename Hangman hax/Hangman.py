import tkinter as tk

window = tk.Tk()

setting = tk.Frame()
setting.pack()

word_count = 0
entry_count = 0
word_count_label = tk.Label(master = setting, text = "Word count", width = 10, height = 1)
word_counter = tk.Entry(master = setting, width = 3)
word_count_label.pack()
word_counter.pack()

word_list = []




setting.pack()

dictionary = open("words_alpha.txt")
len_to_word = {}
for line in dictionary:
    line = line.strip()
    if len(line) not in len_to_word:
        len_to_word[len(line)] = []
    len_to_word[len(line)].append(line)


class word_input():
    def __init__(self):
        self.letter_count = 0
        self.letter_counter = None
    def create(self):
        self.letter_counter = tk.Entry(master = word_input_frame, width = 3)
        self.letter_counter.pack(side = "left")
    def get_letter(self):

        try:
            return self.letter_counter.get()
        except:
            return None

letter_count_label = tk.Label(master = setting, text = "Letter count", width = 10, height = 1)
letter_count_label.pack()

words = []

word_input_frame_placeholder = tk.Frame()
word_input_frame_placeholder.pack()
word_input_frame = tk.Frame(master = word_input_frame_placeholder)


prev_letter_count = []
letter_count = []



letter_input_frame_placeholder = tk.Frame()
letter_input_frame_placeholder.pack()
letter_input_frame = tk.Frame(master = letter_input_frame_placeholder)

class word_:
    def __init__(self, letter_count, master):
        self.letters = []
        #print(len(self.letters))
        for i in range(letter_count):
            letter = tk.Entry(master = master, width = 3)
            letter.pack(side = "left")
            self.letters.append(letter)
        
    def get_word(self):
        if self.letters != [] and None not in self.letters:
            #print(len(self.letters))
            self_word = ""
            for letter in self.letters:
                try:
                    current = letter.get()
                except:
                    #print(len(self.letters))
                    current = "_"
                if current != "":
                    if len(current) == 1:
                        self_word += current
                else:
                    self_word += "_"
            return self_word

input_frame_placeholder = tk.Frame()
input_frame_placeholder.pack()
input_frame = tk.Frame(master = input_frame_placeholder)

word_input_label = tk.Label(master = input_frame_placeholder, text = "Word(s)", width = 10, height = 1)
word_input_label.pack()

wrong = tk.Frame()
wrong.pack()

wrong_label = tk.Label(master = wrong, text = "Wrong Guesses", width = 11, height = 1)
wrong_guesses = tk.Entry(master = wrong)
wrong_label.pack()
wrong_guesses.pack()

answer = tk.Frame()
answer.pack()

answer_label = tk.Label(master = answer)
answer_label.pack()



def update_word_count():
    global entry_count
    global word_input_frame
    global letter_input_frame
    global input_frame
    global letter_count
    global prev_letter_count
    global words
    try:
        word_count = word_counter.get().strip()
    except():
        word_count = None


    if word_count.isdigit() and str(word_count) != str(entry_count):
        word_count = int(word_count)
        for word in words:
            words.pop()
        word_input_frame.destroy()
        word_input_frame = tk.Frame(master = word_input_frame_placeholder)
        word_input_frame.pack()
        letter_input_frame.destroy()
        letter_input_frame = tk.Frame(master = letter_input_frame_placeholder)
        letter_input_frame.pack()
        input_frame.destroy()
        input_frame = tk.Frame(master = input_frame_placeholder)
        input_frame.pack()
        letter_count = []
        prev_letter_count = []
        entry_count = word_count
        words = []
        for i in range(word_count):
            new_word = word_input()
            new_word.create()
            words.append(new_word)
            
        entry_count = word_count
        
def update_letter_count():
    global prev_letter_count
    global letter_count
    valid = True
    if len(letter_count) == 0:
        valid = False
    letter_count = []
    
    if None not in words:
        for word_c in words:
            count = word_c.get_letter()
            if count != None:
                count = count.strip()
                if not count.isdigit():
                    valid = False
                letter_count.append(count)
    else:
        letter_count = []
        valid = False
    if valid and letter_count != prev_letter_count:
        global input_frame
        global word_list
        input_frame.destroy()
        input_frame = tk.Frame(master = input_frame_placeholder)
        input_frame.pack()
        if valid:
            word_list = []
            for i in range(len(letter_count)-1):
                count = letter_count[i]
                wrd = word_(int(count), input_frame)
                word_list.append(wrd)
                space = tk.Label(master = input_frame, text = "   ")
                space.pack(side = 'left')

            count = letter_count[len(letter_count)-1]
            wrd = word_(int(count), input_frame)
            word_list.append(wrd)
            
    if len(letter_count) == 0:
        valid = False
    prev_letter_count = letter_count

def solve(lst):
    candidate_words = []
    for guess_word in lst:
        candidate = []
        current_word = guess_word.get_word()
        if current_word != None:
            current_word = current_word.lower()
        else:
            return ""

        place_to_letter = {}
        length = len(current_word)
        if len(current_word) not in len_to_word:
            #print(len(current_word), len_to_word.keys())
            return "No solutions in length"
        
        for letter in range(length):
            if current_word[letter].isalpha():
                place_to_letter[letter] = current_word[letter]
        for en in len_to_word[length]:
            entry = en.lower().strip()
            correct_letter = True
            for place in range(len(entry)):
                if place in place_to_letter and place_to_letter[place] != entry[place]:
                    correct_letter = False
            if correct_letter and entry.isalpha():
                candidate.append(entry)
        if len(candidate) == 0:
            return "No solutions"
        candidate_words.extend(candidate)
    letter_to_occurrence = {}
    letter_to_total_occurrence = {}
    if len(candidate_words) == 1:
        return(candidate_words[0])
    for word in candidate_words:
        word_without_duplicate = ""
        for ch in word:
            if ch.isalpha() and ch not in word_without_duplicate:
                word_without_duplicate += ch
                letter_to_total_occurrence[ch] = 0
            letter_to_total_occurrence[ch] += 1
                
        for ch in word_without_duplicate:
            if ch not in letter_to_occurrence:
                letter_to_occurrence[ch] = 0
            letter_to_occurrence[ch] += 1
    max_letter = ""
    max_count = 0
    for letter in letter_to_occurrence:
        if letter not in current_word and letter not in wrong_guesses.get().lower():
            if letter_to_occurrence[letter] > max_count:
                max_count = letter_to_occurrence[letter]
                max_letter = letter
            elif letter_to_occurrence[letter] == max_count:
                if letter_to_total_occurrence[letter] > letter_to_total_occurrence[max_letter]:
                    max_letter = letter
    return max_letter
    
def check_solution():
    letter = solve(word_list).upper()
    answer_label.config(text = letter)




while True:
    update_word_count()
    if entry_count !=0:
        update_letter_count()
        check_solution()
    window.update()











