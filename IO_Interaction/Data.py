__auth__ = 'NguyenTTin'


def getRequest():
    while 1:
        request = int(input("Enter the number of request:  "))
        if 1<=request<=4:
            break
    return request

def shouldDisplay(accountType, balance):
    if accountType == 2 and balance < 0:
        return 1
    elif accountType == 3 and balance > 0:
        return 1
    elif accountType == 1 and balance ==0:
        return 1
    else:
        return 0

def outputLine(account, name, balance):
    print (account.ljust(10),)
    print (name.ljust(10),)
    print (balance.rjust(10))

try:
    file = open("client.dat", "r+")
except IOError:
    print("File could be opened!")

print("Enter request")
print("1 - List Account with Zero balance")
print("2 - List Account with Credit balance")
print("3 - List Account with Debit balance")
print("4 - End of Run")

while 1:
    request = getRequest()
    if request == 1:
        print ("Account with Zero balance")
    elif request == 2:
        print ("Account with Credit balance")
    elif request == 3:
        print ("Account with Debit balance")
    elif request ==4:
        break
    else:
        print("Invalid Request!!!")

    currentRecord = file.readline()
    while (currentRecord != ""):
        account, name, balance = currentRecord.split()
        balance = float(balance)
        if shouldDisplay(request, balance):
            outputLine(account, name, str(balance))
        currentRecord = file.readline()
        file.seek(0,0)
print("End of Run!")
file.close()
    
    
    
    
