#import os
originalAudio = open(r"wave.txt","r")

audioContent = originalAudio.read().splitlines()
arrayLength = len(audioContent)

print("Enter the range:")
numRange = int(input())
print("Enter expression:")
function = input() # user inputs bytebeat expression

for i in range(arrayLength):
    
    audioContent[i] = float(audioContent[i]) # turn the strings from the texfile into floats
    audioContent[i] = ((audioContent[i]) + 1 )/2 # change the range from (-1,1) to (0,1)
    audioContent[i] = int((audioContent[i]*numRange)) # set the number range
    t = audioContent[i] #make the place in the function "t"
    audioContent[i] = eval(function) # run the expression on the array
    audioContent[i] = audioContent[i] %numRange # wrap it around the range
    audioContent[i] = (((audioContent[i]/numRange) * 2) -1) # convert it back into digital audio range
#    print("Sample " + str(i) + " processed.")
#save the data to a new text file    
with open(r'wave2.txt', 'w') as fp:
    for item in audioContent:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Processing completed') # Print when completed