def divide(a, b):
    # نتأكد إنو ما في قسمة على صفر
    if b == 0:
        return "خطأ: لا يمكن القسمة على صفر"
    return a / b


# تشغيل مباشر
print(divide(10, 2))