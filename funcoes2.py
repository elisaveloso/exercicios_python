# imprimir todos os elementos da lista numerando-os

def list_function(elements):
    counter = 0
    for x in elements:
        print(counter, ': ', elements[counter])
        counter = counter+1


#test = [655, 68465, 96151, 3956232, 546, 655]
#test = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
test = ["banana", "apple", "orange", "pepper",
        "mango", "pitaya", "lemon", "cucumber"]
list_function(test)
