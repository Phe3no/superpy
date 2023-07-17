from classes.buy_order import BuyOrder
from classes.sell_order import SellOrder
from functions.read_write_txt import set_time, get_time
from datetime import datetime, date, timedelta


def process_arguments(args):
    processing = "\n===== Time processing....................."
    if ("adjusted_time" in args and args.adjusted_time != None):
        tdelta = timedelta(days=args.adjusted_time)
        new_date = date.today() + tdelta
        set_time(new_date.strftime("%B %d %Y"))
        if (args.adjusted_time == 0):
            print(processing)
            print("===== ATTENTION program set to real time mode! =====")
        elif (args.adjusted_time < 0):
            print(processing)
            print(
                f"===== ATTENTION program is set {args.adjusted_time * -1} days in the past! =====")
        else:
            print(processing)
            print(
                f"===== ATTENTION program is set {args.adjusted_time} days in the future! =====")

    elif ("now" in args and args.now != None):
        set_time(args.now.strftime("%B %d %Y"))
        print("\n===== Time processing......................... =====")
        print("===== ATTENTION program set to real time mode! =====")

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
        sell_order = SellOrder(id, args.product_id, args.quantity,
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
