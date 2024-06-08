from fileinput import filename

from src.dto import Operation
from src.utils import get_operations, filter_operation_by_state, sory_operation_by_date


def main(filename='operations.json'):
    operations = get_operations(filename)
    operations = filter_operation_by_state(*operations, state='EXECUTED')
    operations = sory_operation_by_date(*operations)

    for op in operations[:5]:
        print(op.save())
        print()


if __name__ == '__main__':
    main()
