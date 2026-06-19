def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles to your ice cream...")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge to your ice cream...")
        print(args, kwargs)
        func(*args, **kwargs)
    return wrapper

@add_sprinkles # immediately after the fn defn below ts is interpreted, add_sprinkles decorator is called
#after calling decorator, it happens: get_ice_cream = add_sprinkles(get_ice_cream)
#which means get_ice_cream = wrapper , where wrapper = base fn + decorator extension
@add_fudge #multiple decorators are applied in a bottom-up manner, so add_fudge is applied first, then add_sprinkles
def get_ice_cream(flavor):
    print(f"Here's your {flavor} ice cream!")

print(get_ice_cream) #this is ref to wrapper fn, not the original get_ice_cream fn. <function add_sprinkles.<locals>.wrapper at 0x7f8c8c8c8c8c>
get_ice_cream("vanilla") #calling the wrapper fn

#all those process is equivalent to:
# add_sprinkles(get_ice_cream)() #equivalent to @add_sprinkles above, but more explicit.
# add_sprinkles(get_ice_cream)() is equivalent to new get_ice_cream() which is wrapper() in disguise  