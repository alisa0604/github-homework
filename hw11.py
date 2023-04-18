from fields import Field

class Record:
    def __init__(self, *args, **kwargs):
        self.fields = []
        for arg in args:
            self.fields.append(arg)
        for key, value in kwargs.items():
            self.fields.append(Field(key, value))

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = self.process(value)

    def process(self, value):
        phone_pattern = re.compile(r'^\+?(\d{2,3})?\s*\(*(\d{3})\)*[\.\-\s]*(\d{3})[\.\-\s]*(\d{2})[\.\-\s]*(\d{2})$')
        if not phone_pattern.match(value):
            raise ValueError('Invalid phone number')
        return value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()

class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        self.value = self.process(value)

    def process(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Invalid date')
        return value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.__str__()
    
class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def delete_record(self, record):
        self.records.remove(record)

    def iterator(self, n):
        for i in range(0, len(self.records), n):
            yield self.records[i:i+n]