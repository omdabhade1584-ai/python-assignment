correct_pass = "some_pass"
not_found = True

while not_found:
    passw = input("Enter a pass:")
    if passw == correct_pass:
        not_found = False

print("Pass Matched")
       