# FuruYoniStatistics
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


## 추후 구현될 기능
- 시즌별 아카이브  
- 대전기록 여신 선택  


## 패치 노트
- 2022.9.26 미오비키 항로 카드 관련 오류 수정
- 2022.10.03 이미지 로딩 속도 개선 [(상세정보)](https://github.com/ClearSky-S/FuruYoniStatistics/pull/1)

## 개발자
- 쾌청 / junhyuckjang3@gmail.com