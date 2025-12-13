# a security key used for securing the data

key = 123

# function for encrypting the data
def encryt(file_data):

    l =[]
    for x in file_data:
        new_x = x^key
        l.append(new_x)

    return bytes(l)      

#function for decryption
def decrypt(file_data):
    l=[]
    for x in file_data:
        new_x = x^key
        l.append(new_x)

    return bytes(l)

