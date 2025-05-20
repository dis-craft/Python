# PROGRAM 5:
# DEVELOP A PROGRAM TO PRINT 10 MOST FREQUENTLY APPEARING WORDS IN A TEXT FILE. 
#[Hint: Use dictionary with distinct words and their frequency of occurrences. Sort the dictionary in the reverse order of frequency and display dictionary slice of first 10 items]

file=open("sample.txt")  # Opens the file named "sample.txt" for reading

text=file.read()         # Reads the entire content of the file into the variable 'text'

print(text)              # Displays the entire text content to the console
                         # This is useful to verify the file was read correctly

words=text.split()       # Splits the text into a list of words using whitespace as the delimiter
                         # Note: This simple split doesn't handle punctuation, so words like "hello." and "hello" will be counted separately

frequency={}             # Creates an empty dictionary to store words and their frequencies
                         # The keys will be the unique words and the values will be their count

for word in words:       # Iterates through each word in the list of words
    if word not in frequency:   # Checks if this is the first occurrence of the word
        frequency[word]=1       # If it's the first occurrence, add the word to the dictionary with a count of 1
    
    else:                      # If the word already exists in the dictionary
        frequency[word]+=1     # Increment its count by 1


most_frequency=dict(sorted(frequency.items(),key=lambda elem:elem[1],reverse=True))
        # This sorts the dictionary by values (frequencies) in descending order
        # - frequency.items() returns key-value pairs
        # - key=lambda elem:elem[1] tells sort to use the second element (value) of each pair for comparison
        # - reverse=True makes it sort in descending order (highest frequency first)
        
output_list=dict(list(most_frequency.items())[0:10])
        # This creates a new dictionary with only the first 10 items from the sorted dictionary
        # - most_frequency.items() gets all key-value pairs
        # - list() converts to a list that can be sliced
        # - [0:10] takes only the first 10 items
        # - dict() converts back to a dictionary

# print("1st 10 most frequent words are"+str(output_list))  # Prints the 10 most frequent words and their counts
# The string formatting could be improved for better readability

print("")
for(key,value) in output_list.items():
    print(f"{key}:{value}")