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
                        if data[2] == list['name']:
                            list['data'].append(int(data[1]))
                    else:
                        prod.append('null')
                        prod.append(int(data[1]))
                        product['name'] = data[2]
                        product['data'] = prod
                elif 201 <= data[0] <= 210:
                    for list in lists:
                        if data[2] in list:
                            list['data'].append(int(data[1]))
                    else:
                        prod.append('null')
                        prod.append('null')
                        prod.append(int(data[1]))
                        product['name'] = data[2]
                        product['data'] = prod
                elif 301 <= data[0] <= 310:
                    for list in lists:
                        if data[2] in list:
                            list['data'].append(int(data[1]))
                    else:
                        prod.append('null')
                        prod.append('null')
                        prod.append('null')
                        prod.append(int(data[1]))
                        product['name'] = data[2]
                        product['data'] = prod
                elif 401 <= data[0] <= 410:
                    for list in lists:
                        if data[2] in list:
                            list['data'].append(int(data[1]))
                    else:
                        prod.append('null')
                        prod.append('null')
                        prod.append('null')
                        prod.append('null')
                        prod.append(int(data[1]))
                        product['name'] = data[2]
                        product['data'] = prod
                lists.append(product)
        con.close()
        print(lists)
        return lists
    def kakaoo(self):
        kakaoo = [{'name': '널 담은 뚱카롱 [널담카롱] 12구[8+4] 세트, [NEW] 비건 초코파이 예파이 8개입', 'data': [1]}, {'name': '유가네 닭갈비 볶음밥 외 14종 인기상품 골라담기', 'data': [2, 8]}, {'name': '[룩옵틱스] 명품선글라스 최대96%할인! 펜디,질샌더 외 71종 중 택1', 'data': [3]}, {'name': '해남 땅끝햇살 수 10kg (2020년 수확, 등급-상)', 'data': [4]}, {'name': '안동에서 자란 포슬포슬 수미 햇감자 4.5kg 중', 'data': [5]}, {'name': '위닉스뽀송 16L 제습기(DN2H160-IWK)', 'data': [6]}, {'name': '앤드류앤코 라방튀르 EDT 향수 95ml', 'data': [7]}, {'name': '[BRAND DAY] 프레시지 (선착순)골든라벨스테이크+머쉬룸크림스프 외 BEST 골라담기', 'data': [8]}, {'name': '여름필수품 모기패치 넉넉한 수량 54매 108매 162매 구성 선택가능', 'data': [9]}, {'name': '[슈네이처] 물빠짐 퀄팅 욕실화1+1 외 3종 /3개이상 구매시 사은품증정', 'data': [10]}, {'name': '충북 초당옥수수 특품 10개(16cm이상) - 2세트 구매시 2개 추가 증정', 'data': ['null', 1]}, {'name': '[셀퓨전씨] 더마 릴리프 & 클리어 썬스크린 (2종 택1)', 'data': ['null', 2]}, {'name': '[코몽트X슬레진저] 추성훈,김동현 시원한 여름 티셔츠/팬츠/바람막이/등산조끼 4,900원~', 'data': ['null', 3]}, {'name': '프링글스&켈로그 미니간식 모음', 'data': ['null', 4]}, {'name': '[블랙야크] 역시즌 여성 B모션네오벤치다운자켓2 (1BYPAW9522)', 'data': ['null', 5]}, {'name': "'월드클래스' 티젠 콤부차 레몬/베리/유자 (30스틱, 60스틱+보틀)", 'data': ['null', 6]}, {'name': '실외기 없는 친환경 이동식 에어컨 (자가설치/ 15평형 / 제습모드)', 'data': ['null', 7]}, {'name': '유가네 닭갈비 볶음밥 외 14종 인기상품 골라담기', 'data': ['null', 8]}, {'name': '부사 빨간 한입사과 가정용 5KG', 'data': ['null', 9]}, {'name': '청도산지직송 당도선별 달달한 백도 복숭아 4kg 18과내~', 'data': ['null', 10]}, {'name': '삼익가구 유로탑 독립스프링 롤팩 매트리스(슈퍼싱글/퀸)', 'data': ['null', 'null', 1]}, {'name': '애슐리 시그니처 부채살 스테이크 x 5pk(시그니처/허브시즈닝)', 'data': ['null', 'null', 2]}, {'name': '[한샘] 마이쿡 쏠로팬  IH 24cm 냄비와 후라이팬이 하나로! (국내생산)', 'data': ['null', 'null', 3]}, {'name': '매직브라이트 여름 덴탈형 KF94 마스크 100매 대형 / 소형', 'data': ['null', 'null', 4]}, {'name': "'월드클래스' 티젠 콤부차 레몬/베리/유자 (30스틱, 60스틱+보틀)", 'data': ['null', 'null', 5]}, {'name': '(총32팩) 원더 더치커피 5종원두 10+10+12팩 외 콜드브루', 'data': ['null', 'null', 6]}, {'name': '이너리즘 에어 1+1 시원하고 편한 쿨모달 브라나시 2장', 'data': ['null', 'null', 7]}, {'name': '충북 초당옥수수 특품 10개(16cm이상) - 2세트 구매시 2개 추가 증정', 'data': ['null', 'null', 8]}, {'name': '한우가 들어간 한돈 떡갈비 총20장 (1.4kg)', 'data': ['null', 'null', 9]}, {'name': '[평창 라마다 호텔] 야외 키즈풀 or 객실 업그레이드 특전, 7만원대 프라이빗 특가!', 'data': ['null', 'null', 10]}, {'name': '린제이 대용량 모델링팩+팩도구세트 쿨티트리/비타민 1kg 외', 'data': ['null', 'null', 'null', 1]}, {'name': '[웅진] 빅토리아 0 kcal 탄산수/탄산음료 500mlx20펫 총 15종 중 선택1종', 'data': ['null', 'null', 'null', 2]}, {'name': '광주 정순부님의 파김치1kg 외 김치모음', 'data': ['null', 'null', 'null', 3]}, {'name': '퀴드노비1979 커트러리 실버_골드_스푼,포크,나이프,젓가락 8종 기획전 1p', 'data': ['null', 'null', 'null', 4]}, {'name': '[LIVE] USA코튼 솔리드 반팔티 (19color)', 'data': ['null', 'null', 'null', 5]}, {'name': '바삭바삭 영양간식 수제 김부각', 'data': ['null', 'null', 'null', 6]}, {'name': '[정품-역시즌] 네파 아르테 누오보 고어텍스 다운패딩(남녀) - 택1', 'data': ['null', 'null', 'null', 7]}, {'name': '[르헤브] 무더위/폭염속 잠이솔솔 시원한 여름 메밀베개/편백베개', 'data': ['null', 'null', 'null', 8]}, {'name': '크리스탈라이트 10개입 3개 골라담기 + 핸트타월 증정', 'data': ['null', 'null', 'null', 9]}, {'name': '스틸가드핏 컬러 패션마스크 국산100% 2D/KF94 새부리형 대형/소형 50매', 'data': ['null', 'null', 'null', 10]}, {'name': '[농사랑]맑은 물 서산에서 자란 믿을 수 있는 우리 쌀 서해안 간척미 10kg', 'data': ['null', 'null', 'null', 'null', 1]}, {'name': '[송주불냉면] 인기 양념 반반세트 10인분', 'data': ['null', 'null', 'null', 'null', 2]}, {'name': '광주 정순부님의 파김치1kg 외 김치모음', 'data': ['null', 'null', 'null', 'null', 3]}, {'name': 'VIPS 오리지널 바비큐 폭립 450g x 3팩', 'data': ['null', 'null', 'null', 'null', 4]}, {'name': '[LITTLE TREES] 리틀트리 방향제 종이방향제 3개입 모음전 균일가', 'data': ['null', 'null', 'null', 'null', 5]}, {'name': '구이요 소곱창, 한우소곱창, 순살족발, 돼지양념구이 + 증정품', 'data': ['null', 'null', 'null', 'null', 6]}, {'name': '바자르 시원한 여름소재 침구세트 모음전 11종 택 1', 'data': ['null', 'null', 'null', 'null', 7]}, {'name': '마모트 남/녀 상하의 세트 균일가 최대80% SALE', 'data': ['null', 'null', 'null', 'null', 8]}, {'name': '[정품-역시즌] 네파 아르테 누오보 고어텍스 다운패딩(남녀) - 택1', 'data': ['null', 'null', 'null', 'null', 9]}, {'name': 'Apple 애플 펜슬 2세대', 'data': ['null', 'null', 'null', 'null', 10]}]
        print(kakaoo)
        return kakaoo

if __name__ == '__main__':
    result = MyAnalysis().kakao();