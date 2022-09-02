from select import KQ_NOTE_ATTRIB


input_id = input("아이디를 입력해주세요. \n")
input_pwd = input("비밀번호를 입력해주세요. \n")
print("회원가입이 완료되었습니다.!! \n")
real_id = input("아이디를 입력해주세요. \n")
#real_pwd = input("비밀번호를 입력해주세요. \n")

while True :
    if input_id ==  real_id :
        real_pwd = input("비밀번호를 입력해주세요. \n")
        while True :
            if input_pwd == real_pwd :
                print("로그인이 완료되었습니다.")
                import sys
                sys.exit()
            else : 
                print("비밀번호가 잘못되었습니다. \n")
                real_pwd = input("비밀번호를 입력해주세요. \n")
    else :
        print("아이디가 잘못되었습니다. \n")
        real_id = input("아이디를 입력해주세요. \n")