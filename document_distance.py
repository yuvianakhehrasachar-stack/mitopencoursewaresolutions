# 6.100A Fall 2022
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name:
# Collaborators:

# Purpose: Check for similarity between two texts by comparing different kinds of word statistics.

import string
import math
from collections import Counter

### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def text_to_list(input_text):
    """
    Args:
        input_text: string representation of text from file.
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    final_text=input_text.split()
    return final_text


### Problem 1: Get Frequency ###
def get_frequencies(input_iterable):
    """
    Args:
        input_iterable: a string or a list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in input_iterable and the corresponding int
        is the frequency of the letter or word in input_iterable
    Note: 
        You can assume that the only kinds of white space in the text documents we provide will be new lines or space(s) between words (i.e. there are no tabs)
    """
    frequencies_dic={}
    
    for word in input_iterable:
        if word not in frequencies_dic:
            frequencies_dic[word]=1
        else:
            frequencies_dic[word]+=1
            
    return frequencies_dic


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    
    letter_freq={}
    
    for letter in word:
        if letter not in letter_freq:
            letter_freq[letter]=1
        else:
            letter_freq[letter]+=1
    
    return letter_freq

### Problem 3: Similarity ###
def calculate_similarity_score(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary of letters of word1 or words of text1
        freq_dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    
    all_words= freq_dict1 | freq_dict2
    freq1=sum(freq_dict1.values())
    freq2=sum(freq_dict2.values())
    ALL=freq1+freq2
    DIFF=0
    
    for word in all_words:
         
        if word in freq_dict1 and word in freq_dict2:
            diff1=freq_dict1[word]
            diff2=freq_dict2[word]
            
            DIFF+=abs(diff1-diff2)
            
        elif word in freq_dict1 and word not in freq_dict2:
            DIFF+=freq_dict1[word]
            
        else :
            DIFF+=freq_dict2[word]
            
    
    similarity_score=1-(DIFF/ALL)
    similarity_score_round=round(similarity_score,2)  
    
    return similarity_score_round
            


### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(freq_dict1, freq_dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        freq_dict1: frequency dictionary for one text
        freq_dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    all_words= dict(Counter(freq_dict1) + Counter(freq_dict2))
    frequentest_words=[]
    highest_freq=max(all_words.values())
    
    
    for word, freq in all_words.items():
        if freq==highest_freq:
            frequentest_words.append(word)
        
    return frequentest_words    
        
        

### Problem 5: Finding TF-IDF ###
def get_tf(file_path):
    """
    Args:
        file_path: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    converted_text=text_to_list(load_file(file_path))
    frequencies=get_frequencies(converted_text)
    tf_dic={}
    
    total_words=len(converted_text)
    
    for word,freq in frequencies.items():
        word_freq=frequencies[word]
        tf_score=word_freq/total_words
        tf_dic[word]=tf_score
        
    return tf_dic
        
        
    
    
    

def get_idf(file_paths):
    """
    Args:
        file_paths: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    idf_dic={}
    total_docs=len(file_paths)
    
    
    
    for file in file_paths:
        loaded_file=load_file(file)
        converted_text=text_to_list(loaded_file)
        set_text=set(converted_text)
    
        for word in set_text:
        
            if word not in idf_dic:
                idf_dic[word]=1
            else:
                idf_dic[word]+=1
        
    for word in idf_dic:
        idf_freq=idf_dic[word]
        idf_score=math.log10(total_docs/idf_freq)
        idf_dic[word]=idf_score
            
            
    return idf_dic  
    
   
    
   
    # num_of_docs=len(file_paths)
    # converted_text=text_to_list(load_file(file_paths))
    # frequencies=get_frequencies(converted_text)
    # set_freq=set(frequencies)
    # idf_dic={}
    
    
    # for word in set_freq.items():
        
    #     if word not in idf_dic:
    #         count=1
    #         idf_score=(num_of_docs/count)
    #         idf_dic[word]=idf_score
    #     else:
    #         count+=1
    #         idf_score=(num_of_docs/count)
    #         idf_dic[word]=idf_score
            
    # return idf_dic     
        
    

def get_tfidf(tf_file_path, idf_file_paths):
    """
        Args:
            tf_file_path: name of file in the form of a string (used to calculate TF)
            idf_file_paths: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    tf_dic=get_tf(tf_file_path)
    idf_dic=get_idf(idf_file_paths)
    
    returnedlist=[]
    
    for word,freq in tf_dic.items():
        if freq!= 0:
            tf_val=tf_dic[word]
            idf_val=idf_dic.get(word,0.0)
            tf_idf=tf_val*idf_val
            returnedlist.append((word,tf_idf))
            
    result=sorted(returnedlist, key=lambda score: score[1])
        
        
        
    
    return result

if __name__ == "__main__":
    pass
    ###############################################################
    ## Uncomment the following lines to test your implementation ##
    ###############################################################

    # Tests Problem 0: Prep Data
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    print(world)      # should print ['hello', 'world', 'hello']
    print(friend)     # should print ['hello', 'friends']

    # Tests Problem 1: Get Frequencies
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    print(world_word_freq)    # should print {'hello': 2, 'world': 1}
    print(friend_word_freq)   # should print {'hello': 1, 'friends': 1}

    # Tests Problem 2: Get Letter Frequencies
    freq1 = get_letter_frequencies('hello')
    freq2 = get_letter_frequencies('that')
    print(freq1)      #  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(freq2)      #  should print {'t': 2, 'h': 1, 'a': 1}

    # Tests Problem 3: Similarity
    test_directory = "tests/student_tests/"
    hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    world, friend = text_to_list(hello_world), text_to_list(hello_friend)
    world_word_freq = get_frequencies(world)
    friend_word_freq = get_frequencies(friend)
    word1_freq = get_letter_frequencies('toes')
    word2_freq = get_letter_frequencies('that')
    word3_freq = get_frequencies('nah')
    word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    print(word_similarity1)       # should print 1.0
    print(word_similarity2)       # should print 0.25
    print(word_similarity3)       # should print 0.0
    print(word_similarity4)       # should print 0.4

    # Tests Problem 4: Most Frequent Word(s)
    freq_dict1, freq_dict2 = {"hello": 5, "world": 1}, {"hello": 1, "world": 5}
    most_frequent = get_most_frequent_words(freq_dict1, freq_dict2)
    print(most_frequent)      # should print ["hello", "world"]

    # ## Tests Problem 5: Find TF-IDF
    tf_text_file = 'tests/student_tests/hello_world.txt'
    idf_text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    tf = get_tf(tf_text_file)
    idf = get_idf(idf_text_files)
    tf_idf = get_tfidf(tf_text_file, idf_text_files)
    print(tf)     # should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    print(idf)    # should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    print(tf_idf) # should print [('hello', 0.0), ('world', 0.10034333188799373)]