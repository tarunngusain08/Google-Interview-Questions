# Format a list of strings into a table.

# We have a style guide (for example, lines must be at most 80 characters wide). We have a tool that automatically
# formats code to the style guide. One thing it can do is arrange lists of strings into a table. The strings in
# each column are left-aligned to be more easily readable. It leaves no holes in the table except after the last
# string in the last row (i.e. every cell contains a string, except possibly in the last row). Of course, the
# strings remain in the original order.

# Example:

# W = 68 (characters)
# S = [IsAudioBuffer, GetTimestamp, SetTimestamp, GetSampleRate, GetSampleSize, GetNumberOfChannels,
# GetNumberOfSamples, GetDataBuffer, GetChannel]

# We can format this as follows:

# IsAudioBuffer GetTimestamp SetTimestamp GetSampleRate |
# GetSampleSize GetNumberOfChannels GetNumberOfSamples GetDataBuffer |
# GetChannel |

# Given the list of strings, and a maximum number of characters per line, format the table using the maximum
# number of columns without violating the line width constraint.

def formatListOfStringsIntoTable(listOfStrings, maxWidth):
    table = []
    line = ""
    for string in listOfStrings:
        if len(line) + len(string) + 2 > maxWidth:
            table.append(line + "|")
            line = ""
        line += string + " "
    if line != "": table.append(line + "|")
    return table

print(formatListOfStringsIntoTable(["IsAudioBuffer", "GetTimestamp", "SetTimestamp", 
                                    "GetSampleRate", "GetSampleSize", "GetNumberOfChannels", 
                                    "GetNumberOfSamples", "GetDataBuffer", "GetChannel"], 68))

