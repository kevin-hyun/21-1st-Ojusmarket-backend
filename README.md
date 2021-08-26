# 21-1st-Ojusmarket-backend
![레이어 3](https://user-images.githubusercontent.com/78678551/122677514-92942900-d21d-11eb-8ddb-d94491a41c57.png)

### 🌽 O Jus Maket (오져스 마켓) **Team**

**개발인원 (7명)**

[Frontend](https://github.com/wecode-bootcamp-korea/21-1st-Ojusmarket-frontend) |  김명준, 김민기, 이기완

[Backend](https://github.com/wecode-bootcamp-korea/21-1st-Ojusmarket-backend) | 박준영, 박지우, 장동국, 현상협

> *"소통은 무조건 중요하다! 사랑해요 오저스마켓팀" - ojusmarket -*
> 

**개발기간**

2021.06.07 ~ 2021.06.18

---

### ✔오아시스마켓 클론 프로젝트 선정이유

커머스사이트의 다양한 회원가입, 결제, 배송 서비스들이 실제 구현되어있는것에 도전의식을 느꼈고, 

레시피가 제공 될 뿐만아니라 레시피에 사용된 제품추천 기능 모델링에 호기심을 느끼며 직접 구현 해 보고자 선정하게 되었습니다.

### ✔️오저스마켓 프로젝트 소개

오아시스마켓의 깔끔한 디자인과 서비스를 변형하여 클론한 "오저스마켓" 입니다!

오아시스 마켓이 제공하는 판매상품들로 적용할 수 있는 레시피의 연결성에 주목하였고, 메인페이지에서 “주문도하고 요리도하고” 탭을 추가적으로 구현하여 기존 오아시스마켓과 서비스기획의 중점을 달리하여 클론하였습니다.

결제서비스를 제외한 영상에서 보이는 부분들은 모두 실제 사용할 수 있는 서비스 수준으로 초기세팅부터 백앤드 연결까지 구현하였습니다.

---

### 🏗 Modeling

![maxojus_20210620_13_54](https://user-images.githubusercontent.com/78678551/122676732-3d0a4d00-d21a-11eb-9e14-6e251319ece6.png)

크게 사용자 (users), 재료 (ingredients), 레시피(recipes), 장바구니(carts), 주문하기(orders)를 우선적으로 구성하고, 이에 따른 세부 모델링을 구성하는 순서로 진행 하였습니다.



---

### 🧑‍💻 구현기능

Users | 아이디 중복체크 회원가입 및 로그인, 기본배송정보 저장

Ingredients | 상품정보, main 과 sub 카테고리, 관련 레시피와 연결

Recipes | 관련 재료와 연결, 레시피 카테고리

Carts | 상세페이지를 통한 장바구니 페이지 연결, 재료 삭제, 수량변경 가능

Orders | 유저 정보와 상품 정보 조회, 배송 상태 저장, 결제하기 이동 시 결제된 장바구니 상품 삭제  

---


### 🧑‍💻 담당기능

DB modeling | Aquery 툴로 커머스 사이트에 사용하는 형태로 cart , order, order_status로 관리 

Ingredients | 상품정보, main 과 sub 카테고리, 관련 레시피와 연결 (M:M관계 참조 - Django ORM 활용 )

Recipes |  레시피 카테고리, 관련 재료와 연결 (M:M관계 참조 - Django ORM 활용 )

AWS | S3와 RDS를 통한 배포 (웹서버 구동을 위해 파이썬 gunicorn 사용) 



### 💻 사용 기술

Frontend | HTML5, SASS, REACT, Javascript

Backend |  Python, Django web framework,  Bcrypt, My SQL

Common | Restful API, AWS(EC2,RDS)

### 👍 커뮤니케이션

**저희 오져스마켓 팀은 팀원간의 원활한 커뮤니케이션을위해 다양한 수단을 사용했습니다.**

APP | [Notion](https://www.notion.so/163f5d1be77f4dd7a33ec0377c2f0a6a) , [Trello](https://trello.com/b/S8Bjq4QR/ojusmarket), Google spreadsheet, Slack

Scrum | 스크럼 방식을 사용하여 매일 아침 미팅을 통해 어제 한 일, 오늘 할 일, blocker 세 가지를 공유하며 팀원들과 미팅을 진행하였습니다.

---

## **Reference**

- 이 프로젝트는 [오아시스마켓](https://www.oasis.co.kr/main) 사이트를 참조하여 학습목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
