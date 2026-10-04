import databaseconnection as Data
import sys

class main():
    def __init__(self, tripid, id, pronouns, phonenum, harness, helmet, bmcmember, emgname, relation, emgnumber, medconditions):
        if helmet == "none":
            helmet = 0
        else:
            helmet = 1
        if harness == "none":
            harness = 0
        else:
            harness = 1
        if bmcmember == "yes":
            bmcmember = 1
        else:
            bmcmember = 0
            
        
        result = self.singup(tripid, id, pronouns, phonenum, harness, helmet, bmcmember, emgname, relation, emgnumber, medconditions)
        if result:
            print("Success")
        else:
            print("There was an error")
        
    def singup(self,tripid, id, pronouns, phonenum, harness, helmet, bmcmember, emgname, relation, emgnumber, medconditions):
        query = (f"INSERT INTO TripSignups (TripID, UserID, Pronouns, Phonenum, Harness, Helmet, bmcmember, emgname, emgrelation, emgnumber, medconditions) VALUES "
                 f"({tripid}, {id}, '{pronouns}', '{phonenum}', {harness}, {helmet}, {bmcmember}, '{emgname}', '{relation}', '{emgnumber}', '{medconditions}');")
        
        if self.testaccount(id,tripid):
            try:
                data = Data.main()
                data.update(query)
                data.closeConnection()
                return True
            except:
                data.closeConnection()
                return False
        else:
            return False
        
    def testaccount(self, id, tripid):
        query = "SELECT TripID FROM TripSignups WHERE UserID == " + id + " and TripID == " + tripid + ";"
        try:
            data = Data.main()
            data.execute(query)
            out = data.fetchOneRecord()
            if out == None:
                return True
            else:
                return False
        except:
            return False

if __name__ == "__main__":
    if len(sys.argv) == 12:
        tripid = sys.argv[1]
        id = sys.argv[2]
        pronouns = sys.argv[3]
        phonenum = sys.argv[4]
        harness = sys.argv[5]
        helmet = sys.argv[6]
        bmcmember = sys.argv[7]
        emgname = sys.argv[8]
        relation = sys.argv[9]
        emgnumber = sys.argv[10]
        medconditions = sys.argv[11]
        main(tripid, id, pronouns, phonenum, harness, helmet, bmcmember, emgname, relation, emgnumber, medconditions)
    else:
        print("Error")