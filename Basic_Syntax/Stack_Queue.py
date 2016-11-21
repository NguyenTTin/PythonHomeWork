__auth__ = 'NguyenTTin'

stack=list(input("\t\t\tEnter a infix expression "
                 "\nWhat you Want to exchange to prefix and post fix format:  \n"))

print(stack)
print(stack.count("("))

# def extract(stack):
#     if stack.count('(')==0:
#         pass
#     while stack.count('('):
#         stack.count('(')-=1
#         for i in range(int(len(stack))):
#             if stack[i]==('('):
#                 stack=stack[i+1:]
#                 for j in range(int(len(stack))):
#                     if stack[j]==')':
#                         stack=stack[:j]
#                     extract(stack)
#
#     print(stack)
#
#
# extract(stack)
