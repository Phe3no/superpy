Superpy is a nice featured command line application to keep track of the inventory of a supermarked.
You can create buy and sell orders and it allows you to generate reports on profit, revenue and inventory.
There is even an option to travel through time!



**** How to use:
To find out how to work with superpy it is best to follow the step by step below.
By the time you get to the end you'll be a superpy specialist!
Have fun!

Open a CLI and navigate to the folder where you saved superpy.
CD into the superpy directory and start superpy with the help page:

python main.py -h
python main.py --help


If you want help to create a buy order use:

python main.py buy -h
python main.py buy --help


If you want help to create a sell order use:

python main.py sell -h
python main.py sell --help


If you want help to create a report use:

python main.py report -h
python main.py report --help



*** Let's create a buy order:

use 'buy' for buy order folowed by
-n product_name
-q quantity"
-p price
-x expirationdate in YYYY-MM-DD

XXXXample
python main.py buy -n peach -q 12 -p 0.72 -x 2023-07-22



*** Check the inventory

Know that products that have expired do not appear in the inventory. 
Another module has to be written to get these products out of stock.


XXXXamples
python main.py report
python main.py report inventory



**** Let's create a sell order:

use 'sell' for sell order folowed by
-n product-name      
-q quantity
-p price

XXXXamples
python main.py sell -i hamburger -q 2 -p 0.99
python main.py sell -i orange -q 1 -p 0.98
python main.py sell -i melon -q 1 -p 3.24


*** Let's check the inventory again

XXXXamples
python main.py report
python main.py report inventory                 -->> defaults today's date, all products in stock AT --set-date
python main.py report inventory -y              -->> all products in stock yesterday
python main.py report inventory -d 2023         -->> all products in stock in this year
python main.py report inventory -d 2023-07      -->> all products in stock in this month
python main.py report inventory -d 2023-07-22   -->> all products in stock on this day
 


*** Let's check the revenue

XXXXamples
python main.py report revenue                   -->> defaults --set-date
python main.py report revenue -y                -->> revenue yesterday
python main.py report revenue -d 2023           -->> revenue 2023
python main.py report revenue -d 2023-07        -->> revenue July 2023
python main.py report revenue -d 2023-07-22     -->> revenue July, 22 2023 



*** Let's check the profit

XXXXamples
python main.py report profit                    -->> defaults today's date
python main.py report profit -y                 -->> profit yesterday
python main.py report profit -d 2023            -->> profit 2023
python main.py report profit -d 2023-07         -->> profit July 2023
python main.py report profit -d 2023-07-22      -->> profit July, 22 2023



*** Let's go in adjusted time mode

XXXXamples
python main.py -a 1
python main.py --adjusted-time 3



**** Add a buy and a sell order now and get some reports

XXXXamples
python main.py buy -n butter -q 16 -p 1.88 -x 2023-09-04
python main.py sell -n 11 -q 3 -p 2.45 
python main.py report
python main.py report revenue         -->> defaults today's date  
python main.py report revenue -y
python main.py report profit          -->> defaults today's date
python main.py report profit -y




**** Let's get back to real time mode

XXXXamples
python main.py -n
python main.py --now



**** and check all 3 reports.....

python main.py report
python main.py report revenue        
python main.py report profit  

**** Let's set a date

python main.py -s 2023-07-13
python main.py --set-date 2023-07-13

**** and check all 3 reports.....

python main.py report inventory
python main.py report inventory -y

python main.py report revenue        
python main.py report revenue -y        

python main.py report profit  
python main.py report profit -y



As you can see the butter order is gone. 
We did sell it though. But in was in the future.
So if you'll wait long enough, it will be there.

Know that you are also be able to go back in time.
You know enough about superpy to try this out for yourself.




Thanks for reading!






