# Program name: Python File IO Code Challenge

# Programmer name: Vanessa Barajas

# Course: CIT 95

# Date: 9/24/2023

# Define the input and output file paths
input_file_path = "/Users/Vanessa/myGitDir/code-challenge-file-i-o-vbarajas95/arrivingAnimals.txt"
# Use r (raw) before the path string to tell Python to not use the backslash as an escape character
output_file_path = r"/Users/Vanessa/myGitDir/code-challenge-file-i-o-vbarajas95/outputFile.txt"

def get_species(my_str):
    # Split my_str using the character space
    words = my_str.split()
    # TODO: find the data type of words. What can you do with words?
    return words[4]

# Open the input file for reading:
try:
    with open(input_file_path, 'r') as input_file:
        # Read lines from the input file
        lines = input_file.readlines()
        # 'lines' now contains a list of all lines in the input file
        # TODO: Output the type of 'lines'
        # TODO: Fill in the blank: The readlines() method returns a _____ containing all the text lines of input_file.
        # TODO: Output the 2nd and 4th list elements
        #   print("The second list element is: " + _______________ )
        #   print("The fourth list element is: " + _______________ )
        print(f"The second list element is: { lines[1]}")
        print("\n\n")
        print(lines)
        print("\n\n")

        # Open the output file for writing
        with open(output_file_path, "w") as output_file:
            for line in lines:
                # Split each line on the comma
                substrings = line.strip().split(',')

                # TODO: Spend an hour exploring 'substring'
                #   Examine it, ask yourself "what is this" each time you perform a method on it
                #   Spend some time thinking about the many operation you can use on 'substrings' and how this
                #   can help you present your processed data in various ways.
                # TODO: Output the data type of 'substrings'
                # print(f"\n The data type of substrings is ...")

                # TODO: Output "substrings" and think about what you see
                #
                # TODO: Output the first and second elements of substrings
                #
                # TODO: Call get_species and output the species. What will you use for input?

                # hint: print(f"the species is: {....}")
                # TODO: Use a "for each" loop to output the substrings on different lines.
                #
                #
                # TODO: Code up this line to do the same thing. Observe and think about it. This is Python shorthand!
                #   print("\n".join(substrings))
                #
                # TODO: Use "***************" in place of "\n" and examine your output. Read your code from right to
                #   left and think about what is happenening. Communicate with someone on our Discord server and ask
                #   a question about this.
                #
                #
                #
                #
                #
                # Write each substring to the output file separated by newlines
                output_file.write("\n".join(substrings))
                #
                # Add two empty lines between groups of substrings
                output_file.write("\n\n")

    print("\n\nData processed and written to 'outputFile.txt'!")


# TODO: Look at these errors and think how you could modify your input file to cause an error
# TODO: Modify your input file to throw an error!
except FileNotFoundError:
    # This is probably the most common file i/o error.
    print(f"Error: The file '{input_file_path}' was not found.")

except IOError as e:
    # Handle file I/O errors
    if "No space left on device" in str(e):
        # Disk full error
        print("Exception caught! Disk full. Cannot write to the file.")
    elif "Permission denied" in str(e):
        # File locked error
        print("Error: File is locked. Cannot write to the file.")
    else:
        # Other I/O errors (file is corrupted - this happens sometimes on thumb drives )
        print(f"An error occurred: {str(e)}")

except PermissionError:
    # Handle the PermissionError exception here
    print("Error: Permission denied. You don't have the necessary permissions to modify this file.")

except Exception as e:
    # Handle other exceptions you did not imagine.
    print(f"An error occurred: {str(e)}")

finally:
    # Code in this block will execute regardless of whether an exception occurred or not.
    print(f"\n\n End of try/catch block! Good job!")





