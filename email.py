
def remove_space(phonenum):
    phonenum = phonenum.strip()
    return phonenum
def find(email):
    where = email.find("@")
    p1 = email[:where]
    p2 = email[where + 1:]
    return p1, p2
def is_valid(email):
    if "@" in email:
        where = email.find("@")
        if where > 0 and where < len(email) - 1:
            return True
    return False

ma = (input("Email: "))
clean_email = remove_space(ma)

# main function
if is_valid(clean_email) == False:
    print("Invalid email")
else:
    p1, p2 = find(clean_email)
    print(f"Username: {p1}\nDomain: {p2}")

