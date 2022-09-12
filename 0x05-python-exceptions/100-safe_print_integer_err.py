def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as error:
        import sys
        print("Expception: {}".format(error), file=sys.stderr)
        return False
    else:
        return True

