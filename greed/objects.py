from greed.actor import Actor

class Objects(Actor):
    """
    Marcos
 
    Assign each object a value
    """
    def __init__(self):
        """Constructs a new Actor."""
        self._type = ""
            
    def get_tyoe(self):
        """Gets the Object type.
        
        Returns:
            string: The Obejct type Gem or Rock.
        """
        return self._type
    
    def set_type(self, type):
        """Updates the Object Type.
        
        Args:
            type (string): The Objetct Type Gem or Rock.
        """
        self._type = type

