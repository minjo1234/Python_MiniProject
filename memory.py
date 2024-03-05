import random
import time

def memoryGame():
    level = [6, 8, 10]

    print("\n************* 기억력 테스트 게임 *******************")
    time.sleep(1.5)
    print('숫자가 나온 순서대로 입력해주세요.')
    time.sleep(1.5)
    print('숫자 사이에 스페이스바 , 완료 후 엔터')
    time.sleep(1.5)

    for lv in level:
        printRandomNum(lv)

        user_input = input('정답 >>> ')

        answerCheck(user_input , answer)

        if success == False:
            break
        if lv != level[-1]:
            print('다음 단계로 !')
            time.sleep(1)


def printRandomNum(lv):
    global answer 
    answer = []

    for i in range(lv):
        n = random.randint(0, 9)
        answer.append(n)
        print(' '*i, n, end='\r')
        time.sleep(0.5)

def answerCheck(user_input , answer):
    global success
    try:
        user_input = list(map(int , user_input.strip().split(' ')))
        if user_input == answer:
            print('정답입니다!')
            time.sleep(1)
            success = True
        else:
            print('틀렸습니다.')
            time.sleep(1)
            print('정답은' , answer , '입니다.')
            time.sleep(1)
            success = False
    except:
        print('숫자와 스페이스바만 신경써 주세요 !')
        user_input = input('정답 >>> ')
        answerCheck(user_input , answer)


memoryGame()