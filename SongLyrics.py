"""
Purpose: Analyze the given song lyrics to find word statistics about it
 Takes a list of strings where each string represents:
 1. Total number of words in the lyrics
 2. Total number of unique words in the lyrics
 3. Five most common words in the lyrics along with their frequency
 4. Longest word in the lyrics

Contract:
 Parameters: A list of strings where each string is a line from a songs lyrics.
 Return: A tuple containing four elements in the following order:
   - Integer representing total number of words in the lyrics
   - Integer representing the total number of unique words in the lyrics
   - A list of tuples containing a word (string) and its frequency (integer) representing 5 most common words
   - A string representing the longest word in the lyrics
"""

# Function to combine the lyrics into a single line making everything lowercase and removes punctuation
def combine_lyrics(lyrics):
    punctuation = '!.?' # Defines the punctuation marks to be removed
    joined_lyrics = ' '.join(lyrics).lower() # Combines the lyrics into a single string and converting them to lowercase
    words = joined_lyrics.split() # Splits the string into individual words
    cleaned_words = [word.strip(punctuation) for word in words] # Removes the punctuation marks defined earlier
    return cleaned_words # Returns the list of processed words

# Function to count the amount of times each word is used
def count_words(words):
    word_count = {} # Initializes an empty dictionary for the word counts

    # Loop to iterate through each word
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1 # Increments the word count for each word used
    return word_count # Returns the complete dictionary with word counts

# Function to convert the word count dictionary into a list of tuples
def word_frequency(word_count):
    # Creates and returns a list of tuples from the word count dictionary
    return [(word, count) for word, count in word_count.items()]

# Function to find the most commonly used words in the lyrics
def most_common_words(word_frequency, top_five=5):

    # First loop to iterate through the word frequency list
    for i in range(len(word_frequency)):

        # Second loop to compare with the rest of the list
        for k in range(i + 1, len(word_frequency)):

            # Checks if the current word count is less than the next word count
            if word_frequency[i][1] < word_frequency[k][1]:
                # If true, it swaps the elements to sort
                word_frequency[i], word_frequency[k] = word_frequency[k], word_frequency[i]

    return word_frequency[:top_five] # Returns the top 5 most commonly used words in the lyrics

# Function to find the longest word count in the word count dictionary
def longest_word(word_count):
    return max(word_count, key=len) # Returns the longest word based on character length

# Main function to analyze the lyrics, calling all the other defined functions
def analyze_lyrics(lyrics):
    words = combine_lyrics(lyrics)  # Combines the lyrics into a single string of words
    word_count = count_words(words)  # Counts how many times each word occurs in the lyrics
    find_word_frequency = word_frequency(word_count)  # Finds the frequency of each word in the lyrics
    find_most_common_words = most_common_words(find_word_frequency)  # Finds the top 5 most commonly used words in the lyrics
    find_longest_word = longest_word(word_count)  # Finds the longest word in the lyrics

    total_words = len(words)  # Calculates the total number of words in the lyrics
    unique_words = len(word_count)  # Calculates the total number of unique words in the lyrics

    # Returns the final analysis with all the data we're looking for
    return total_words, unique_words, find_most_common_words, find_longest_word


# Test case using the Happy Birthday song to ensure the functions are running properly
def test_analyze_lyrics():
    test_lyrics1 = [
        "Happy Birthday to You",
        "Happy Birthday to You",
        "Happy Birthday Dear Kevin",
        "Happy Birthday to You",
        "From good friends and true",
        "From old friends and new",
        "May good luck go with you",
        "And happiness too"
    ]

    result = analyze_lyrics(test_lyrics1)
    assert result[0] == 35
    assert result[1] == 19
    assert result[2] == [('happy', 4), ('birthday', 4), ('you', 4), ('to', 3), ('and', 3)]
    assert result[3] == 'happiness'


# Example song using Livin' On A Prayer by Bon Jovi
livingOnAPrayer = [
        "Once upon a time, not so long ago",

        "Tommy used to work on the docks, union's been on strike",
        "He's down on his luck, it's tough, so tough",
        "Gina works the diner all day, working for her man",
        "She brings home her pay, for love, mmm, for love",

        "She says, \"We've gotta hold on to what we've got",
        "It doesn't make a difference if we make it or not",
        "We've got each other and that's a lot for love",
        "We'll give it a shot\"",

        "Whoa, we're half way there",
        "Whoa oh, livin' on a prayer",
        "Take my hand, we'll make it, I swear",
        "Whoa oh, livin' on a prayer",

        "Tommy's got his six string in hock, now he's holding in",
        "When he used to make it talk so tough, ooh, it's tough",
        "Gina dreams of running away",
        "When she cries in the night, Tommy whispers",
        "\"Baby, it's okay, someday\"",

        "We've gotta hold on to what we've got",
        "It doesn't make a difference if we make it or not",
        "We've got each other and that's a lot for love",
        "We'll give it a shot",

        "Whoa, we're half way there",
        "Whoa oh, livin' on a prayer",
        "Take my hand, we'll make it, I swear",
        "Whoa oh, livin' on a prayer",
        "Livin' on a prayer",

        "Oh, we've gotta hold on, ready or not",
        "You live for the fight when that's all that you've got",

        "Whoa, we're half way there",
        "Whoa oh, livin' on a prayer",
        "Take my hand, we'll make it, I swear",
        "Whoa oh, livin' on a prayer",

        "Whoa, we're half way there",
        "Whoa oh, livin' on a prayer",
        "Take my hand, we'll make it, I swear",
        "Whoa oh, livin' on a prayer",

        "Whoa, we're half way there",
        "Whoa oh, livin' on a prayer",
        "Take my hand, we'll make it, I swear",
        "Whoa oh"
    ]

# Analyzing the lyrics
result = analyze_lyrics(livingOnAPrayer)

# Displaying the results from Livin' on a Prayer
print("Total Word Count:", result[0])
print("Number of Unique Words:", result[1])
print("Most Common Words:", result[2])
print("Longest Word:", result[3])