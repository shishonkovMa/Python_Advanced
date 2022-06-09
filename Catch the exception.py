def exception_logger(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ZeroDivisionError as e:
            print(type(e).__name__)
            pass
        except ArithmeticError as e:
            print(type(e).__name__)
            pass
        except AssertionError as e:
            print(type(e).__name__)
            pass
        else:
            return func(*args, **kwargs)
    return inner
