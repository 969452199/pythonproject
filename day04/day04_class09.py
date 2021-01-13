def debug(func):
    def wrapper():
        print( "[DEBUG]: enter {}()".format(func.__name__))
        return func()
    return wrapper
@debug
def say_hello():
    print( "hello!")
say_hello()    #[DEBUG]: enter say_hello()
               #hello!



def debug(func):
    def wrapper(something):  # 指定一毛一样的参数
        print( "[DEBUG]: enter {}()".format(func.__name__))
        return func(something)
    return wrapper  # 返回包装过函数
@debug
def say(something):
    print( "hello! {}!".format(something))
say('nice to meet you!')    #[DEBUG]: enter say()
                            #hello! nice to meet you!!


def debug(func):
    def wrapper(*args, **kwargs):  # 指定宇宙无敌参数
        print( "[DEBUG]: enter {}()".format(func.__name__))
        print( 'Prepare and say...')
        return func(*args, **kwargs)
    return wrapper  # 返回
@debug
def say1(something,rt):
    print( "hello! {}!{}!".format(something,rt))
say1('nice to meet you','my name is xiao')      #[DEBUG]: enter say1()
                                                #Prepare and say...
                                                #hello! nice to meet you!my name is xiao!
