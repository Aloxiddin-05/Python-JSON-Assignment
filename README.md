## 📁 Foydali JSON Uyga Vazifalar

### ✅ 1. **Ma’lumotni JSON faylga yozish**

**Tavsif**: Talabalar ro‘yxati bor (ism, familiya, yosh). Shu ma’lumotlarni `students.json` faylga yozing.

```python
# Ma’lumotlar:
students = [
    {"name": "Ali", "surname": "Valiyev", "age": 20},
    {"name": "Laylo", "surname": "Karimova", "age": 21},
    {"name": "Bekzod", "surname": "Xolmatov", "age": 19}
] 
```

---

### ✅ 2. **JSON faylni o‘qish**

**Tavsif**: Yuqoridagi `students.json` faylini o‘qing va har bir talabaning ismi bilan yoshi ekranga chiqsin:

```
Ali - 20 yosh
Laylo - 21 yosh
Bekzod - 19 yosh
```

---

### ✅ 3. **Yangi element qo‘shish**

**Tavsif**: `students.json` fayliga yangi talaba qo‘shing:

```json
{"name": "Shahzoda", "surname": "Nazarova", "age": 22}
```

---

### ✅ 4. **Foydalanuvchidan ma’lumot olib JSON ga yozish**

**Tavsif**: `input()` yordamida foydalanuvchidan `ism`, `familiya`, `yosh` so‘rang va mavjud `students.json` fayliga qo‘shib yozing.

---

### ✅ 5. **Yosh bo‘yicha filtr qilish**

**Tavsif**: `students.json` faylidan faqat `20 yoshdan katta` bo‘lganlarni ekranga chiqaring.

---

### ✅ 6. **JSONdan boshqa CSV formatga o‘tkazish**

**Tavsif**: `students.json` faylini `students.csv` fayliga aylantiring. Har bir qatorda ism, familiya, yosh bo‘lsin.

---

### ✅ 7. **Statistika chiqarish**

**Tavsif**: `students.json` faylidan o‘rtacha yoshni hisoblang.

---

### ✅ 8. **Top Student (Maksimal yosh)**

**Tavsif**: Eng katta yoshli talabani toping va chiqaring.

---

### ✅ 9. **Studentlar sonini hisoblash**

**Tavsif**: `students.json` faylidagi talabalarning umumiy sonini aniqlang.

---

### ✅ 10. **Tartiblab chiqish**

**Tavsif**: Talabalarni yosh bo‘yicha oshib boruvchi tartibda chiqaring.

---

### 🔥 11. **Fayl mavjud bo‘lmasa yaratish**

**Tavsif**: Dastur ishga tushganida `students.json` fayli mavjud bo‘lmasa, uni avtomatik yaratadigan kod yozing.
