dbfilename = "test3_2.dat"

def readScoreDB():
    try:
        fH = open(dbfilename)
    except FileNotFoundError as e:      # 에러 처리하기 / 파일이 존재하지 않는 경우
        print("New DB: ", dbfilename)   # 새로운 DB의 이름을 입력받는다.
        return []
    else:                               # except 문에 걸리지 않았을 때(예외가 발생하지 않았을 때)
        print("Open DB: ", dbfilename)  # Open DB: test3_2.dat

    scdb = []
    for line in fH:                     # "test3_2.dat" 파일을 한 줄씩 line으로 받는다.
        dat = line.strip()              # 앞 뒤 공백을 제거한다.
        person = dat.split(",")         # ","을 기준으로 나눈 것을 person에 대입한다.
        record = {}
        for attr in person:             # person의 정보들이 attr 이다.
            kv = attr.split(":")        # ":"을 기준으로 나눈다.
            record[kv[0]] = kv[1]       # ":"기준 앞이 key값, 뒤가 value값이다.
        scdb += [record]                # 각 사람들의 record라는 dictionary에 저장된 정보들을 scdb라는 리스트에 추가한다.
    fH.close()                          # 파일을 닫는다.
    return scdb                         # scdb 리스트를 return한다.


# write the data into person db
def writeScoreDB(scdb):                 # 함수의 인수로 scdb 리스트 값을 받는다.
    fH = open(dbfilename, 'w')          # 파일을 쓰기모드로 연다.
    for p in scdb:                      # scdb 리스트 안에 있는 dictionary들을 하나씩 가져온다.
        pinfo = []
        for attr in p:                  # dictionary 안에 있는 key 값들을 하나씩 attr롤 가져온다.
            pinfo += [attr + ":" + p[attr]] # pinfo라는 리스트에 [key값 : value값]을 추가한다.
        line = ','.join(pinfo)          # ','를 구분자로 해서 데이터를 합친다.
        fH.write(line + '\n')           # line을 파일에 쓰고 개행한다.
    fH.close()                          # 파일을 닫는다.


def doScoreDB(scdb):
    while(True):                        # 무한루프
        inputstr = (input("Score DB > ")) # input 값을 받는다.
        if inputstr == "": continue     # 입력값이 공백이면 continue
        parse = inputstr.split(" ")     # parse는 input 값을 " "을 구분으로 나눈 것이다.
        if parse[0] == 'add':           # input 값의 [0]이 'add' 일 때
            record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]} # [1]은 Name, [2]는 Age, [3]은 Score로 저장된다.
            scdb += [record]            # scdb 리스트에 record를 추가한다.
        elif parse[0] == 'del':         # [0]이 del 일 때
            for p in scdb:              # scdb 리스트의 요소 하나씩 p로 불러온다.
                if p['Name'] == parse[1]:   # 만약 dictionary의 key 값 Name의 value가 [1]과 같을 때
                    scdb.remove(p)      # 해당 dictionary를 삭제한다.
                    break               # 찾으면 for문 break한다.
        elif parse[0] == 'show':        # [0]이 show일 때
            sortKey ='Name' if len(parse) == 1 else parse[1]    # 입력값의 길이가 1이면 이름으로 정렬하고, 아니면 입력[1]을 기준으로 정렬한다.
            showScoreDB(scdb, sortKey)  # showScoreDB에 scdb 리스트와 정렬할 key값을 인수로 한다.
        elif parse[0] == 'quit':        # [0]이 quit일 때
            break                       # 무한루프를 break한다.
        else:                           # 해당되지 않는 입력값을 받았을 경우
            print("Invalid command: " + parse[0])   # 유효하지 않은 명령문이라는 의미로 Invalid command를 출력하고 입력값을 출력한다.


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()                     # readScoreDB 함수의 return 값인 scdb 리스트를 scoredb에 대입한다.
doScoreDB(scoredb)
writeScoreDB(scoredb)