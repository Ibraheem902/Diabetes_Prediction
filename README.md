# Diabetes Prediction 🩺

مشروع للتنبؤ باحتمالية الإصابة بمرض السكري باستخدام تقنيات **تعلم الآلة**. يعتمد المشروع على بيانات مرضى السكري، ويستخدم نموذج **Support Vector Machine (SVM)** بعد توحيد البيانات باستخدام `StandardScaler`.

يحتوي المشروع أيضًا على واجهة ويب عربية بسيطة وواجهة برمجية مبنية باستخدام **FastAPI** لإرسال بيانات المريض واستقبال نتيجة التنبؤ.

> ⚠️ **تنبيه:** هذا المشروع تعليمي ولا يُعد أداة تشخيص طبية. لا تعتمد على النتيجة بدلًا من استشارة الطبيب أو إجراء الفحوصات الطبية اللازمة.

## المزايا

- تحليل بيانات مرضى السكري باستخدام Python وJupyter Notebook.
- تدريب نموذج تصنيف باستخدام `SVC` بخوارزمية SVM.
- توحيد الخصائص باستخدام `StandardScaler`.
- توفير API للتنبؤ عبر المسار `/api/predict`.
- واجهة ويب باللغة العربية لإدخال بيانات المريض وعرض النتيجة.
- استخدام `joblib` لتحميل النموذج والـ scaler المحفوظين.

## بنية المشروع

```text
Diabetes_Prediction/
├── Diabetes Prediction.ipynb   # تحليل البيانات وتدريب النموذج
├── diabetes.csv                # مجموعة البيانات
├── predictor.py                # تحميل النموذج وتنفيذ التنبؤ
├── app.py                      # خادم FastAPI وواجهة API
├── index.html                  # واجهة المستخدم العربية
├── .gitignore
└── README.md
```

## مجموعة البيانات

يستخدم المشروع مجموعة بيانات **Pima Indians Diabetes Dataset**، وتحتوي على 768 سجلًا و8 خصائص إدخال بالإضافة إلى العمود الهدف `Outcome`.

### الخصائص المستخدمة

| الخاصية | الوصف |
|---|---|
| `Pregnancies` | عدد مرات الحمل |
| `Glucose` | مستوى الجلوكوز |
| `BloodPressure` | ضغط الدم |
| `SkinThickness` | سمك الجلد |
| `Insulin` | مستوى الإنسولين |
| `BMI` | مؤشر كتلة الجسم |
| `DiabetesPedigreeFunction` | مؤشر التاريخ الوراثي للسكري |
| `Age` | العمر |
| `Outcome` | النتيجة: `0` غير مصاب، `1` مصاب |

## المتطلبات

- Python 3.9 أو أحدث
- pip
- Jupyter Notebook (اختياري لتشغيل التحليل)

## التثبيت

1. استنسخ المستودع:

```bash
git clone https://github.com/Ibraheem902/Diabetes_Prediction.git
cd Diabetes_Prediction
```

2. أنشئ بيئة افتراضية:

```bash
python -m venv venv
```

3. فعّل البيئة الافتراضية:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

4. ثبّت المكتبات المطلوبة:

```bash
pip install fastapi uvicorn pandas numpy scikit-learn joblib jupyter
```

## تشغيل النموذج والتحليل

افتح ملف الـ Notebook:

```bash
jupyter notebook "Diabetes Prediction.ipynb"
```

يستعرض الـ Notebook الخطوات التالية:

1. قراءة ملف `diabetes.csv`.
2. استكشاف البيانات وتحليلها.
3. فصل الخصائص عن النتائج.
4. توحيد البيانات باستخدام `StandardScaler`.
5. تقسيم البيانات إلى تدريب واختبار بنسبة 80/20.
6. تدريب نموذج SVM باستخدام `SVC(kernel='linear')`.
7. تقييم النموذج باستخدام `accuracy_score`.

## تشغيل واجهة API

يحتاج التطبيق إلى وجود الملفين التاليين في المجلد الرئيسي:

```text
diabetes_model.pkl
scaler.pkl
```

يقوم `predictor.py` بتحميل هذين الملفين عند تشغيل التطبيق. بعد تجهيز ملفات النموذج، شغّل الخادم بالأمر التالي:

```bash
uvicorn app:app --reload
```

ستتوفر الواجهة البرمجية على:

```text
http://127.0.0.1:8000
```

كما يمكنك فتح توثيق FastAPI التفاعلي على:

```text
http://127.0.0.1:8000/docs
```

## استخدام API

### Endpoint

```http
POST /api/predict
```

### مثال على الطلب

```json
{
  "Pregnancies": 1,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 79,
  "BMI": 25.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 30
}
```

### مثال على الاستجابة

```json
{
  "status": "success",
  "data": {
    "prediction": 0,
    "result": "Non-Diabetic"
  }
}
```

القيم المحتملة:

- `prediction: 0` — Non-Diabetic
- `prediction: 1` — Diabetic

## تشغيل واجهة المستخدم

بعد تشغيل FastAPI، افتح ملف `index.html` في المتصفح. الواجهة ترسل البيانات إلى:

```text
http://127.0.0.1:8000/api/predict
```

إذا ظهرت رسالة تفيد بتعذر الاتصال بالخادم، تأكد من تشغيل أمر `uvicorn` أولًا.

## التقنيات المستخدمة

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Joblib
- HTML وJavaScript

## حدود المشروع

- النتائج تقديرية ومبنية على بيانات تدريب محدودة.
- وجود قيم صفرية في بعض الخصائص قد يمثل بيانات مفقودة وليس قيمة فعلية.
- لا ينبغي استخدام النموذج لاتخاذ قرارات طبية.
- يجب توفير ملفات النموذج المحفوظة `diabetes_model.pkl` و`scaler.pkl` قبل تشغيل API.

## المساهمة

المساهمات مرحب بها. يمكنك:

1. عمل Fork للمستودع.
2. إنشاء فرع جديد للتعديلات.
3. إرسال Pull Request مع شرح واضح للتغييرات.

## الترخيص

لم يتم تحديد ترخيص للمشروع حتى الآن.

## رابط المشروع

[Diabetes Prediction على GitHub](https://github.com/Ibraheem902/Diabetes_Prediction)
