# ๐ฌ ์ํ ๋ฆฌ๋ทฐ ์ปค๋ฎค๋ํฐ ์ฌ์ดํธ

> ํ์ด ํ๋ก์ ํธ
>
> 2์ธ 1์กฐ: ๊ถ์ธ๋น, ๊น๊ต๋ฏผ

## ๐ ํ๋ก์ ํธ ๊ธฐ๊ฐ

- 2022-10-14

## ๐งฐ ์ฌ์ฉ ๊ธฐ์ 

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br>

## ๐ฉ๐ปโ๐ป ์ญํ  ๋ฐ ๋งก์ ๊ธฐ๋ฅ

> HTML, CSS, Bootstrap์ผ๋ก ํ๋ก ํธ์๋ ๊ตฌํ, Django MTV ํจํด์ผ๋ก ๋ฐฑ์๋ ๊ตฌํ

- #### ๊ถ์ธ๋น

  1. **ํ์๊ฐ์**

     - Django `AbstractUser` ๋ชจ๋ธ ์์

     - Django ๋ด์ฅ ํ์๊ฐ์ ํผ `UserCreationForm`์ ์์ ๋ฐ์์ CustomUserCreationForm ์์ฑ

     - `CustomUserCreationForm`์ ํ์ฉํด์ ํ์๊ฐ์ ๊ตฌํ

     - ํ์๊ฐ์ ํ ๊ณง๋ฐ๋ก ๋ก๊ทธ์ธ ๋๋๋ก ๊ธฐ๋ฅ ์ถ๊ฐ

  2. **ํ์ ๋ชฉ๋ก ์กฐํ**

  3. **ํ์ ์ ๋ณด ์์ **
     - Django ๋ด์ฅ ํ์ ์์  ํผ `UserChangeForm`์ ์์ ๋ฐ์์ `CustomUserChangeForm` ์์ฑ

  4. **๋ฆฌ๋ทฐ ์์ฑ**
     - ๋ชจ๋ธ Review ์์ฑ

  5. **๋ฆฌ๋ทฐ ์ ๋ณด ์กฐํ**
     - ํด๋น ๋ฆฌ๋ทฐ ์ ๋ณด ์ถ๋ ฅ, ๋ก๊ทธ์ธํ ์ ์ ๋ง ์์  ๋ฐ ์ญ์  ๊ฐ๋ฅ

  6. **๋ฆฌ๋ทฐ ์ญ์ **

  7. **ํ์ํํด**

  8. **์น๋์์ธ**
     - HTML, CSS, Bootstrap ํ์ฉ

- #### ๊น๊ต๋ฏผ

  1. **๋ก๊ทธ์ธ**
     - Django ๋ด์ฅ ๋ก๊ทธ์ธ ํผ `AuthenticationForm` ํ์ฉ

  2. **ํ์ ์ ๋ณด ์กฐํ**
     - ํ์ ์์ด๋๋ฅผ ํด๋ฆญํ๋ฉด ํด๋น ํ์ ์กฐํ ํ์ด์ง๋ก ์ด๋

  3. **๋ก๊ทธ์์**

  4. **๋ค๋น๊ฒ์ด์ ๋ฐ**
     - ํํ๋ฆฟ ๋ถ๊ธฐ๋ก ๋น ๋ก๊ทธ์ธ ์ ์ ๋ ์์ฑ ๋ฒํผ ์ถ๋ ฅํ์ง ์์

  5. **๋ฆฌ๋ทฐ ๋ชฉ๋ก ์กฐํ**

  6. **๋ฆฌ๋ทฐ ์ ๋ณด ์์ **

<br>

## ๐จ ์๋ฌ ๋ฐ์

- `@login_required`๋ฅผ ์ด์ฉํ์ฌ ๋น ๋ก๊ทธ์ธ ์ ์ ๋ฅผ ๋ง๊ณ  ๋ก๊ทธ์ธ ์ฐฝ์ผ๋ก ์ด๋ํ๊ฒ ํ๋ ค๊ณ  ํ๋๋ฐ ์ด๋ํ์ง ์๊ณ  page not found ์๋ฌ๊ฐ ๋ฐ์ํ๋ค.

## ๐ ๋ฌธ์  ํด๊ฒฐ

- urls.py์์ login์ path๋ `'accounts/login'` ์ด๋ ๊ฒ ์์ฑํ์๋ค.
- ๋น ๋ก๊ทธ์ธ ์ ์ ๊ฐ ์ ๊ทผํ์ ๋ url์์ `next`๋ผ๋ ์ถ๊ฐ ๋ณ์๋ฅผ ๋ฐ๊ฒ ๋๋๋ฐ, ๊ธฐ์กด url์ ๋งจ ๋ค์  `/` ๊ฐ ์๊ธฐ ๋๋ฌธ์ ๋ฐ์ ์ ์์๋ค.
- `/` ๋ฅผ ์ถ๊ฐํ์ฌ `'accounts/login/'` ์ด๋ ๊ฒ ๋ณ๊ฒฝํ๋๋ ํด๊ฒฐ๋์๋ค.

<br>

## โ๏ธ ๋๋์ 

์ ๋ง ์์ํ ์คํ ์กฐ์ฌํ๊ณ  ๋ ์กฐ์ฌํ์๊ณ  ๋ค์งํ์ต๋๋ค. ์ฌ์ํ๋๋ผ๋ ๊ผผ๊ผผํ ์ ํ์ธํ๋ ์ต๊ด์ด ์ค์ํ๋ค๊ณ  ์๊ฐํ์ต๋๋ค. 

๋ค์์๋ ๊ฒ์ ๊ธฐ๋ฅ์ด๋ ํ์ด์ง๋ค์ด์, ๋ณ์  ๊ธฐ๋ฅ ๋ฑ์ ์ถ๊ฐํ๊ณ  ์ถ๊ณ  ํ๋ก ํธ๋ ๋ฐ์ํ ๋ฐ ์ ๋๋ฉ์ด์์ผ๋ก ๊ตฌํํ๊ณ  ์ถ์ต๋๋ค.
