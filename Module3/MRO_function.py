# # The code here is simple.
# # class F directly inherits from its immediate superclass
# # and the first class that is passed to it.
# # The second line then demonstrates the return from the mro() function.
# class A:
#     def d(self):
#         return "Function inside A"
#
# class B:
#     def d(self):
#         return "Function inside B"
#
#
# class C:
#     def d(self):
#         return "Function inside C"
#
#
# class D(A, B):
#     def d(self):
#         return "Function inside D"
#
#
# class E(B, C):
#     def d(self):
#         return "Function inside E"
#
#
# class F(E,D,C):
#     pass
#
# f = F()
# print(f.d())
# print(F.mro())
#
#
#
# #example
# class A:
#     def b(self):
#         return "Function inside A"
#
# class B:
#     pass
#
# class C:
#     def b(self):
#         return "Function inside C"
#
# class D(B, C, A):
#     pass
#
# class D(C):
#     pass
#
# d = D()
# print(d.b())
#
#
# # example of MRO
#
value = 7
class A:
    value = 5

a = A()
a.value = 3
print(value)