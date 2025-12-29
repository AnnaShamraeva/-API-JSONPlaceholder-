

class UrlAndEndpoint:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    # POST Creating a resource
    CREATE_POST =  f"{BASE_URL}/posts"
    
    # PUT Updating a resource
    UPDATING_POST = f"{BASE_URL}/posts/1"
  
    # DELETE Deleting a resource
    DELETE_POST =  f"{BASE_URL}/posts/1"
    DELETE_POST_WHITHOUT_ID = f"{BASE_URL}/posts"
    