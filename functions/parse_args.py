from classes.buy_order import BuyOrder
from classes.sell_order import SellOrder
from functions.read_write_txt import set_time, get_time
from datetime import datetime, date, timedelta
from functions.read_write_txt import show_time


def process_arguments(args):
    processing = "\n===== Time processing....................."
    if ("adjusted_time" in args and args.adjusted_time != None):
        tdelta = timedelta(days=args.adjusted_time)
        # new_date = date.today() + tdelta
        new_date = get_time() + tdelta
        set_time(new_date.strftime("%B %d %Y"))
        if (args.adjusted_time == 0):
            print(processing)
            print(
                f"===== ATTENTION, you did not change time! It is {show_time()}. =====\n")
        elif (args.adjusted_time < 0):
            print(processing)
            print(
                f"===== ATTENTION, you have set the time in the past! It is {show_time()}. =====\n")
        else:
            print(processing)
            print(
                f"===== ATTENTION, you have set the time in the future! It is {show_time()}. =====\n")

    elif ("set_date" in args and args.set_date != None):
        try:
            check_if_date = datetime.strptime(args.set_date, "%Y-%m-%d").date()
            if type(check_if_date) == date:
                print("okay")
                set_time(check_if_date.strftime("%B %d %Y"))
                print(processing)
                print(
                    f"===== ATTENTION, a new date is set! It is {show_time()}. =====\n")

        except ValueError:
            print("----- You did not insert a correct date format, use YYYY_MM_DD! -----")

    elif ("now" in args and args.now != None):
        set_time(args.now.strftime("%B %d %Y"))
        print("\n===== Time processing......................... =====")
        print(
            f"===== ATTENTION, you have set time to current time! It is {show_time()}. =====")

    elif args.command == "buy":
        file = "data/bought.csv"
        from functions.read_write_csv import get_last_order_id
        id = get_last_order_id(file) + 1
        buy_order = BuyOrder(id, args.product_name, args.quantity,
                             args.price, args.expire)

        if (buy_order.append_buy_order()):
            buy_order.report()

        else:
            print("Sorry, problem saving data!")

    elif args.command == "sell":
        file = "data/sold.csv"
        from functions.read_write_csv import get_last_order_id
        id = get_last_order_id(file) + 1
        sell_order = SellOrder(id, args.product_name, args.quantity,
                               args.price)
        if (sell_order.append_sell_order()):
            sell_order.report()

        else:
            print("Sorry, problem saving data!")

    elif args.command == "report":

        def check_time_args(args):
            if args.yesterday:
                tdelta = timedelta(days=1)
                yesterday = args.yesterday - tdelta
                return yesterday.strftime('%Y-%m-%d')
            elif args.date:
                return args.date
            else:
                return get_time().strftime('%Y-%m-%d')

        if "inventory" in args.actions:
            file = "data/inventory.csv"
            from functions.calc_reports import inventory_report
            inventory_report(check_time_args(args))

        if "revenue" in args.actions:
            file = "data/sold.csv"
            from functions.calc_reports import revenue_report
            revenue_report(check_time_args(args))

        if "profit" in args.actions:
            file = "data/sold.csv"
            from functions.calc_reports import profit_report
            profit_report(check_time_args(args))
