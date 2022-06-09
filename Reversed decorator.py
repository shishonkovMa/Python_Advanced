import functools


def reversed_dec(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*tuple(reversed(list(args))), **kwargs)
    return inner

# упрощенный вариант декоратора (авторское решение)

# def reversed_dec(func):
#     @functools.wraps(func)
#     def wrapped(*args, **kwargs):
#         return func(*reversed(args), **kwargs)
#
#     return wrapped


# для проверки работы декоратора

# def f_1(*args):
#     lst = list(args)
#     return lst[0] * lst[1]
#
#
# f_2 = reversed_dec(f_1)
#
# res_1 = f_1(1, 3, 4, a=14, b=51)
# res_2 = f_2(4, 3, 1, a=14, b=51)
#
# print(res_1)
# print(res_2)