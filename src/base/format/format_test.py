# coding: UTF-8


def print_tt():
    # %[(name)][flags][width].[precision]typecode

    # normal
    fmt = "%s age is %d, weight is %fkg" % ("jason", 27, 60.5)
    print(fmt)

    # 使用name
    fmt = "%(name)s age is %(age)d, weight is %(weight)fkg, this is %(name)s" % \
            {"name": "jason", "age": 27, "weight": 60.5}
    print(fmt)

    # 使用[flags][width]
    fmt = "%(name)+10s age is %(age)05d, weight is %(weight)fkg, this is %(name)-10s." % \
          {"name": "jason", "age": 27, "weight": 60.5}
    print(fmt)

    # 使用[precision]
    fmt = "%(name)s age is %(age)d, weight is %(weight).1fkg, this is %(name)s." % \
          {"name": "jason", "age": 27, "weight": 60.5}
    print(fmt)


def format_tt():
    fmt = "{} age is {}, weight is {}kg".format("jason", 27, 60.50)
    print(fmt)

    fmt = "{} age is {}, weight is {}kg".format(*["jason", 27, 60.5])
    print(fmt)

    # :s :d :f 指定类型
    fmt = "{:s} age is {:d}, weight is {:f}kg".format("jason", 27, 60.50)
    print(fmt)

    fmt = "{0} age is {1}, weight is {2}kg. this is {0}".format(*["jason", 27, 60.5])
    print(fmt)

    fmt = "{name} age is {age}, weight is {weight}kg. this is {name}".format(
                **{"name": "jason", "age": 27, "weight": 60.5})
    print(fmt)

    fmt = "{name} age is {age}, weight is {weight}kg. this is {name}".format(
                name = "jason", age = 27, weight = 60.5)
    print(fmt)

    fmt = "{0[1]} age is {1[0]}, weight is {2[1]}kg. this is {0[0]}".format(
        ["jason", "hong"], [20, 21], [100.0, 10.0])
    print(fmt)

def run():
    format_tt()


if __name__ == "__main__":
    run()
    

