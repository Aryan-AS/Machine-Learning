import nlpcloud


class NLPapp:
    def __init__(self):
        self.__database = {}
        self.__first_menu()
    def __first_menu(self):
        first_input = input("""Hello! How would you like to proceed?
              1. Not a member? Register
              2. Already a member? Log in
              3. Exit
              """)
        if first_input =="1":
          self.__register()
        elif first_input=="2":
          self.__login()
        else:
           exit()
    def __second_menu(self):
        second_input = input("""Hello! How would you like to proceed?
              1. NER
              2. Language Detection
              3. Sentiment Analysis
              4. Logout
              """)
        if second_input=="1":
         self.__ner()
        elif second_input == "2":
           self.__language_detection()
        elif second_input =="3":
           self.__sentiment_anaylysis()
        else:
           exit()

    def __register(self):
        name = input("enter name")
        email = input("enter email")
        password = input("enter password")
        if email in self.__database:
           print("email already exists")
        else:
           self.__database[email]= [name,password]
           print("registernation succesfful")
           print(self.__database)
           self.__first_menu()

           
    def __login(self):
        email = input("enter email")
        password = input("enter password")
        if email in self.__database:
           if self.__database[email][1]==password:
              print("login successful")
              self.__second_menu()
           else:
              print("wrong passsword")
              self.__login()
        else:
           print("This email is not registered")
           self.__first_menu()
    def __ner(self):
       para = input("Enter the paragraph")
       search_term = input("What would you like to search?")
       client = nlpcloud.Client("finetuned-gpt-neox-20b", "2b58d7fb9af09e617ee525e78c7766b6d8c5bb61", gpu=True, lang="en")
       response = client.entities(para, searched_entity=search_term)
       print(response)
obj = NLPapp()