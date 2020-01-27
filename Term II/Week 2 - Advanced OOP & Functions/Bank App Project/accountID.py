# Though the name of the script is set as AccountID, this particular application or script
# will denote account number, first and last name of the account holder.count

class Account:
    transaction_counter = itertools.count(100)
    
    def __init__(self, account_number, first_name, last_name):
        # in practice we probably would want to add checks to make sure these values are valid / non-empty
        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def account_number(self):
        return self._account_number
    
    @property 
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError('First name cannot be empty.')
        self._first_name = value
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError('Last name cannot be empty.')
        self._last_name = value
        
    # also going to create a full_name computed property, for ease of use
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'