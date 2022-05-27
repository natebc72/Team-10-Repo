class TerminalService:

    def __init__(self):
        #Seperatted each step into a picture which will disappear when there is a mistake.
        self._first_mistake = "  ___"
        self._second_mistake = " /___\ "
        #The third mistake is actually just the second line without the / and \.
        self._third_mistake = "  ___"
        self._fourth_mistake = " \   /"
        self._fifth_mistake = "  \ /"
        self._guy = "   o\n  /|\ \n  / \ "
        #Dead guy is used at the very end to represent a loss.
        self._dead_guy = "   x\n  /|\ \n  / \ "
        #Decided to combine all of the different pictures into an array so I could print it easier.
        self._whole_picture = [self._first_mistake, self._second_mistake, self._fourth_mistake, self._fifth_mistake, self._guy]
        self.num_wrong = 0
        
    #display function uses if statements to change the array and then displays it 
    def display(self):
        if self.num_wrong >= 1:
            self._whole_picture.remove("  ___")
        if self.num_wrong >= 2:
            #replaces second_mistake with third_mistake
            self._whole_picture[0] = self._third_mistake
        if self.num_wrong >= 3:
            self._whole_picture.remove("  ___")
        if self.num_wrong >= 4:
            self._whole_picture.remove(" \   /")
        if self.num_wrong >= 5:
            self._whole_picture.remove("  \ /")
            self._whole_picture[0] = self._dead_guy
        print(*self._whole_picture, sep='\n')

display = TerminalService()
display.display()