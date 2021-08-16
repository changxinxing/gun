import  mysql.connector
from django.http import HttpResponse

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
print(mydb)

def index(request):
    return HttpResponse("Hello World! MySQL is connected")
