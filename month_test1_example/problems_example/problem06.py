def is_id_valid(user_data):
    if user_data.get('id'):
        if user_data.get('id')[-1] in map(str, range(0,10)):
            return True
        else:
            return False
    else:
        return False


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False