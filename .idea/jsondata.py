# import the json and urlib

import urllib.request
import json


def printResults(data):
    # use the json module to load the data into a dictionary
    jsondata = json.loads(data)

    if "title" in jsondata["metadata"]:
        print(jsondata["metadata"]["title"])

    # output the number of events and the magnitude of each event
    count = jsondata["metadata"]["count"]
    print(str(count) + " events recorded")

    # for each event print the place where it occured
    for i in jsondata["features"]:
        print(i["properties"]["place"])

    # print only the events that have a magnitude >=4
    for i in jsondata["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("2.1f" %i["properties"]["mag"], i["properties"]["place"])

    # print only the events where atleast 1 person felt something
    print("Events felt:")
    for i in jsondata["features"]:
        feltReports = i["features"]["felt"]
        if (feltReports != None) & (feltReports > 0):
            print("2.1f" %i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times" )




def main():
    # data feed from the USGS
    # feed lists all earthquakes from the last day larger than mag 2.5
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # open the url and read the data
    webUrl = urllib.request.urlopen(url)
    code = webUrl.getcode()

    if code == 200:
        data = webUrl.read()
        printResults(data)
    else:
        print("Recieved an error from server, cannot retrieve results "
              + str(webUrl.getcode()))


if __name__ == "__main__":
    main()