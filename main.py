from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result
from cloudant.result import Result, ResultByKey


# IBM Cloudant Legacy authentication
client = Cloudant("apikey-v2-19tnsio1aucl2iumux6t1auic0wej0ouorbmcthpy6rc", "9683b33231c604a4552d62ef60d95463",
                  url="https://apikey-v2-19tnsio1aucl2iumux6t1auic0wej0ouorbmcthpy6rc:9683b33231c604a4552d62ef60d95463@2cb2e988-2ce8-4573-b30a-57bb81162555-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()

database_name = "sensordata"

my_database = client.create_database(database_name)

if my_database.exists():
    print(f"'{database_name}' successfully created.")
    json_document = {
                    "_id": "1001",
                    "name":"prathiba"
                    }
    new_document = my_database.create_document(json_document)
    if new_document.exists():
        print("Document '{new_document}' successfully created.")

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['1001']  #search by id, if id=1001   

print("---------------")
print("the data with id =1001 is")
print (result)
print("---------------")
# Iterate over the result collection
for result in result_collection:
    print(result)# it will print all the records

# First retrieve the document
for document in my_database:
    my_document = my_database['1001'] 

# Update the document content
# This can be done as you would any other dictionary
my_document['Id'] = 12345
my_document['Name'] = 'Prathiba'
my_document['Id1'] = 12456
my_document['Name1'] = 'Kalyan'
my_document['Id2'] = 12356
my_document['Name2'] = 'Ram'



# You must save the document in order to update it on the database
my_document.save()

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['1001']     
# Iterate over the result collection
print (result)


