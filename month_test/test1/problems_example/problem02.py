import json


def over(scores):
    my_scores=[]
    for i in scores:
        if i >= 60:
            my_scores += [i]
    return len(my_scores)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
