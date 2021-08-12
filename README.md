
# Netflix Data-Pipeline and Rest API
------------------------------------------------------------------------------------------------------------------------------------------------------
**Brief Summary**


- [ ] A Rest API which fetches, uploads and deletes movie details from a Postgresql database
- [ ] The Restful API can be found in the REST_API folder.
- [ ] The Datase folder holds the csv file contian the data used
- [ ] THe Dataflow folder contains the Data pipeline

## **How the API runs**
1.  Download the API files and Install the required libraries using  the requirements.txt file
2.  The API can be run using your local IDE such as pycharm. 
3.  The API contains a run.py file in the api folder which has to be executed to deploy the API on your local server(computer)
4.  After running the run.oy file, create your profile using the /netflix/user/signup URL endpoint
5.  Then login into the API to get an access token that will be used to access the other request methods. Use the /netflix/user/login URL endpoint.
6.  Use the access token to fetch, upload and delete movie detials in the database


## **URL Endpoints**

The API uses the following methods and url endpoints to fetch or delete data

| Method   | URL End Point            | Summary	            						                    |
|----------|--------------------------|-----------------------------------------------------|
|  	POST   | netflix/user/signup      | Register your details to the API                    |
|  	POST   |  netflix/user/login      | Login into the API to receive an access token       |
|  	GET    |  netflix/movie/fetchall  | Fetch all the movies in the database                |
|  	POST   |  netflix/movie/fetch     | Fetch a single movie from the databse using it title|
|  	POST	 |  netflix/movie/add       | Add movie details in the database                   |
|  	DELETE |  netflix/movie/delete    | Delete movie details from API                       |



## **Swagger UI**
- [ ] A Swagger UI was generated which shows how to use the REST API in additionin more detail.
The Swagger UI can be accessed through following the steps as shown on the Swagger website [here](https://swagger.io/docs/swagger-inspector/how-to-use-swagger-inspector/)

## **Docker file**
- [ ] The docker image of the RESTful API can be pulled from this link  [docker image link](docker%20pull%20shafiqkyazze/netflix-api:latest)

## **Note**
- [ ] Access tokens are valid for 30 minutes only
