############################################
#                                          #
#      Convert List of Tuples to Dict      #
#                                          #
#          Mateo Saettone Ascenzo          #
#               U56111212                  #
#                                          #
############################################

# function to convert list of tuples into a dictionary
def convertToDictionary(dataList):
    # create an empty dictionary to store the result
    resultDict = {}
    
    # loop through each tuple in the list
    for item in dataList:
        key = item[0]       # first element of tuple is the key
        value = item[1]     # second element of tuple is the value
        resultDict[key] = value   # add key-value pair to the dictionary
    
    return resultDict

# main function to run the program
def main():
    # given list of tuples
    dataList = [('apple', 5), ('banana', 2), ('orange', 8), ('grapes', 3), ('pineapple', 1)]
    
    # display the original list of tuples
    print("Original List of Tuples:", dataList)
    
    # convert list of tuples to dictionary
    convertedDict = convertToDictionary(dataList)
    
    # display the converted dictionary
    print("Converted Dictionary:", convertedDict)

# run the main function
main()
