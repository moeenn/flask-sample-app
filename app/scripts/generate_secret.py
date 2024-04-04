import os

"""
inside the environment variables, notice the APP_SECRET variable. The value for
this variable is used by flask to sign cookies etc. This script generates 
the value fro app secret and prints it to the stdout.
"""
secret = os.urandom(64).hex()
print(secret)
