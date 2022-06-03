This program examines whether 2 words are the same. It also recognizes, if you misspelled it.
The program asks for 2 words:
-the correct  word
-the word to be examined

EXAMPLES:
------------------------------

Two words are the same:
input1:	apple
input2:	apple

output:	This is correct: "apple" :)
-------------------------------------------

One character is wrong:
input1:	apple
input2:	opple

output:	These words are maybe the same: apple
	But you wrote 'o', instead of: 'a'
-------------------------------------------------------------

More character is wrong:
input1:	apple
input2:	opppe

output:	These words are not the same!
-------------------------------------------------------------

Swaped two characters:
input1:	apple
input2: 	aplpe

output:	These words are maybe the same: apple
	But you swaped these characters: p,l
-------------------------------------------------------------

One letters are missing: (more than 50% match)
input1:	apple
input2:	aple

output: 	These words are maybe the same: apple
	But you forgot this character: p
-------------------------------------------------------------

A few letters are missing: (more than 50% match)
input1:	apple
input2:	apl

output: 	These words are maybe the same: apple
	But you forgot these characters: p,e
-------------------------------------------------------------

A few letters are missing: (maximum 50% match)
input1:	guitar
input2:	gut

output: 	These words are not the same!
-------------------------------------------------------------

There is an extra letter:
input1:	apple
input2:	guitar

output: 	These words are maybe the same: guitar
	But you don't need to this character: r
-------------------------------------------------------------

There are extra letters: (more than 50% match)
input1:	apple
input2:	apkplek

output: 	These words are maybe the same: apple
	But you don't need to these characters: k,k
-------------------------------------------------------------

There are extra letters: (maximum 50% match)
input1:	apple
input2:	akpkpklkek

output: 	These words are not the same!
-------------------------------------------------------------

In every other case:
input1:	apple
input2:	guitar

output: 	These words are not the same!
-------------------------------------------------------------
