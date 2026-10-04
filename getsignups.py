import databaseconnection as Data
import sys

class main:
    def __init__(self,tripid):
        tripid = tripid
        out = self.getSignups(tripid)
        if out == False:
            print("There was an error")
        else:
            for counter in out:
                print(counter)
    
    
    def getSignups(self,tripid):
        query = ("SELECT Users.Forename, Users.Surname, TripSignups.Pronouns, TripSignups.Phonenum, TripSignups.Harness, TripSignups.Helmet, TripSignups.bmcmember, TripSignups.emgname, TripSignups.emgrelation, TripSignups.emgnumber, TripSignups.medconditions From Users "
                 "INNER JOIN TripSignups ON Users.ID = TripSignups.UserID WHERE TripSignups.TripID == " + tripid)
        try:
            data = Data.main()
            data.execute(query)
            out = data.fetchAllRecords()
            data.closeConnection()
            return out
        except:
            data.closeConnection()
            return False
            


if __name__ == "__main__":
    if (len(sys.argv) == 2):
        tripid = sys.argv[1]
        main(tripid)
    else:
        print("There was an error")