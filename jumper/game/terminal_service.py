class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
    def __init__(self):
        #Seperatted each step into a picture which will disappear when there is a mistake.
        self.first_mistake = "  ___"
        self.second_mistake = " /___\ "
        #The third mistake is actually just the second line without the / and \.
        self.third_mistake = "  ___"
        self.fourth_mistake = " \   /"
        self.fifth_mistake = "  \ /"
        self.guy = "   o\n  /|\ \n  / \ "
        #Dead guy is used at the very end to represent a loss.
        self.dead_guy = "   x\n  /|\ \n  / \ "
        #Decided to combine all of the different pictures into an array so I could print it easier.
        self.whole_picture = [self.first_mistake, self.second_mistake, self.fourth_mistake, self.fifth_mistake, self.guy]

        #display function uses if statements to change the array and then displays it 
    def display(self, num_wrong):
        if num_wrong >= 1:
            self.whole_picture.remove("  ___")
        if num_wrong >= 2:
            #replaces second_mistake with third_mistake
            self.whole_picture[0] = self.third_mistake
        if num_wrong >= 3:
            self.whole_picture.remove("  ___")
        if num_wrong >= 4:
            self.whole_picture.remove(" \   /")
        if num_wrong >= 5:
            self.whole_picture.remove("  \ /")
            self.whole_picture[0] = self.dead_guy
        print(*self.whole_picture, sep='\n')

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
    
    
    
        
