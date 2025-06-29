import easyocr
import csv

# function to get all information from images
def extractToList(language, imagePath):
    # language should be an string 
    # path must the an string too, path must be using "/""
    reader = easyocr.Reader([language])
    results = reader.readtext(imagePath)
    final_results = []

    for detection in results:
        final_results.append(detection[1])
    
    #return an list with all the results
    return final_results

# function to print all this informations in a spreadsheet
def data_sps(data, header):
    # create a CSV
    with open("spreadsheet.csv", mode='w',
              newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(header)
        writer.writerow(data)
        
    print("All done!")
    return 0




