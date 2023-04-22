import pickle

def save_data_to_file(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data_from_file(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

class AddressBook:
    def __init__(self):
        self.contacts = []

    def find_contacts(self, search_str):
        result = []
        for contact in self.contacts:
            if search_str.lower() in contact.name.lower() or search_str in contact.phone:
                result.append(contact)
        return result