class Journal:
    def __init__(self):
        self.entries  =[]
        self.count = 0

    def add_entry(self,text):
        self.entries.append(f"{self.count}:{text}")
        self.count+=1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    def save(self, filename):
        file = open(filename,"w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(selfself, uri):
        pass

class PersistenceManager:
        def save_to_file(selfjournal, filename):
            file = open(filename, "w")
            file.write(str(journal))
            file.close()

j = Journal()
j.add_entry("I cried today")
j.add_entry("I ate a bug today")
print(f"Jornal entries:\n{j}\n")

p = PersistenceManager()
file = r'/home/jyoti/Documents/output.txt'
p.save_to_file(j,file)

with open(file) as fh:
    print(fh.read())