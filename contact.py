def create_contact(*args):
    print("Enter contact information")
    info = {}
    for arg in args:
        info[arg] = input('Type it %s: ' % arg)
    return info

def save_contact(**kwargs):
    arquivo = open('contacts.csv', 'a')
    arquivo.write(','.join(kwargs.values()))
    arquivo.write('\n')
    arquivo.flush()
    arquivo.close()


amount = input("How many contacts do you want to register? ")
amount = int(amount)
field = input("Enter the fields separated by commas: ")
field = field.split(',')
for i in range(amount):
    contact = create_contact(*field)
    save_contact(**contact)
