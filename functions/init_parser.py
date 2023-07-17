from argparse import ArgumentParser
from functions.parse_args import process_arguments
from datetime import date
from functions.read_write_txt import get_time

REPORTS = {
    "inventory": "Inventory",
    "revenue": "Revenue",
    "profit": "Profit",
}


def initialize_parser():
    # create the main parser
    parser = ArgumentParser(
        description="\n==== Welcom to Superpy, let's keep track of the inventory!! ===="
    )
    subparsers = parser.add_subparsers(
        dest="command")

    parser.add_argument("-a", "--adjusted-time",
                        type=int,
                        help="manipulate the time, enter the number of days you want to travel in the future (pos int) or the past (neg int)",
                        metavar=""
                        )

    parser.add_argument("-n", "--now",
                        action="store_const",
                        const=date.today(),
                        help="stop manipulating time, turn time back to today",
                        metavar=""
                        )

    # create the subparser for the buy command
    buy_order = subparsers.add_parser(
        "buy", help="create a buy order.... use 'buy -h' for help with a buy order")

    buy_order.add_argument(
        '-n', '--product-name',
        type=str,
        required=True,
        help="required... specifie a product name.",
        metavar=""
    )

    buy_order.add_argument(
        "-q", "--quantity",
        type=int,
        required=True,
        help="required... specifie the quantity of the product in numbers",
        metavar=""
    )

    buy_order.add_argument(
        "-p", "--price",
        type=str,
        required=True,
        help="required... specifie the price for the product in this format 00.00",
        metavar=""
    )

    buy_order.add_argument(
        "-x", "--expire",
        type=str,
        required=True,
        help="required... specifie the expiration date for the product in this format: YYYY-MM-DD",
        metavar=""
    )

    # create the parser for the sell command
    sell_order = subparsers.add_parser(
        "sell", help="create a sell order... use 'sell -h' for help with a sell order")

    sell_order.add_argument(
        "-i", "--product-id",
        type=str,
        required=True,
        help="required... specifie a product id... use 'report inventory' to find a product id",
        metavar=""
    )

    sell_order.add_argument(
        "-q", "--quantity",
        type=int,
        required=True,
        help="reguired... specifie the quantity of the product in numbers",
        metavar=""
    )

    sell_order.add_argument(
        "-p", "--price",
        type=str,
        required=True,
        help="required... specifie the price for the product in this format 00.00",
        metavar=""
    )

    # create the parser for the report command
    create_report = subparsers.add_parser(
        "report", help="create a report....... use 'report -h' for help with a report")

    create_report.add_argument(
        "actions", type=str,
        default="inventory",
        nargs="*",
        action="store",
        choices=REPORTS.keys(),
        help="use report with inventory, revenue or profit for the desired report, inventory is default"
    )

    create_report.add_argument(
        "-y", "--yesterday",
        action="store_const",
        const=get_time(),
        help="use this to create a report for yesterday",
        metavar=""
    )

    create_report.add_argument(
        "-d", "--date",
        type=str,
        help="use this to create a report for a given date, specifie in this formats: YYYY, YYYY-MM or YYYY-MM-DD",
        metavar=""
    )

    parsed_args = parser.parse_args()
    process_arguments(parsed_args)
