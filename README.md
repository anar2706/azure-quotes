
# Azure Quotes Assignment

A brief description of what this project does and who it's for:
    This project is using azure functions to create 2 sepearate endpoints

    1. Retrieves random quote from https://api.quotable.io/random and returns it in the response.
    2. Retrieves all quotes where the author contains "les".



## Endpoints

Random - https://quotesassignment.azurewebsites.net/api/quotes/random?code=752lrKau7Z5rqD4uXxNRH7L8xSnkbxD95QEQMjRzY1BOAzFuQjfksuw==

Author - https://quotesassignment.azurewebsites.net/api/quotes/author?code=752lrKau7Z5rqD4uXxNRH7L8xSnkbxD95QEQMjRzY1BOAzFuQjfksuw==

## Environment Variables

To run this project, you will need use following enviroenment Variables

`functions host key` = `752lrKau7Z5rqD4uXxNRH7L8xSnkbxD95QEQMjRzY1BOAzFuQjfksuw==`




## Issues

In given repostitory for getting data from API have some problems:

    1) Beta searches for author and specially quotes does not work as intended. Param fields are not working correctly as written in documentation. i had to look at the source code to see what is happening.
    2) Atlas Search regex was not working as it is written in mongo db documentation I was not able to use .* kind of regexes
    3) Because of these problems I had to write inefficent coding in python fetching all the authors from api filtering it and for these names getting quotes


Please take into consideration when evaluation code base.