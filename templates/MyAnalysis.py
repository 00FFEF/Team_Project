import sqlite3

class MyAnalysis:
    def kakao(self):
        con = sqlite3.connect("../db.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT * FROM dbapp_kakaoshop")
        datas = cur.fetchall()
        lists = []
        for data in datas:
            product = dict()
            prod = []
            if 1 <= int(data[1]) <= 10:
                if data[0] <= 10:
                    prod.append(int(data[1]))
                    product['name'] = data[2]
                    product['data'] = prod
                elif 101 <= data[0] <= 110:
                    for list in lists:
                        prod2 = []
                        if data[2] == list['name']:
                            list['data'].append(int(data[1]))
                            del(product['name'])
                            del(product['data'])
                            break;
                        else:
                            prod2.append('null')
                            prod2.append(int(data[1]))
                            product['name'] = data[2]
                            product['data'] = prod2
                elif 201 <= data[0] <= 210:
                    for list in lists:
                        prod2 = []
                        if data[2] == list['name']:
                            list['data'].append(int(data[1]))
                            del (product['name'])
                            del (product['data'])
                            break;
                        else:
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append(int(data[1]))
                            product['name'] = data[2]
                            product['data'] = prod2
                elif 301 <= data[0] <= 310:
                    for list in lists:
                        prod2 = []
                        if data[2] == list['name']:
                            list['data'].append(int(data[1]))
                            del (product['name'])
                            del (product['data'])
                            break;
                        else:
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append(int(data[1]))
                            product['name'] = data[2]
                            product['data'] = prod2
                elif 401 <= data[0] <= 410:
                    for list in lists:
                        prod2 = []
                        if data[2] == list['name']:
                            list['data'].append(int(data[1]))
                            del (product['name'])
                            del (product['data'])
                            break;
                        else:
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append(int(data[1]))
                            product['name'] = data[2]
                            product['data'] = prod2
                elif 501 <= data[0] <= 510:
                    for list in lists:
                        prod2 = []
                        if data[2] == list['name']:
                            list['data'].append(int(data[1]))
                            del (product['name'])
                            del (product['data'])
                            break;
                        else:
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append(int(data[1]))
                            product['name'] = data[2]
                            product['data'] = prod2
                if len(product.keys()) != 0:
                    lists.append(product)
        con.close()
        print(lists)
        return lists

    def kakaoo(self):
        kakaoo = [{'name': '널 담은 뚱카롱 [널담카롱] 12구[8+4] 세트, [NEW] 비건 초코파이 예파이 8개입', 'data': [1]}, {'name': '유가네 닭갈비 볶음밥 외 14종 인기상품 골라담기', 'data': [2, 8]}, {'name': '[룩옵틱스] 명품선글라스 최대96%할인! 펜디,질샌더 외 71종 중 택1', 'data': [3]}, {'name': '해남 땅끝햇살 수 10kg (2020년 수확, 등급-상)', 'data': [4]}, {'name': '안동에서 자란 포슬포슬 수미 햇감자 4.5kg 중', 'data': [5]}, {'name': '위닉스뽀송 16L 제습기(DN2H160-IWK)', 'data': [6]}, {'name': '앤드류앤코 라방튀르 EDT 향수 95ml', 'data': [7]}, {'name': '[BRAND DAY] 프레시지 (선착순)골든라벨스테이크+머쉬룸크림스프 외 BEST 골라담기', 'data': [8]}, {'name': '여름필수품 모기패치 넉넉한 수량 54매 108매 162매 구성 선택가능', 'data': [9]}, {'name': '[슈네이처] 물빠짐 퀄팅 욕실화1+1 외 3종 /3개이상 구매시 사은품증정', 'data': [10]}, {'name': '충북 초당옥수수 특품 10개(16cm이상) - 2세트 구매시 2개 추가 증정', 'data': ['null', 1, 8]}, {'name': '[셀퓨전씨] 더마 릴리프 & 클리어 썬스크린 (2종 택1)', 'data': ['null', 2]}, {'name': '[코몽트X슬레진저] 추성훈,김동현 시원한 여름 티셔츠/팬츠/바람막이/등산조끼 4,900원~', 'data': ['null', 3]}, {'name': '프링글스&켈로그 미니간식 모음', 'data': ['null', 4]}, {'name': '[블랙야크] 역시즌 여성 B모션네오벤치다운자켓2 (1BYPAW9522)', 'data': ['null', 5]}, {'name': "'월드클래스' 티젠 콤부차 레몬/베리/유자 (30스틱, 60스틱+보틀)", 'data': ['null', 6, 5]}, {'name': '실외기 없는 친환경 이동식 에어컨 (자가설치/ 15평형 / 제습모드)', 'data': ['null', 7]}, {'name': '부사 빨간 한입사과 가정용 5KG', 'data': ['null', 9]}, {'name': '청도산지직송 당도선별 달달한 백도 복숭아 4kg 18과내~', 'data': ['null', 10]}, {'name': '삼익가구 유로탑 독립스프링 롤팩 매트리스(슈퍼싱글/퀸)', 'data': ['null', 'null', 1]}, {'name': '애슐리 시그니처 부채살 스테이크 x 5pk(시그니처/허브시즈닝)', 'data': ['null', 'null', 2]}, {'name': '[한샘] 마이쿡 쏠로팬  IH 24cm 냄비와 후라이팬이 하나로! (국내생산)', 'data': ['null', 'null', 3]}, {'name': '매직브라이트 여름 덴탈형 KF94 마스크 100매 대형 / 소형', 'data': ['null', 'null', 4]}, {'name': '(총32팩) 원더 더치커피 5종원두 10+10+12팩 외 콜드브루', 'data': ['null', 'null', 6]}, {'name': '이너리즘 에어 1+1 시원하고 편한 쿨모달 브라나시 2장', 'data': ['null', 'null', 7]}, {'name': '한우가 들어간 한돈 떡갈비 총20장 (1.4kg)', 'data': ['null', 'null', 9]}, {'name': '[평창 라마다 호텔] 야외 키즈풀 or 객실 업그레이드 특전, 7만원대 프라이빗 특가!', 'data': ['null', 'null', 10]}, {'name': '린제이 대용량 모델링팩+팩도구세트 쿨티트리/비타민 1kg 외', 'data': ['null', 'null', 'null', 1]}, {'name': '[웅진] 빅토리아 0 kcal 탄산수/탄산음료 500mlx20펫 총 15종 중 선택1종', 'data': ['null', 'null', 'null', 2]}, {'name': '광주 정순부님의 파김치1kg 외 김치모음', 'data': ['null', 'null', 'null', 3, 3]}, {'name': '퀴드노비1979 커트러리 실버_골드_스푼,포크,나이프,젓가락 8종 기획전 1p', 'data': ['null', 'null', 'null', 4]}, {'name': '[LIVE] USA코튼 솔리드 반팔티 (19color)', 'data': ['null', 'null', 'null', 5]}, {'name': '바삭바삭 영양간식 수제 김부각', 'data': ['null', 'null', 'null', 6]}, {'name': '[정품-역시즌] 네파 아르테 누오보 고어텍스 다운패딩(남녀) - 택1', 'data': ['null', 'null', 'null', 7, 9]}, {'name': '[르헤브] 무더위/폭염속 잠이솔솔 시원한 여름 메밀베개/편백베개', 'data': ['null', 'null', 'null', 8]}, {'name': '크리스탈라이트 10개입 3개 골라담기 + 핸트타월 증정', 'data': ['null', 'null', 'null', 9]}, {'name': '스틸가드핏 컬러 패션마스크 국산100% 2D/KF94 새부리형 대형/소형 50매', 'data': ['null', 'null', 'null', 10]}, {'name': '[농사랑]맑은 물 서산에서 자란 믿을 수 있는 우리 쌀 서해안 간척미 10kg', 'data': ['null', 'null', 'null', 'null', 1]}, {'name': '[송주불냉면] 인기 양념 반반세트 10인분', 'data': ['null', 'null', 'null', 'null', 2]}, {'name': 'VIPS 오리지널 바비큐 폭립 450g x 3팩', 'data': ['null', 'null', 'null', 'null', 4]}, {'name': '[LITTLE TREES] 리틀트리 방향제 종이방향제 3개입 모음전 균일가', 'data': ['null', 'null', 'null', 'null', 5]}, {'name': '구이요 소곱창, 한우소곱창, 순살족발, 돼지양념구이 + 증정품', 'data': ['null', 'null', 'null', 'null', 6, 3]}, {'name': '바자르 시원한 여름소재 침구세트 모음전 11종 택 1', 'data': ['null', 'null', 'null', 'null', 7]}, {'name': '마모트 남/녀 상하의 세트 균일가 최대80% SALE', 'data': ['null', 'null', 'null', 'null', 8]}, {'name': 'Apple 애플 펜슬 2세대', 'data': ['null', 'null', 'null', 'null', 10]}, {'name': 'MLB 샌들/슬리퍼 18종 모음', 'data': ['null', 'null', 'null', 'null', 'null', 1]}, {'name': '링티 2박스 (20포 / 레몬맛 1박스, 복숭아맛 1박스)', 'data': ['null', 'null', 'null', 'null', 'null', 2]}, {'name': '챔피온 반팔티 GT23H', 'data': ['null', 'null', 'null', 'null', 'null', 4]}, {'name': '[메종르자비] 라이크라 노와이어 브라+팬티 5종 택1  ML05_SELECT0205', 'data': ['null', 'null', 'null', 'null', 'null', 5]}, {'name': '피죤 섬유유연제 3100mlx4개+스프레이200ml증정', 'data': ['null', 'null', 'null', 'null', 'null', 6]}, {'name': '[땅깊은김치] 100%국산재료 인공감미료 없는 건강한 열무김치/배추김치/총각김치', 'data': ['null', 'null', 'null', 'null', 'null', 7]}, {'name': '제주안심밥상 제주돼지 숯불갈비맛 불고기 300g x 6팩 총1.8kg', 'data': ['null', 'null', 'null', 'null', 'null', 8]}, {'name': '[동원][1+1] 펭수참치 135g x 6캔+6캔 더! (총12캔 랜덤증정)', 'data': ['null', 'null', 'null', 'null', 'null', 9]}, {'name': 'Apple애플워치 SE 40mm GPS 알루미늄 케이스 + 스포츠 밴드', 'data': ['null', 'null', 'null', 'null', 'null', 10]}]
        print(kakaoo)
        return kakaoo

    def naver(self):
        con = sqlite3.connect("../db.sqlite3")
        cur = con.cursor()
        cur.execute("SELECT * FROM dbapp_navershop")
        datas = cur.fetchall()
        lists = []
        for data in datas:
            product = dict()
            prod = []
            if 1 <= data[0] <= 10 or 1 <= data[0]%100 <= 10:
                if data[0] <= 10:
                    prod.append(int(data[0]))
                    product['name'] = data[1]
                    product['data'] = prod
                elif 101 <= data[0] <= 110:
                    for list in lists:
                        prod2 = []
                        if data[1] == list['name']:
                            try:
                                list['data'].append(int(data[0])-100)
                                del (product['name'])
                                del (product['data'])
                            except:
                                continue
                            break;
                        else:
                            prod2.append('null')
                            prod2.append(int(data[0])-100)
                            product['name'] = data[1]
                            product['data'] = prod2
                elif 201 <= data[0] <= 210:
                    for list in lists:
                        prod2 = []
                        if data[1] == list['name']:
                            try:
                                list['data'].append(int(data[0])-200)
                                del (product['name'])
                                del (product['data'])
                            except:
                                continue
                            break;
                        else:
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append(int(data[0])-200)
                            product['name'] = data[1]
                            product['data'] = prod2
                elif 301 <= data[0] <= 310:
                    for list in lists:
                        prod2 = []
                        if data[1] == list['name']:
                            try:
                                list['data'].append(int(data[0])-300)
                                del (product['name'])
                                del (product['data'])
                            except:
                                continue
                            break;
                        else:
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append(int(data[0])-300)
                            product['name'] = data[1]
                            product['data'] = prod2
                elif 401 <= data[0] <= 410:
                    for list in lists:
                        prod2 = []
                        if data[1] == list['name']:
                            try:
                                list['data'].append(int(data[0])-400)
                                del (product['name'])
                                del (product['data'])
                            except:
                                continue
                            break;
                        else:
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append(int(data[0])-400)
                            product['name'] = data[1]
                            product['data'] = prod2
                elif 501 <= data[0] <= 510:
                    for list in lists:
                        prod2 = []
                        if data[1] == list['name']:
                            try:
                                list['data'].append(int(data[0])-500)
                                del (product['name'])
                                del (product['data'])
                            except:
                                continue
                            break;
                        else:
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append('null')
                            prod2.append(int(data[0])-500)
                            product['name'] = data[1]
                            product['data'] = prod2
                if len(product.keys()) != 0:
                    lists.append(product)
        con.close()
        print(lists)
        return lists

    def never(self):
        never = [{'name': '맛있는 오뚜기밥 210g', 'data': [1, 1, 1, 1, 1, 1]}, {'name': '후디스 하이뮨 프로틴 밸런스 304g', 'data': [2, 2, 2, 2, 2, 2]}, {'name': '농심 신라면 120g', 'data': [3, 3, 7]}, {'name': '락토핏 생유산균 골드 2g x 50포', 'data': [4, 4, 4, 4, 5, 4]}, {'name': '오늘의바디 에이치프로틴 WPI 초코맛 1000g', 'data': [5, 9, 9, 9]}, {'name': '하루웰빙 락토 리얼 포스트바이오틱스 500m...', 'data': [6, 5, 5, 5, 6, 6]}, {'name': 'CJ제일제당 햇반 210g', 'data': [7, 7, 9, 6, 4, 7]}, {'name': '제주특별자치도개발공사 삼다수 2L', 'data': [8, 6, 3, 3, 3, 3]}, {'name': '지웨이 알티지 오메가3 장용성 EPA DHA 120...', 'data': [9, 8, 6, 8, 8, 5]}, {'name': '골든팜 지웨이 올스타 스팀 닭가슴살 오리지...', 'data': [10, 9, 8, 7, 7]}, {'name': '맛있는 오뚜기밥 210g', 'data': ['null', 1, 1, 1, 1, 1]}, {'name': '종근당건강 프로메가 알티지 오메가3 듀얼 ...', 'data': ['null', 10, 10]}, {'name': '에스큐 SQ 캡슐 프로바이오틱스 생유산균 5...', 'data': ['null', 'null', 'null', 10, 10]}, {'name': '동원 샘물 2L', 'data': ['null', 'null', 'null', 'null', 'null', 8]}, {'name': '제주특별자치도개발공사 삼다수 500ml', 'data': ['null', 'null', 'null', 'null', 'null', 10]}]
        return never

if __name__ == '__main__':
    result = MyAnalysis().naver();