# Book Store

# About the project
The aim of this project was to develope a simple Rest API simulating a Book Store using Django Rest Framework 
also using Token JWT for Authentication.

Some of the features added to this project were:
- API Rest With Django Rest Framework
- JWT Authentication
- Refresh Token
- Adding books to the Store
- Consulting Books from the Store
- Deleting Books from the Store
- Updating Books from the Store

# Description
- Once the user is authenticated and logged in he get a list of books, adding books, deleting books and updating books.
- also once authenticated a refresh token feature was added so the refreshe token lasts 24 hours.


# Example
__If the user tries to get to the books without being authenticated the Token JWT won't allow it__

![NotProvided Page](https://github.com/Brunotorres15/DjangoApiRest/blob/main/assets/NotProvided.png)

__Testing the endpoints using Insomnia and providing a real user we could get the access token and the refresher token__

![TokenProvided Page](https://github.com/Brunotorres15/DjangoApiRest/blob/main/assets/TokenProvided.png)

__Once authenticated the user could get the list of books__

![BooksList Page](https://github.com/Brunotorres15/DjangoApiRest/blob/main/assets/BooksList.png)

__Using the refresher token we could get another access token__

![TokenRefresh Page](https://github.com/Brunotorres15/DjangoApiRest/blob/main/assets/TokenRefresh.png)
