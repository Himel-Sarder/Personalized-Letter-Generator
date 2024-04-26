# Mail Marge Project

# Himel Sarder
# Dept. of CSE, BSFMSTU, Bangladesh
# gmail : info.himelcse@gmail.com
# Linkedin : Himel Sarder

with open("Containers/Names_container.txt") as Name_File:
    Name = Name_File.readlines()
    #for n in Name:
        #StripedName = n.strip()
        #print(StripedName)


PLACEHOLDER = "[NAME]"

with open("Containers/Letter_container.txt") as Letter_File:
    Letter = Letter_File.read()
    #print(Letter)

    for name in Name:
        stripped_name = name.strip()

        new_letter = Letter.replace(PLACEHOLDER, stripped_name)
        #print(new_letter)

        with open(f"Output/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
