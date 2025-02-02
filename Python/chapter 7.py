# f = open("demo.txt","r+")
# f.write("abc")
# print(f.read())
# f.close()





# f = open("demo.txt","r+")
# f.write("abcfddkhgfhg")
# print(f.read())
# f.close()

# import os

# os.remove("demo.txt")




# with open("practice.txt","w") as f:
#     f.write("Hi everyone\n")
#     f.write("we are learning File I/O\n")
#     f.write("using Java\n")
#     f.write("I like programming in Java\n")



# with open("practice.txt","r") as f:
#     data = f.read()

# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt","w") as f:
#     data = f.write(new_data)




# with open("practice.txt", "r") as f :
#     data = f.read()
# if data.find("learning"):
#     print("Yes")
# else:
#     print("No")


# word = "learning"

# with open("practice.txt","r") as f:
#     data = f.readline()
#     if data.find(word) == True:
#         print("line 1")
#     else:
#         data = f.readline()
#         if data.find(word) == True:                           #Not Working
#             print("line 2")
#         else:
#             data = f.readline()
#             if data.find(word) == True:
#                 print("line 3")
#             else:
#                 data = f.readline()
#                 if data.find(word) == True:
#                     print("line 4")
#                 else:
#                     print("Not Found")
            



# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f :
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no +=1
#     return -1

# print(check_for_line())



# with open("practice.txt","r") as f :
#     data = f.read()
    
    



































































