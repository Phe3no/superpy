# Classes

## Order, BuyOrde, SellOrder

For this assignment I developed the classes BuyOrder and SellOrder which inherit from Order.
Both classes have:

- a constructor,
- an override for the **str** method, which is never used because of the Report class which I came up with later,
- a method that calls a function that handles writing to a csv file,
- and a function that creates an object of the Report class based on the values ​​of the Order object. The Report object then calls a method of class Report where the necessary 'spacing', per value, is passed as its parameters

## Report

For this assignment I developed a class Report that can be used for all reports:

- buy-order report,
- sell-orderreport,
- inventory report,
- revenue report,
- profit report

The Report class has:

- a constructor,
- a method to_dict, which creates a dictionary of all the values of a Report Object,
- a method create_header, which creates a frame row based up on a the given spaces and a character,
- a method create_title_bar, which creates a row for the title of a report, based upon the given spaces,
- a method create_value_bar, which creates a row with the values of a row, based upon the given spaces,
- a method create_report, which creates a complete single value row report (used for buy-orders and sell-orders),
- a method create_report_full_header, which is re-usable code for the generation of an inventory, revenue and profit report

# Functions

I have divided the functions that I developed for this assignment into several files whereby I have tried to separate functionality:

- calc_reports

  here the calculations for the different reports are done. Although I used the date object, strftime and strptime functions and datetime timedelta, part of the calculations are done based on string comparisons. This is because a large part of the calculations were already done before I started using the date object.

- color_theme

  here simple lists can be made with different color schemes where only the number of the scheme needs to be passed when calling the get_theme function. The name of the required variable is constructed from the combination of a string and the passed parameter, after which 'eval' ensures that this string is converted

- init_parser

  here the argparser() is built where I used several subparsers

- parse_args

  here all arguments are parsed so that what the user has requested can be called

- read_write_csv

  most of these features are self-explanatory. For the function get_last_order_id I wrote the necessary inline comments

- read_write_txt

  A getter and setter for requesting the modified time.
  A try except block ensures that if no advanced_time.txt file exists, the set_time function is called.
  A show_time functions which doesn't do any reading or writing, but i thought it would fit best in this file.

# Main

I like to have main as clean as possible, therefor it calls show_time(), so the users gets a message whenever saved time is different from the real time. Then initialize_parser() is called after which the user can go ahead.
