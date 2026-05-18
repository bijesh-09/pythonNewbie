import import_module_eg as mod

print(mod.pi)

print(mod.square(4))

print(mod.cube(3))

def fn1():
    a = 10
    def fn2():
        a = 20
        print("Inside fn2:", a)
    fn2()

fn1()