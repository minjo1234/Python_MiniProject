import time
import random

def memoryGame():

    num_length = [6, 8, 10]

    print('기억력 게임을 시작합니다.')
    time.sleep(1.5)
    print('게임에서는 총 6개 8개 10개의 숫자가 등장합니다.')
    time.sleep(1.5)
    print('숫자사이의 공백을 유지해주세요!')
    time.sleep(1.5)

    for length in num_length:
        answer = []
        input_num = []
        time.sleep(1.5)

        for i in range(length):
            n = random.randint(0, 9)
            answer.append(n)
            print(' '*i, n, end='\r')
            time.sleep(0.5)

        while True:
            try:
                input_num = list(map(int, input('정답 >>> ').strip().split(' ')))   
                if input_num == answer:
                    if length != num_length[-1]:
                        print("정답입니다! 다음 단계로")
                    else:
                        break
                else:   
                    print('틀렸습니다ㅠㅠ')
                    print('정답은' , answer , '입니다.')
                    break
            except Exception as arr:
                print("숫자를 입력해주세요")
                print("정답 >>> ")        



memoryGame()
            
