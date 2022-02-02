# open the names file
with open("./Input/Names/invited_names.txt", 'r') as names:
    # loop through the names
    for name in names.readlines():
        # inside the loop
        # open the sample letter file
        with open("./Input/Letters/starting_letter.txt", 'r') as sample:
            # create the intended letter file with the same name as the recipient
            with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", "w") as ready_letter:
                # loop through the lines in the sample letter
                for line in sample.readlines():
                    # make the correction
                    ready_letter.write(line.replace("[name]", name.rstrip()))
