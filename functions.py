
# coding: utf-8

# In[23]:

import string
import math

    
def clean_text(dirty_text):
    """
    Cleans the text inputted by the user to remove invalid inputs. Extracts only upper case characters so that the 
    chi_sq function can analyze the text.
    
    Parameters:
    -----------
    dirty_text: string
        The user-inputted string as given by the user  
        
    Returns:
    --------
    clean_text: string
        The uppercase version of the dirty string but with all punctuation removed. To be used in chi-square function.
    """
    clean_text = ''
    dirty_text = dirty_text.upper()
    for character in dirty_text:
        if character in string.ascii_uppercase:
            clean_text += character
            
    return clean_text

def caesar_text(dirty_text):
    """
    Similar to clean_text, but keeps the spaces. Used so that the caesar function produces ciphertext with better 
    readability
    
    Parameters:
    -----------   
    dirty_text: string
        The user-inputted string as given by the user
    
    Returns:
    --------   
    caesar_text: string
        The uppercase version of the dirty string but with all punctuation except for spaces removed. To be used when
        encrypting with caesar shift.
    """
    caesar_text = ''
    dirty_text = dirty_text.upper()
    for character in dirty_text:
        if character in string.ascii_uppercase or character == ' ' or character == '\n':
            caesar_text += character
           
    return caesar_text


def letter_count(text_file):
    """
    Counts the number of uppercase occurrences in the given text. Needs to call clean_text to work properly.
    
    Parameters:
    -----------
    text_file: string
        Any given textfile or string by the user
    
    Returns:
    --------
    letter_dict: dictionary
        A dictionary containing all 26 uppercase letters and the number of occurrences in the text_file
    """
    #creates a dictionary of uppercase letters with values of 0
    letter_dict = dict.fromkeys(string.ascii_uppercase, 0)

    text_file = clean_text(text_file)
    for letter in text_file:
        letter_dict[letter] += 1;
        
    return letter_dict

def chi_sq(text):
    """
    Performs a chi-square analysis for a given string. Compares the expected vs. actual occurrences of each letter 
    in the string. Comparison is based on an English dictionary.    
    
    Parameters:
    -----------
    text: string
        Any given text
    
    Returns:
    --------
    chi_sq: int
        The chi-square value of the string vs. expected number of occurrences in the English language
    """
    text=letter_count(text)
    chi_sq = 0
    len_text = sum(text.values())
    
    #generate a dictionary of expected letter occurrences for a text of size 100
    eng_freq = {'E' : 12.02,
        'T' : 9.10,
        'A' : 8.12,
        'O' : 7.68,
        'I' : 7.31,
        'N' : 6.95,
        'S' : 6.28,
        'R' : 6.02,
        'H' : 5.92,
        'D' : 4.32,
        'L' : 3.98,
        'U' : 2.88,
        'C' : 2.71,
        'M' : 2.61,
        'F' : 2.30,
        'Y' : 2.11,
        'W' : 2.09,
        'G' : 2.03,
        'P' : 1.82,
        'B' : 1.49,
        'V' : 1.11,
        'K' : 0.69,
        'X' : 0.17,
        'Q' : 0.11,
        'J' : 0.10,
        'Z' : 0.07 }
            
        
    for letter in eng_freq:
        #print(letter + ' %+2.2f' % eng_freq[letter])
        #print ('enfr = %+2.2f' % (eng_freq[letter]))
        
        #recalculate the expected frequencies for the given text
        eng_freq[letter] = (eng_freq[letter] * len_text) / 100
        chi_sq += math.pow((text[letter] - eng_freq[letter]),2) / eng_freq[letter]
    
    return chi_sq



def caesar(text, shift):
    """
    Shifts each letter in the string by a given amount.   
    
    Parameters:
    -----------
    text: string
        Any given textfile or string by the user
    
    shift: int
        The degree of shift that the text should be moved
        
    Returns:
    --------
    ctext: string
        The encrypted version of the text, using a simple caesar shift
    """
    #error handling when user input for shift is not an int
    try:
        int(shift)
    except:
        return('Not a number, try again!')  
    
    shift = int(shift)
    text = caesar_text(text)
    
    #Handles the case for negative shift inputs
    while shift < 0:
        shift += 26

    #Handles the case for large shift inputs
    shift %= 26
        
    ctext = ''
    shifted = ''
    
    #iterate through the text and add the given amount to each letter. Doesn't do anything if letter is a space.
    for char in text:
        
        #ASCII 'Z' = 90, 'A' = 65
        if char == ' ':
            ctext += ' '
        else:
            shifted = chr((ord(char) + shift))

            #if shifting causes overflow, then loop back to beginning of alphabet to prevent random ASCII characters
            if ord(shifted) > 90:
                shifted  = chr((ord(shifted) % 91) + 65)

            #add the shifted character into the new string
            ctext += shifted
        
    return ctext
    

def main():   
    """
    Main function where user input is collected. Prompts the user with a menu for various interactions. Handles most
    unexpected inputs.
    
    Parameters:
    -----------
    None
    
    Returns:
    --------
    
    """    
    ans=input('What would you like to do today?\nOptions:\n 1: Encrypt\n 2: Decrypt\n 3: Chi-Square\n 4: Quit\n')
    
    #Interaction for Encryption using Caesar Shift
    if ans == '1':
            
        response=input('1: String\n2: Textfile\n')
    
        #encryption of a string
        if response == '1':
            text=input('Please enter the string:\n')
            shift=input('and degree of shift:\n')
            
            #error handling when user input for shift is not an int
            try:
                int(shift)
            except:
                return('Not a number, try again!')
            
            return(caesar(text,int(shift)))
        
        #encryption of a text_file    
        elif response == '2':
            
            filename=input('Please enter the name of the file\n')
            shift=input('and degree of shift:\n')
            
            try:
                readfile = open("textfiles/" + filename, "r")
            except:
                return('File not found')
            
            text = caesar_text(readfile.read())
            readfile.close()
            
            wfile = open("textfiles/ciphertext.txt","w+")
            wfile.write(caesar(text,shift))
            wfile.close()
            
            return('Result has been printed to ciphertext.txt')
               
        else: 
            print('Invalid option, try again\n')

    #Interaction for Decryption
    elif ans == '2':
        
        response=input('1: String\n2: Textfile\n')
            
        if response == '1':
            text=input('Please enter the string:\n')
            text = caesar_text(text)
            for shift in range (1,27):
                if shift == 1:
                    print('Caesar shift of ' + str(shift) + ' place: ' + caesar(text,shift) + '\n')
                else:
                    print('Caesar shift of ' + str(shift) + ' places: ' + caesar(text,shift) + '\n')
                    
            return('All possible caesar shifts listed.')
                    
        elif response == '2':

            filename=input('Please enter the name of the file\n')
            
            try:
                readfile = open("textfiles/" + filename, "r")
            except:
                return('File not found')
            
            text = caesar_text(readfile.read())
            wfile = open("textfiles/decrypted.txt","w+")
            
            for shift in range (1,27):
                if shift == 1:
                    wfile.write('Caesar shift of ' + str(shift) + ' place: ' + caesar(text,shift) + '\n \n')
                else:
                    wfile.write('Caesar shift of ' + str(shift) + ' places: ' + caesar(text,shift) + '\n \n')
                    
            wfile.close()
            readfile.close()
            return('Result has been printed to decrypted.txt')
        else: 
            print('Invalid option, try again')

            
    #Interaction for Chi-Square test
    elif ans == '3':
        
        filename=input('Please enter the name of the file\n')
            
        try:
            readfile = open("textfiles/" + filename, "r")
        except:
            return('File not found')
        text = clean_text(readfile.read())
        readfile.close()
        
        return chi_sq(text)
    
    elif ans == '4':
        return('Quitting')
    
    #Error handling for invalid input
    else:
        print('Invalid option, try again')
        
    return 1



# additional code for vignere cipher support
#
#def generateKey(text, key):
#
#    if len(key) == len(text):
#        return key
#    
#    vkey = list(key)
#    for char in range (len(text) - len(vkey)):
#        vkey.append(key[char % len(key)])
#    
#    return ''.join(vkey)
#    
#shifts each letter in the string using multiple alphabets
#def vignere(text, key):
#    
#    return 0


# In[27]:


#main()


# In[19]:


#os.getcwd()

