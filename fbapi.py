# importing library

import facebook as fb

access_token= '' # paste the access token of the app that we have created

data= graph.put_object("me","feed",message="this is my first automated message")
print(data)

graph.get_object(id='****************', fields='name,id') #id = output of the data

graph.get_connections(id='************', connection_name='posts')

graph.put_photo('spider web.jpg',album_path='************',message='automated post')