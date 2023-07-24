# changes in version 101 (July, 24 2023)

- now the date can be set in the future as well as in the past more then once
- the set date is now shown in the title of every report
- it is now possible to set a date. -->> use main.py --set-date YYYY-MM-DD
- it is no longer possible to sell products of which the expiration date has expired
- it is no longer possible to sell products by id, instead you have to give a product-name

# in response to comments of previously submitted version

The last comment was made on the incorrect functioning of inventory, revenue and profit without arguments.
I did nothing change there, because I am convinced that it worked correctly.

- The inventory report shows stock from the --set-date and before, as long as the products are not expired
- the revenue and profit reports show the revenue or profit on the --set-date

If not, I'd like to hear about it

# my comment

In the version supplied earlier, I assumed that the supermarket itself completes all operations. That's why I found it logical to fill in sales order with ID.
Based on the comments, I understood that the customer fills the sales order. It can be deduced from this that the supermarket has a lot of confidence in its customers, given that they are allowed to set their own price. 😉
