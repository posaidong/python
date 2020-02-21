
import Util.GoogleTranslate

print("Hello")

print("__name__ value: ", __name__)

def my_order_arr(a):
    s = sorted(a, reverse=True)
    if len(s) > 0 :
        return s[0]
    return 0

def my_order(it):
    s = sorted(it[1], reverse=True)
    if len(s) > 0 :
        return s[0]
    return 0

def test():
    d = {'a':[4,6], 'b':[2,10]}
    s = sorted(d.values(), key=my_order_arr, reverse=True)
    print(s)
    # s = sorted(d.items(), key=my_order, reverse=True)
    # print(s)

def main():
    print("python main function")
    test()
    ret = Util.GoogleTranslate.translate('book')
    print(ret)

if __name__ == '__main__':
    main()
