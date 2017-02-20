import datetime
import setting
import threading
import time
import tkinter
import tkinter.font as Tkfont

# 'default' time spent between each user key input
SLEEP_TIME = 0.5


class LIST_GUI():
    def __init__(self):
        # next_word is the word currently being typed by user
        self.__next_word = ""
        # rec is a list of recommended words
        self.__rec = []
        # num is a corresponding list of the word count of the recommended words
        self.__num = []
        # MAGIC_NUM is the number of recommended words
        self.__MAGIC_NUM = 0
        # the dictionary of words and corresponding word counts from user
        self.__dict = {}
        # number of words typed by user so far
        self.__num_words = 0
        # amount of time spent by user typing so far
        self.__old_time = 0.0
        # initialize the recommended words GUI
        self.__gui = tkinter.Tk()
        self.__btns = []
        self.__frames = []
        self.__mainframe = tkinter.Frame(self.__gui)
        self.__mainframe.grid(row=5, column=5)

        self.__butFont = tkinter.font.Font(size=36)
        self.__recFont = tkinter.font.Font(size=48)
        for idx in range(0, 5):
            self.__frames.append(tkinter.Frame(self.__mainframe))

        # initialize the customizable keypad buttons
        print(setting.SWITCH)
        print(setting.keys_poss[0])
        self.__btns.append(tkinter.Button(
            self.__frames[0],
            text="Switch",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[1],
            text="CapsLock",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[2],
            text="a",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[0],
            text="b",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[1],
            text="c",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[2],
            text="d",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[3],
            text="e",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[0],
            text="f",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[1],
            text="g",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[2],
            text="h",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[3],
            text="i",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[0],
            text="j",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[1],
            text="k",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[2],
            text="l",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[0],
            text="m",
            font=self.__butFont))
        self.__btns.append(tkinter.Button(
            self.__frames[2],
            text="n",
            font=self.__butFont))
        # the space button
        self.__btns.append(tkinter.Button(
            self.__frames[1], text="Space", font=self.__butFont))
        # the back button
        self.__btns.append(tkinter.Button(
            self.__frames[3], text="Back", font=self.__butFont))
        # the enter button
        self.__btns.append(tkinter.Button(
            self.__frames[3], text="Enter", font=self.__butFont))
        # packing the 'column 1' buttons
        self.packButtons([0, 3, 7, 11, 14])
        # packing the 'column 2' buttons
        self.packButtons([1, 4, 8, 12, 16])
        # packing the 'column 3' buttons
        self.packButtons([2, 5, 9, 13, 15])
        # packing the 'column 4' buttons
        self.packButtons([17, 6, 10, 18])
        # filename storing current profile
        self.__profile = ""
        # gets filename of last used profile
        with open("lastProfile.txt", "r") as check_prof:
            content = [line.rstrip('\n') for line in check_prof]
            self.__profile = str(content[0])
        check_prof.close()
        # gets information from last used profile
        with open(self.__profile, "r") as curr_prof:
            content = [line.rstrip('\n') for line in curr_prof]
            # title of the profile
            self.__gui.title(str(content[0]))
            # number of recommended words
            self.__MAGIC_NUM = int(content[1])
            idx = 0
            while idx < self.__MAGIC_NUM:
                # initialize recommended words to empty string
                self.__rec.append("")
                self.__num.append(0)
                # adds a button for each recommended word slot onto GUI
                self.__btns.append(
                    tkinter.Button(self.__frames[4],
                                   text=self.__rec[idx],
                                   font=self.__recFont))
                self.__btns[idx + 19].pack(fill="x")
                idx += 1
            self.__num_words = int(content[2].split(' ')[0])
            self.__old_time = float(content[2].split(' ')[1])
            # Stores the user profile's dictionary
            for i in range(3, len(content)):
                self.__dict[str(content[i].split(' ')[0])] = int(content[i].split(' ')[1])
        curr_prof.close()
        for i in range(0, len(self.__frames)):
            self.__frames[i].pack(side="left")

    # Called when user finishes typing / selecting a word
    def updateDict(self, event):
        print(event)
        # number of user's typed words gets incremented by 1
        self.__num_words += 1
        # update the word count of the typed word
        if event in self.__dict:
            self.__dict[event] += 1
        else:
            self.__dict[event] = 1
        # clear next_word back to the empty string
        self.__next_word = ""
        # reset the recommendation word list
        self.clearList()

    # rewrite keypad
    def changeKeypad(self):
        idx = 0
        if setting.SWITCH % 2 is 0:
            while idx < len(setting.keys_poss):
                self.__btns[idx].config(
                text=setting.PAGES[setting.SWITCH][
                    setting.keys_poss[idx]])
                self.__btns[idx].pack()
                idx += 1
        else:
            while idx < len(setting.keys_poss2):
                self.__btns[idx].config(
                    text=setting.PAGES[setting.SWITCH][
                        setting.keys_poss2[idx]])
                self.__btns[idx].pack()
                idx += 1

    # packs the buttons from num_list in a frame
    def packButtons(self, num_list):
        for num in num_list:
            self.__btns[int(num)].pack(fill="x")

    # Removes all recommended words from the GUI buttons
    def clearList(self):
        idx = 0
        while idx < self.__MAGIC_NUM:
            self.__rec[idx] = ""
            self.__num[idx] = 0
            idx += 1

    # Display each current recommended word on the GUI
    def updateList(self):
        idx = 0
        while idx < self.__MAGIC_NUM:
            self.__btns[idx + 19].config(text=self.__rec[idx])
            self.__btns[idx + 19].pack()
            idx += 1

    # Send untyped portion of word back to the OS
    def sendWord(self):
        pass

    # Calculates the difference in time between old and new (in minutes)
    def diffTime(self, old, new):
        sec = int(new.second) - int(old.second)
        if(sec < 0):
            sec += 60
        min = int(new.minute) - int(old.minute)
        if(min < 0):
            min += 60
        hr = int(new.hour) - int(old.hour)
        if(hr < 0):
            hr += 24
        return (sec / 60) + min + (60 * hr)

    # Starts the main GUI application
    def run(self):
        start_time = datetime.datetime.now().time()
        # Runs 'infinite' loop awaiting user input
        self.__gui.mainloop()
        # Calculates runtime of application
        add_time = self.diffTime(start_time, datetime.datetime.now().time())
        # Stores the cumulative runtime of the application over all user sessions
        new_time = self.__old_time + add_time
        with open(self.__profile, "r+") as close_prof:
            # Skips over the 'static' data
            for i in range(0, 2):
                close_prof.readline()
            # Sets file object to start writing over first line of 'dynamic' data
            close_prof.seek(close_prof.tell())
            # Update num_words, cumulative runtime, and words-per-minute in profile
            close_prof.write(str(self.__num_words) + " " +
                             str(new_time) + " " +
                             str(self.__num_words / new_time))
            # Stores word count of each word from dictionary in profile
            for word in self.__dict:
                close_prof.write('\n' + str(word) + " " +
                                 str(self.__dict[word]))
        close_prof.close()
        # Saves the filename of current profile
        with open("lastProfile.txt", "r+") as save_prof:
            save_prof.seek(0)
            save_prof.write(self.__profile)
        save_prof.close()

    # Checks if word contains the user's currently typed word
    def findWord(self, word, small_word):
        if word.find(small_word) == 0:
            return True
        else:
            return False

    def searchDict(self):
        # Clear list to get fresh list of recommended words for next_word
        self.clearList()
        # Search dictionary for every word that contains next_word
        for word in self.__dict:
            if self.findWord(word, self.__next_word):
                #print(word)
                idx = 0
                updated = False
                seen = False
                while not updated and (idx < self.__MAGIC_NUM) and not seen:
                    # word is already in recommended list, SKIP
                    if self.__rec[idx] is word:
                        seen = True
                    # word has better word count
                    elif self.__dict[word] > self.__num[idx]:
                        idx2 = self.__MAGIC_NUM - 1
                        while (idx2 > idx):
                            # Shifts recommended words down 1 ranking
                            self.__num[idx2] = self.__num[idx2 - 1]
                            self.__rec[idx2] = self.__rec[idx2 - 1]
                            idx2 -= 1
                        # Stores word at correct index of list
                        self.__num[idx2] = self.__dict[word]
                        self.__rec[idx2] = word
                        updated = True
                    # To compare with lower ranked recommendation word
                    idx += 1
        self.updateList()

    def auto_complete(self, event):
        # shorten currently typed word by 1 char if not the empty string
        if str(event) == "Back" and len(self.__next_word) > 0:
            self.__next_word = self.__next_word[0: len(self.__next_word) - 1]
        # switch to next mapping
        elif str(event) == "Switch":
            self.changeKeypad()
        # update word count of corresponding recommended word
        elif self.findWord(str(event), "rec")\
                and self.__rec[int(str(event)[3: len(str(event))])] is not "":
            self.updateDict(self.__rec[int(str(event)[3: len(str(event))])])
        # update user's currently typed word and search for new rec words
        elif str(event).isalnum() and len(str(event)) is 1:
            self.__next_word += str(event)
            self.searchDict()
        # update word count of user's currently typed word
        elif len(self.__next_word) > 0 and \
            str(event) != "CapsLock":
            self.updateDict(self.__next_word)

    def testAutoCom(self, *args):
        for file in args:
            # open each file and read it to simulate user input
            with open(str(file), "r") as open_input:
                lines = [line.rstrip('\n') for line in open_input]
                words = lines[0].split(' ')
                for word in words:
                    time.sleep(SLEEP_TIME)
                    # tests 'user input' on rec word list GUI system
                    self.auto_complete(str(word))
            open_input.close()


#if __name__ == "__main__":
#    app = LIST_GUI()
#    test = threading.Thread(target=app.testAutoCom,
#                            args=["sample_input1.txt",
#                                  "sample_input2.txt",
#                                  "sample_input3.txt"])
#    test.start()
#    app.run()
