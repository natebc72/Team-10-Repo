from actor import Actor

class Objects(Actor):
    """
    Marcos
 
    Assign each object a value
    """
    def __init__(self):
        """Constructs a new Actor."""
        super().__init__()
        self._type = ""
        self._value = ""
            
    def get_type(self):
        """Gets the Object type.
        
        Returns:
            string: The Obejct type Gem or Rock.
        """
        return self._type
    
    def set_type(self, type):
        """Updates the Object Type.
        
        Args:
            type (string): The Object Type Gem or Rock.
        """
        self._type = type
        
    def get_value(self):
        """Gets the Object type.
        
        Returns:
            string: The Obejct type Gem or Rock.
        """
        return self._value
    
    def set_value(self, value):
        """Updates the Object Type.
        
        Args:
            type (string): The Object Type Gem or Rock.
        """
        self._value = value

