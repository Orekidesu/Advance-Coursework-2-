
class ExpertSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def apply_rules(self):
        new_facts = set()
        flag = True
        while flag:
          flag = False
          for rule in self.rules:
              if "if" in rule and "then" in rule:
                  conditions, result = rule.split(", then ")
                  conditions = conditions.replace("if ", "").split(" and ")
                  if all(condition in self.facts for condition in conditions):
                      if not result in self.facts:
                        self.facts.add(result)
                        flag = True

    def get_known_facts(self):
        return self.facts

    def get_prev_rule(self):
        return self.rules

    def save_facts(self, filename):
        with open(filename, 'w') as file:
            for fact in self.facts:
                file.write(fact + '\n')

    def load_facts(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.facts.add(line.strip())
                print(line)
    def empty_facts(self,filename):
        file = open(filename,"r+")
        file.truncate(0)
        file.close
        self.facts.clear()

    def save_rules(self,filename):
        with open(filename,'w') as file:
            for rule in self.rules:
                file.write(rule + '\n')
    
    def load_rules(self,filename):
        with open(filename, 'r') as file:
            for line in file:
                self.rules.append(line.strip())
                print(line)
    def empty_rules(self,filename):
      file = open(filename,"r+")
      file.truncate(0)
      file.close
      self.facts.clear()

if __name__ == "__main__":
    expert = ExpertSystem()

    # SA PAG LOAD SA FILE
    try:
      print("=============Facts======================")
      expert.load_facts('facts.txt')
      print("=============END FACTS==================\n\n")
      print("=============RULES======================")
      expert.load_rules('rules.txt')
      print("=============END RULES==================\n")

      
    except FileNotFoundError:
      print("Walay File nakit an!!")


    while True:
        choice = input("Enter: \n\t[fact]\n\t[rule]\n\t[generate]\n\t[save_facts_rules]\n\t[empty_facts_rules]\n\t[exit]:\n-> ")
        if choice == 'fact':
            fact = input("Enter a new fact: ")
            if fact:
                expert.add_fact(fact)
            else:
                print("Tou kag maisahan ko nimu ha~, dili pwede empty boi")
        elif choice == 'rule':
            rule = input("Enter a rule in the form of 'if (condition) and (condition), then (result)': ")
            if rule:
                expert.add_rule(rule)
            else:
                print("Tou kag maisahan ko nimu ha~, dili pwede empty boi")
        elif choice == 'generate':
            expert.apply_rules()
            print("\n[Generated Facts]:")
            for fact in expert.get_known_facts():
                print(fact)
            print("\n")
            
            print("\n[Previously Inputted Rules]:")
            for rule in expert.get_prev_rule():
                print(rule)
            print("\n")
        elif choice == 'save_facts_rules':
            expert.save_facts('facts.txt')
            print("Facts saved!.")
            expert.save_rules('rules.txt')
            print("Rules saved!.")
    
        elif choice == 'empty_facts_rules':
            expert.empty_facts('facts.txt')
            expert.empty_rules('rules.txt')
            print("Matic wagtang!")
        elif choice == 'exit':
            break
        else:
            print("AYG PATAKA PISLIT LODS KABALO SENSITIVE TA, UTRO HAYSSSS")
