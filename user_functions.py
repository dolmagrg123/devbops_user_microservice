import boto3
from boto3.dynamodb.conditions import Attr
import bcrypt


class Users:
    def __init__(self):
        self.__Tablename__ = "Users_devbops"
        self.client = boto3.client('dynamodb')
        self.DB = boto3.resource('dynamodb')
        self.Primary_Column_Name = "ID"
        self.Primary_key = 1
        self.columns = ["Username", "current city", "current country", "email", "first name", "last name", "password"]
        self.table = self.DB.Table(self.__Tablename__)



    def put(self, user, currentcity, currentcountry, email, firstname, lastname, password):
        all_items = self.table.scan()
        last_primary_key = len(all_items['Items']) + 1

        response = self.table.put_item(
            Item = {
                self.Primary_Column_Name:last_primary_key,
                self.columns[0]: user,
                self.columns[1] : currentcity,
                self.columns[2] : currentcountry,
                self.columns[3] : email,
                self.columns[4] : firstname,
                self.columns[5] : lastname,
                self.columns[6] : self.hash_pw(password)


            }
        )

        print(response["ResponseMetadata"]["HTTPStatusCode"])
           



    def verifying_email_and_user_are_available(self, user, currentcity, currentcountry, email, firstname, lastname, password):
        if self.check_if_user_exists(user) and self.check_if_user_exists_email(email):
            self.put(user, currentcity, currentcountry, email, firstname, lastname, password)
            return True
        else:
            return False
            


    def check_if_user_exists(self, username):
        response = self.table.scan(
            FilterExpression=Attr("Username").eq(username)
        )
        if response["Items"] == []:
            # print("name is avaiavible")
            return username
    
    def check_if_user_exists_email(self, email):
        response = self.table.scan(
            FilterExpression=Attr("email").eq(email)
        )
        if response["Items"] == []:
            # print("email is avaiavible")
            return email
    
    
    def hash_pw(self, password):
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        """
        above hased is a byte stream; below we decode back into a striing and save pw as string
        """
               
        return hashed.decode("utf-8")


    def de_hash(self, password, hashed):
        if bcrypt.checkpw(password, hashed):
            print("it matches")
            return True
        else:
            print("it didnt match")
            return False

    def authincate_user(self, user, password):
        response = self.table.scan(
            FilterExpression=Attr("Username").eq(user)
        )
        # print(response['Items'][0]["password"])


        """
            bcrpty library uses byte stream for its function;
            below we are coverting the string into byte stream to check if the hashed paasword on the db 
            is equal to the encode version of the password passed from the form 
        """
        hased = response['Items'][0]["password"].encode("utf-8")

        self.de_hash(password.encode("utf-8"), hased)

        return self.de_hash(password.encode("utf-8"), hased)

    

      

 

        
        
 



# t1 = users()
# # t1.put("asas", "test", "asasas", "asasas", "asasasasas", "asasasas", "asasasasas")
# t1.hash_pw("test")


# t1.authincate_user(user="sabina", password="P@ssW0rd123")   
# t1.check_if_user_exists("summi")
          