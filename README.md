# 🎬 영화 리뷰 커뮤니티 사이트

> 페어 프로젝트
>
> 2인 1조: 권세빈, 김교민

## 📅 프로젝트 기간

- 2022-10-14

## 🧰 사용 기술

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br>

## 👩🏻‍💻 역할 및 맡은 기능

> HTML, CSS, Bootstrap으로 프론트엔드 구현, Django MTV 패턴으로 백엔드 구현

- #### 권세빈

  1. **회원가입**

     - Django `AbstractUser` 모델 상속

     - Django 내장 회원가입 폼 `UserCreationForm`을 상속 받아서 CustomUserCreationForm 작성

     - `CustomUserCreationForm`을 활용해서 회원가입 구현

     - 회원가입 후 곧바로 로그인 되도록 기능 추가

  2. **회원 목록 조회**

  3. **회원 정보 수정**
     - Django 내장 회원 수정 폼 `UserChangeForm`을 상속 받아서 `CustomUserChangeForm` 작성

  4. **리뷰 작성**
     - 모델 Review 작성

  5. **리뷰 정보 조회**
     - 해당 리뷰 정보 출력, 로그인한 유저만 수정 및 삭제 가능

  6. **리뷰 삭제**

  7. **회원탈퇴**

  8. **웹디자인**
     - HTML, CSS, Bootstrap 활용

- #### 김교민

  1. **로그인**
     - Django 내장 로그인 폼 `AuthenticationForm` 활용

  2. **회원 정보 조회**
     - 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동

  3. **로그아웃**

  4. **네비게이션 바**
     - 템플릿 분기로 비 로그인 유저는 작성 버튼 출력하지 않음

  5. **리뷰 목록 조회**

  6. **리뷰 정보 수정**

<br>

## 🚨 에러 발생

- `@login_required`를 이용하여 비 로그인 유저를 막고 로그인 창으로 이동하게 하려고 했는데 이동하지 않고 page not found 에러가 발생했다.

## 🌈 문제 해결

- urls.py에서 login의 path는 `'accounts/login'` 이렇게 작성했었다.
- 비 로그인 유저가 접근했을 때 url에서 `next`라는 추가 변수를 받게 되는데, 기존 url은 맨 뒤에  `/` 가 없기 때문에 받을 수 없었다.
- `/` 를 추가하여 `'accounts/login/'` 이렇게 변경했더니 해결되었다.

<br>

## ✏️ 느낀점

정말 자잘한 오타 조심하고 또 조심하자고 다짐했습니다. 사소하더라도 꼼꼼히 잘 확인하는 습관이 중요하다고 생각했습니다. 

다음에는 검색 기능이나 페이지네이션, 별점 기능 등을 추가하고 싶고 프론트도 반응형 및 애니메이션으로 구현하고 싶습니다.
