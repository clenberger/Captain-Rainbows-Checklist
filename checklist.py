print("Hello World")

#initialize checklist
checklist = list()
checklist.append('Blue')
print(checklist)
checklist.append('Orange')
print(checklist)

#create function
def create(item):
        checklist.append('Blue')

#read function
def read(index):
        return checklist[index]

#update function
def update(index, item):
        checklist[index] = item

#destroy function
def destroy(index):
        checklist.pop(index)

#list all items function
def list_all_items():
        index = 0
        for list_item in checklist:
                print(str(index) + list_item)
                index += 1

#mark completed function
def mark_completed(index):
        for list_item in checklist:
                print ("√ {}".format(list_item))

#user input function
def user_input(prompt):
        user_input = input(prompt)
        return user_input


#select function
def select(function_code):

        #create item
        if function_code == "C":
                input_item = user_input ("Input item:")
                create(input_item)

        #read item
        elif function_code == "R":
                item_index = user_input("Index Number?")
                item = read(int(item_index))  
                print(item)

        #print all items
        elif function_code == "P":
                list_all_items()

        #quitting
        elif function_code == "Q":
                return False

        elif function_code == "U":
                update_index = user_input("Index number?")
                update_item = user_input("New item")
                update(int(update_index), update_item)

        elif function_code == "D":
                index = int(user_input("Index:"))
                destroy(index)
        #catch all
        else:
                print("Unknown Option")

        return True

running = True
while running:
        selection = user_input(
                "Press C to add to list, R to Read from list, P to display list, Q to quit, U to update an index and D to delete an index")
        running = select(selection)


#test function
def test():
        create("purple sox")
        create("red cloak")

        print(read(0))
        print(read(1))

        update(0, "purple socks")
        destroy(1)

        print(read(0))
        print(read(1))

        select("C")

        list_all_items()

        select("R")

        list_all_items()


#calling test
# test()