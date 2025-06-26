# class Converter:

#     def __init__(self, temp):
#         self.temp = temp

#     def f_to_c(self):
#         return (self.temp - 32) * 5 / 9

#     def c_to_f(self):
#         return (self.temp * 9 / 5) + 32


# class to_celcius(Converter):
#     def f_to_c(self):
#         return (self.temp - 32) * 5 / 9


# class to_fahrenheit(Converter):
#     def c_to_f(self):
#         return (self.temp * 9 / 5) + 32


# c = to_celcius(30)
# print(c.f_to_c())


# f = to_fahrenheit(20)
# print(f.c_to_f())

class Converter:

    def f_to_c(self):
        return (f - 32) * 5 / 9

    def c_to_f(self):
        return (c * 9 / 5) + 32

c = Converter()

c = f_to_c(30)
f = c_to_f(20)