CHARACTERS = "characters.txt"
QUESTIONS = "question1.txt"

def main():
    characters = []
    

    with open(CHARACTERS) as f:
        header = f.readline().rstrip()
        feature_names = header.split(";")
        for line in f:
            features = line.rstrip().split(";")
            character = features
            characters.append(character)
    


    print("Game characters:")
    for character in characters:
        print(f"{character[0]} - Gender: {character[1]}, Hair color: {character[2]}, Hair length: {character[3]}", end="")
        for i in range(4, 9):
            if character[i] == "YES":
                print(f", {feature_names[i]}", end="")
        print()
    print("\n")
    #---------------------------------------------------------------------    
    

    candidate_characters = [True] * len(characters)  
    
    with open(QUESTIONS) as f:
        for q, line in enumerate(f):
            fields = line.split("=");
            feature_name = fields[0].rstrip()  
            feature_value = fields[1].strip()  
            print(f"Step {q+1} - question: {feature_name} = {feature_value}")
            print("Selected characters:")
            for i, character in enumerate(characters):  
                if candidate_characters[i] == True:  
                    feature_index = name2index[feature_name]  
                    if character[feature_index] != feature_value:  
                        candidate_characters[i] = False  
                    else:
                        print(f"{character[0]} - Gender: {character[1]}, Hair color: {character[2]}, Hair length: {character[3]}", end="")
                        for i in range(4, 9):
                            if character[i] == "YES":
                                print(f", {feature_names[i]}", end="")
                        print()
            print()
    
   
    
    candidate_characters_int = [ int(element) for element in candidate_characters ]
    n_valid_candidates = sum(candidate_characters_int)
    
    if n_valid_candidates != 1:
        print("Too bad, you lose.")
    else:
        print("Congratulations, you win! Character selected:")
        for i, candidate in enumerate(candidate_characters):
            if candidate == True:
                print(f"{character[0]} - Gender: {character[1]}, Hair color: {character[2]}, Hair length: {character[3]}", end="")
                for i in range(4, 9):
                    if character[i] == "YES":
                        print(f", {feature_names[i]}", end="")
                print()


if __name__ == "__main__":
    main()
