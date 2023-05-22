class MyABC(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def show_all_contacts(self):
        pass

    @abstractmethod
    def add_record(self, record):
        pass

    @abstractmethod
    def find_records(self, query):
        pass

    @abstractmethod
    def delete_record(self, name):
        pass

    @abstractmethod
    def get_record_by_name(self, name):
        pass

    @abstractmethod
    def format_records(self, data):
        pass

    @abstractmethod
    def iterator(self, per_page):
        pass

