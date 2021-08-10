from run import app
import unittest


"""Creating testing class"""
class ApiTest(unittest.TestCase):

    """Checking if create-user  endpoint works"""
    def test_create(self):
        tester = app.test_client(self)  #Configuring Api application for testing
        response = tester.post("/create") #Obtaining an object from the search person url end point
        statuscode = response.status_code  #Getting the status code of the response object
        self.assertEqual(statuscode, 200)  #Comparing to see if the response return is the success response i.e 200

    """Checking if login endpoint works"""
    def test_login(self):
        tester = app.test_client(self)  #Configuring Api application for testing
        response = tester.post("/login") #Obtaining an object from the search person url end point
        statuscode = response.status_code  #Getting the status code of the response object
        self.assertEqual(statuscode, 200)  #Comparing to see if the response return is the success response i.e 200

    """Checking if get all movies endpoint works"""
    def test_get_all(self):
        tester = app.test_client(self)  #Configuring Api application for testing
        response = tester.get("/allmovies") #Obtaining an object from the search person url end point
        statuscode = response.status_code  #Getting the status code of the response object
        self.assertEqual(statuscode, 200)  #Comparing to see if the response return is the success response i.e 200


    """Checking if get all profiles endpoint works"""
    def test_get(self):
        tester = app.test_client(self)
        response = tester.get("/movie/<title>")
        statuscode=response.status_code
        self.assertEqual(statuscode,200)

    """Checking if delete single profile endpoint works"""
    def test_add_movie(self):
        tester = app.test_client(self)
        response = tester.post("/movie/add") #Deleting profile from database
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    """Checking if content returned by API is in json format"""
    def test_alter_movie(self):
        tester = app.test_client(self)
        response = tester.put("/movie/<title>/alter")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    """Checking if content return by API is in json format"""
    def test_delete_movie(self):
        tester = app.test_client(self)
        response = tester.delete("/movie/<title>/alter")
        statuscode = response.status_code
        self.assertEqual(statuscode,200)


if __name__ == "__main__":   #Running the python file
    unittest.main(verbosity=1)