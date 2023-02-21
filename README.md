# Furu GG
https://furugg.pythonanywhere.com/  

벚꽃 내리는 시대에 결투를(약칭, 후루요니)의 통계 사이트입니다.  
테이블탑 후루요니의 대전 데이터로 통계를 진행합니다.  

## Getting Started
1. install python packages
```sh
$ pip install -r requirements.txt
```
2. remove ".example" from ".env.example", "db.sqlite3.example", "secrets.json.example"


3. runserver
```sh
$ python manage.py runserver
```

## DB Creation
```sh
$ python manage.py migrate

$ python manage.py loaddata api/master_data/god.json

$ python manage.py read_card

$ python manage.py init_partner_data
```

## Update CDN Hash
```sh
$ ./scripts/update-cdn.sh
```

## FAQ
Q. 밴된 여신도 픽률에 반영되나요?  
A. 네, 밴된 여신도 삼습일사 단계에서 선택했기 때문에 픽한 것으로 취급됩니다.  
** 픽률:  (해당 여신이 선택된 횟수) / (모든 게임의 수)

Q. 한 경기에서 양쪽 플레이어가 중복된 여신을 선택했을 경우 해당 여신은 픽률에 한 번만 반영되나요?  
A. 두 번 선택한 것으로 취급됩니다. 이론상 최대 픽률은 200% 입니다.


Q. 밴된 여신도 승률에 반영되나요?  
A. 아니요, 해당 경기에서 사용되지 않았기 때문에 승률에 반영하지 않습니다.  
** 밴률: (해당 여신이 금지된 횟수) / (픽된 횟수 - 금지된 횟수)

## 추후 구현될 기능
- 사용자별 통계


## 패치 노트
- 2022.9.26 미오비키 항로 카드 관련 오류 수정
- 2022.10.03 이미지 로딩 속도 개선 [(상세정보)](https://github.com/ClearSky-S/FuruYoniStatistics/pull/1)
- 2022.12.31 신규 여신 아키나, 시스이 추가 및 통계 초기화, 시즌 7 데이터 아카이브
- 2023.01.12 부적절한 이름 필터링 기능 추가
- 2023.02.01 일부 모바일 기기에서 대전기록의 여신 이미지 위치 오류 수정, 긴 이름에 말줄임표 적용
- 2023.02.20 대전 기록 페이지에 여신 및 사용자 이름을 통한 검색 기능 추가

## 개발자
- 쾌청 / junhyuckjang3@gmail.com
