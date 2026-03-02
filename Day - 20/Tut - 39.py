while True:
    print("1. Code")
    print("2. DeCode\n")
    inp = input("Enter Your Choice : ")
    
    if inp == "1":
        print("The word you add will be incrypted")
        word_1 = input("\nEnter the word : ")
        print(f"The word you added is {word_1}")
        
        if len(word_1) >= 3:
            store = word_1[1:]
            fl = word_1[0]
            nw_wrd = store + fl
            start = "eyr"
            end = "ahb"
            final_word = start + nw_wrd + end
            print(f"The encrypted code is {final_word}")
        else:
            rev = word_1[::-1]
            print(rev)
            
    elif inp == "2":
        print("Ah!! So you want to decode the word : ")
        word_2 = input("Enter the word you want to decode : ")
        print(f"The word you added is {word_2}")
        
        if len(word_2) <= 3:
            rev_2 = word_2[::-1]
            print(rev_2)
        else:
            store_1 = word_2[3:-3]
            last_ltr = store_1[-1]
            f_word = last_ltr + store_1[:-1]
            print(f"The decoded word is : {f_word}")