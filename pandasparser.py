#importing pandas for convenience
import pandas as pd
def gettoleranceids(data):
    #reading the csv file
    content=pd.read_csv(data)
    #Getting the Latitude diff and converting them to meters
    content["LatitudeDifference"]=content["GPS Latitude"]*111139-content["EXP Latitude"]*111139
    #Getting the Longitude diff and converting them to meters
    content["LongitudeDifference"]=content["GPS Longitude"]*111139-content["EXP Longitude"]*111139
    #extracting meters more than 5000
    result1=content[content["LatitudeDifference"] | content["LongitudeDifference"] > 5000]
    #extracting meters less than -5000
    result2=content[content["LatitudeDifference"] | content["LongitudeDifference"] < -5000]
    # getting only the EID Nos
    result=result1['EID No. ']
    #printing them to CSV
    result.to_csv("result.csv",header="EIDs")