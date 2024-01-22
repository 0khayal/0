commands = '''
**سورس خيال
الأوامر :

`.م1` » اعدادات السورس

`.م2` » لمعرفة اوامر صيد اليوزرات

`.م3` » لمعرفة اوامر تجميع نقاط بوتات التمويل

`.م4` » لمعرفة اوامر السورس الاضافية**
'''
sec1 = '''
**سورس خيال
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`.فحص` : لاجراء فحص للسورس

`.سورس` : لاجراء فحص للسورس الاضافي

`.اعادة تشغيل` : لاجراء اعادة تشغيل للسورس

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
'''
sec2 = '''
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

✩ `.تثبيت يدوي + القناة + اليوزر` : يقوم بتثبيت اليوزر بقناة معينة

✩ `.صيد + العدد + النوع + يوزر القناة` : يقوم بفحص اليوزرات وتثبيتها على القناة

✩ `.تثبيت تلقائي + العدد + القناة + اليوزر` : يقوم بتثبيت اليوزر بقناة معينة

✩ `.حالة الصيد` : لمعرفة اقدم الصيد

✩ `.حالة التثبيت التلقائي` : لمعرفة تقدم التثبيت التلقائي

✩ `.الانواع` : لمعرفة انواع اليوزرات

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
'''
sec3 = """
سورس خيال
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

`.تجميع المليار` : يقوم بتـجميع نقاطـ بوت تمويل المليار

`.تجميع الجوكر` : يقوم بتجميع نقاط بوت تمويل الجوكر

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
"""
sec4 = """
الاوامر الاضافية | خيال

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

1️⃣ الامـر نشر تلقائي 

الوظيفة : نشر رسالة معينة تلقائيا

طريقة الاستعمال : [.مؤقت + عدد الثواني + عدد التكرار + الكليشة]

مثال | [`.مؤقت 3 5 مرحبأ بك في سورس سايثون` ]

2️⃣ الامر [تكرار] 

الوظيفة : تكرار رسالة معينة بالرد عليها

طريقة الاستعمال : .تكرار + عدد التكرار

3️⃣ الامر اذاعة للخاص

الوظيفة : ارسال رسالة معينة الى جميع المحادثات الخاصة في حسابك

طريقة الاستعمال : .للخاص + الكليشة

مثال | `.للخاص مرحبا بك في سورس سايثون `

4️⃣ الامر اذاعة للمجموعات

الوظيفة : ارسال رسالة معينة الى جميع المجموعات في حسابك

طريقة الاستعمال : .للكروبات + الكليشة

مثال | `.للخاص مرحبا بك في سورس سايثون `

5️⃣️ الامر تسلية 

الوظيفة : التسلية فقط 

محتويات الامر : [`.قمور`][`.حلويات`][`.قلوب`][`.العد التنازلي`][`.قمر`]

6️⃣الامر الالة الحاسبة العلمية 

طريقة الاستعمال [`.احسب + الرقم الاول + العملية الحسابية + الرقم الثاني` ]

يجب مراعات المسافة بين كل كلمة

مثال | `.احسب 7 + 7`
مثال | `.احسب 7 * 7`
مثال | `.احسب 7 - 7`
مثال | `.احسب 7 ÷ 7` 

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
"""
tele_checker = '''
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

✩ `.تثبيت يدوي + القناة + اليوزر` : يقوم بتثبيت اليوزر بقناة معينة

✩ `.صيد + العدد + النوع + يوزر القناة` : يقوم بفحص اليوزرات وتثبيتها على القناة

✩ `.تثبيت تلقائي + العدد + القناة + اليوزر` : يقوم بتثبيت اليوزر بقناة معينة

✩ `.حالة الصيد` : لمعرفة اقدم الصيد

✩ `.حالة التثبيت التلقائي` : لمعرفة تقدم التثبيت التلقائي

✩ `.الانواع` : لمعرفة انواع اليوزرات

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
'''
tele_checker2 = '''
سورس خيال

الانواع :

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍

1-:cd_dc
2-:cd_cd
3-:cd_dd
4-:cd_cc
5-:cc_dc
6-:cc_cd

7-:d_ccc
8-:c_dcc
9-:c_cdc
10-:c_ccd

11-:ccc_d
12-:cdd_d
13-:ccd_c
14-:cdc_c
15-:dcc_c

16-:c_dcd
17-:cdc_d

18-:c_cdd
19-:ccd_d

20-:c_ddc
21-:cdd_c

22-:c_d_d_d
23-:c_d_c_c
24-:c_c_d_c
25-:c_c_c_d

26-:ccdddd
27-:cddccc
28-:ccddcc
29-:cccddc
30-:ccccdd
31-:cccddd

32-:cdcddd
33-:cdcdcc
34-:ccdcdc
35-:cccdcd

36-:cdccdc
37-:cddddc

38-:cddcdd
39-:ccdccd
40-:cdcccd
41-:cdddcd
42-:cdcdcd

43-:cdddcc
44-:ccdddc

45-:cdcddc
46-:cddcdc

47-:cdccdd
48-:cddccd

49-:ccdcdd
50-:ccddcd

51-:cddddddd
52-:cdcccccc
53-:ccdccccc
54-:cccdcccc
55-:ccccdccc
56-:cccccdcc
57-:ccccccdc
58-:cccccccd

`59` -:csdbot

╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
طريقة تفعيل الصيد 

.صيد + عدد المحاولات + رقم نوع الصيد + يوزر القناة الذي أنشأتها
╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍
- مثال╎ `.صيد 1000 1 @o_o_v`
'''
