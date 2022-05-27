class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    def __init__(self):
        #Separated each step into a picture which will disappear when there is a mistake.
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
        self._num_wrong = 0
        
    #display function uses if statements to change the array and then displays it 
    def remove_chute(self):
        if (self._num_wrong == 1) | (self._num_wrong == 3) | (self._num_wrong == 4):
            self._whole_picture.remove(self._whole_picture[0])
        elif self._num_wrong == 2:
            #replaces second_mistake with third_mistake
            self._whole_picture[0] = self._third_mistake
        elif self._num_wrong == 5:
            self._whole_picture.remove(self._whole_picture[0])
            self._whole_picture[0] = self._dead_guy
        elif self._num_wrong <=0:
            self._whole_picture = self._whole_picture
        return self._whole_picture
        #display function uses if statements to change the array and then displays it 
    def get_num_wrong(self):
        return self._num_wrong

    def set_num_wrong(self,num_mistake):
        self._num_wrong = num_mistake

    def display(self):
        print()
        print(*self._whole_picture, sep='\n')

    def display_word(self, word):
        for i in word:
            print(i,end=" ")
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))
        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)
    
    
    
        
