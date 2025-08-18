# this function will be used as a "dependency"
#a dependency is a Fastapi function that runs before the main endpoint
#this is a security function to validate the user authentication
def get_current_user():
    """
    this is a placeholder for a real authentication check
    in real app, this function would look for a JWT in the request header,validate it and return the users's data.
    if the token is missing,it would raise an error.
    """
    print("Dependency was called.")
    return {"email":"user@example.com","role":"recruiter"}