myList = []

while True:
  print("1. Append an element")
  print("2. Insert an element")
  print("3. Append a list")
  print("4. Modify an element")
  print("5. Delete an element by position")
  print("6. Delete an element by value")
  print("7. Sort in Ascending") 
  print("8. Sort in decending")
  print("9. Display the list")
  print("10. Exit")

  choice = int(input("Select the function: "))
  
  if choice == "1":
    element = int(input("Enter element to be appended: "))
    myList.append(element)
    print("Sucess!")
    
  elif choice == "2":
    element = int(input("Enter the element to be inserted: "))
    pos = int(input("Enter the position: "))
    myList.insert(pos,element)
    print("Sucess!")
    
  elif choice == "3":
    nElement = int(input("Enter the number if elements in the list: "))
    for i in range(0, nElement):
      element = int(input("Enter the element: "))
      MyList.append(element)
    print("Sucess!")
    
  elif choice == "4":
    posElement = int(input("Enter the position of the element to be modified: "))
    newElement = int(input("Enter the new element: "))
    oldElement = myList[posElement]
    myList[posElement] = newElement
    print("Sucess!")
    
  elif choice == "5":
    posElement = int(input("Enter the index of the element to be deleted: "))
    myList.pop(posElement)
    print("Sucess!")
    
  elif choice == "6":
    valElement = int(input("Enter the value of the element to be deleted: "))
    myList.remove(valElement)
    print("Sucess!")
    
  elif choice == "7":
    myList.sort()
    print("Sucess!")
    
  elif choice == "8":
    myList.sort(reverse=True)
    print("Sucess!")
    
  elif choice == "9":
    print(myList)
    
  elif choice == "10":
    print("Kindly fuck off!")
    break
