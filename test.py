# 2022/11/23 関数のテスト
def func_args(arg1, arg2, *args):
    print("arg1 = ", arg1)
    print("arg2 = ", arg2)
    print("args = ", args)

    i = 0
    coi = 0
    for i in range(0, len(arg2)):
        print("first--------")
        print(f"iの数: {i}")
        print(f"arg2の数: {arg2[i]}")
        for _i in range(0,len(args[i])):
            print("second--------")
            print(f"{_i}test, {arg2[i]}, args=,{args[i][_i]}")

    # i = 0
    # coi = 0
    # for i, num in enumerate(args):
    #     print(i)


func_args(1, [1,2],[11,111,1111],[22,222,2222])
