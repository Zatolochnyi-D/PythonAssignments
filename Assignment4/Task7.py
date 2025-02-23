class B:
    @staticmethod
    def stat_print_dict(object):
        return object.__dict__
    
    def cls_print_dict(self):
        return self.__class__.__dict__

obj = B()
print(obj.stat_print_dict(B))   # Provides the same result, the only difference that stat_print_dict also can be called from B:
print(obj.cls_print_dict())     # B.stat_print_dict()

class C(B):
    e = 'Class C'

obj1 = B()
print(obj1.stat_print_dict(B))  # The same as previous example
print(obj1.cls_print_dict())    # The same as previous example

obj2 = C()
print(obj2.stat_print_dict(C))  # Shows much less attributes, there is "e: Class C" attribute
print(obj2.cls_print_dict())    # Shows much less attributes, there is "e: Class C" attribute