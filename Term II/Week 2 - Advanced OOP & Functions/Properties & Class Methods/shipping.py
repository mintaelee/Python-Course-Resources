class ShippingContainer:
    
    next_serial = 1337

# checkpoint 2
# work on terminal
   
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result
    
 # Part 1   
    def __ini__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        self.next_serial += 1
        #ShippingContainer.next_serial += 1

# Checkpoint   1     
# Work on terminal 
       
        
        