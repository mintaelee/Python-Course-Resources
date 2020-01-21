class ShippingContainer:
    
    next_serial = 1337
    def __ini__(self, owner_code, contents):
        self,owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        
        
        
        