This is a program that will encode or decode the alpha characters within .txt file. 

To use this program, move the .txt file you want to encode/decode into the same directory as caesar.py

Open up a command prompt / terminal / equivalent and navigate the directory containing your file(s) and caesar.py

This program uses commandline arguments to function, I'd recommend first looking at what commands are available.

To do this, enter python caesar.py -h into your terminal - this will display all the commands.

The first command should be one of either -e to encode, -d to decode, or -l to readback the number of characters
within your file.

The second command should be -r "x" where "x" is an integer between 1 and 25 of your choice. This is the key to be
used by the program and determines the shift left or right of an alpha character.

The third command should be -i "my_file".txt where "my_file" is the name of the file you wish to encode / decode.

The fourth command should be -o "my_output".txt where "my_output" is the name of the output file that will be 
created.

There are also three optional commands you can use, the first, -s allows you to start from a certain charater in
your text, for example -s "y" where "y" is 1000 would start the encoding / decoding from the 1000th character in
your text.

The second -n allows you to set the maximum amount of output characters, for example -n "z" where "z" is 1000 will
only only encode 1000 characters of your input text. This can be combined with the -s command.

The final command -p is used when you want the output of the program to print to the screen, this is not
recommended for large text files unless using with the -n command.

An example line in a windows command prompt would be as follows:

python caesar.py –e –r 10 –i “100-0.txt” –o “encoded.txt” –n 1000 –s 5000

Encodes the input file 100-0.txt from the 5000th character with a character rotation of 10 and outputting 
1000 encoded characters to encoded.txt


