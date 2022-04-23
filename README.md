## Working with FastAPI & Hypercorn

FastAPI is a super fast Python framework that allows developers to build APIs. To serve the API it uses Uvicorn which is a fast ASGI-server. While working on this repo, I was able to learn about ways to interact with the API using SwaggerUI which is built within the FastAPI framework.

For this project, I simply wanted to see how the hypercorn ASGI-server works instead of the uvicorn. The database of the fruits wasn't created in this project. To use, simply visit the SwaggerUI and execute the API endpoints. Enjoy!



### Installing FastAPI
pip install fastapi

pip install hypercorn



### Using FastAPI
In the terminal type the following: hypercorn main:app --reload
(This allows fast reload of any changes made to the API)

To visit the SwaggerUI be sure to place "/docs" at the end of the localhost URL.
