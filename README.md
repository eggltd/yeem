# YEEM
yeem is a password creating tool. 
Instruction Manual 


Open a File
Command: open <filename>
Description: Opens a file in write mode. Subsequent commands will write their output to this file.

  
Close the File
Command: close
Description: Closes the currently opened file. No further output will be written to the file.
  
Write  Text
Command: man <text>
Description: Writes the specified text to the currently opened file.

  
Use Alphabets
Command: usealph
Description: Enables the use of alphabets in the tool.

  
Do Not Use Alphabets
Command: usenotalph Or it could be not usealph
Description: Disables the use of alphabets in the tool.
  
Append All Alphabets
Command: alphall
Description: Appends all alphabets (lowercase and uppercase) to the alphlist variable.

  
Set Alphabets Manually
Command: alphman
Description: Allows you to enter a custom list of alphabets. Enter the list of alphabets when prompted.

Set Alphsym Character
Command: alphsym
Description: Allows you to set a custom alphsym character. Enter the character when prompted.

Word Removing
Command: word -r

Phishing:
Command: phish

scanning:
Command: yeemmap

scanning well known ports:
Command: ymap


Hello World!
Command: HelloWorld

Bind/Reverse shell
Commands: 
rshell-php
rshell-rce
bshell
rshell-oth

Replace Alphabets
Command: alph <message>
Description: Replaces the alphsym character in the message with alphabets from the alphlist variable. Writes the output to the currently opened file.

Based on id
Command: yeem
Description: make a list of password based on id

SQL injection
Command: sql-injection
list of password that can used in sql injection 
  
Clear the Console
Command: clear
Description: Clears the console screen.

  
Generate Number Combinations
Command: number <message> <digits>
Description: Generates number combinations by appending digits to the message. Writes the output to the currently opened file.

  

Word Operations
Command: word -r

Description: Clears the word list.

Command: word-a <Word>

Description: Appends a word to the word list.

Command: word-s <Symbol>

Description: Sets the word symbol to the specified symbol.

Command: word-f <stuff>

Description: Replaces the word symbol in the stuff with words from the word list. Writes the output to the currently opened file.


Invalid Command
Description: If an invalid command is entered, an error message will be displayed.
Please note that this instruction manual is specific to the code you provided and assumes familiarity with using the command line or tool interface. Users should refer to this manual to understand how to use the different commands and their corresponding effects.

The tool is open sourced so feel free to remix! 
