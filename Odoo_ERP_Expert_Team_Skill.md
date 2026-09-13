# Odoo ERP Expert Team Skill

## 1. تعريف الملف
هذا الملف هو مرجع رسمي لبناء فريق تطوير Odoo احترافي قادر على تصميم وتنفيذ وتشغيل حلول ERP للمؤسسات والشركات.
**مصدر إضافي:** Odoo Developer documentation وSystem configuration وSecurity.

---

## 2. الغاية من المهارة

### 2.1 الهدف الرئيسي
تمكين الفريق من بناء حلول Odoo:
- صحيحة من الناحية الوظيفية.
- آمنة من الناحية التقنية.
- قابلة للتوسع والصيانة.
- قابلة للترقية بين الإصدارات.
- قابلة للربط مع أنظمة خارجية.
- مناسبة للمؤسسات متعددة الشركات والمواقع والقنوات.
- متوافقة مع السياسات التنظيمية والحوكمة الداخلية.
**مصدر إضافي:** Odoo Developer + Security + Testing.

### 2.2 مبدأ التصميم
الـ Odoo لا يُبنى بشكل احترافي عبر "كتابة كود فقط"، بل عبر منظومة تشمل:
- تحليل الأعمال.
- تصميم البيانات.
- ضبط الأمن.
- تحسين الأداء.
- اختبار التوافق.
- التوثيق.
- المراقبة بعد الإطلاق.
- مواءمة الحل مع الحوكمة والـ ISO.
**مصدر إضافي:** Testing + System configuration + Developer docs.

---

## 3. دور المهارة داخل الفريق

### 3.1 دورها
هذه المهارة ليست مجرد Skill "فردي"، بل إطار عملي لبناء فريق كامل قادر على:
- تنفيذ مشاريع Odoo من البداية للنهاية.
- تقسيم المسؤوليات بوضوح.
- ضمان جودة التسليم.
- توحيد أسلوب العمل.
- تقليل المخاطر التقنية.
- دعم وضبط العمليات التشغيلية داخل الشركات.

### 3.2 كيف تُستخدم
- كمرجع توظيف.
- كمرجع تدريب.
- كمرجع مراجعة كود.
- كمرجع تصميم معماري.
- كمرجع تسليم مشاريع.
- كمرجع لحوكمة العمليات والاعتمادات والتصعيدات.
**مصدر إضافي:** Developer + Security.

---

## 4. هيكل الفريق

### 4.1 Solution Architect
**مسؤول عن:**
- فهم المتطلبات.
- رسم المعمارية العامة.
- تحديد حدود التخصيص.
- اختيار التكاملات المناسبة.
- وضع خطة الترقية والمخاطر.
- مواءمة الحل مع سياسات الشركة والحوكمة.
**مصدر إضافي:** Developer + Upgrade scripts.

### 4.2 Odoo Backend Developer
**مسؤول عن:**
- models.
- ORM.
- workflows.
- business rules.
- access logic.
- server actions.
- scheduled jobs.
- migration support.
**مصدر إضافي:** ORM + Testing.

### 4.3 Odoo Frontend Developer
**مسؤول عن:**
- OWL components.
- client actions.
- widgets.
- view customization.
- assets.
- responsive interface.
**مصدر إضافي:** Owl components + Tutorials.

### 4.4 Odoo Website/Portal Developer
**مسؤول عن:**
- website pages.
- themes.
- snippets.
- portal layouts.
- public components.
- customer experience.
**مصدر إضافي:** Owl on portal/website + Website docs.

### 4.5 API & Integration Developer
**مسؤول عن:**
- JSON-2.
- controllers.
- external systems.
- webhooks.
- sync jobs.
- authentication.
**مصدر إضافي:** External JSON-2 API + HTTP controllers.

### 4.6 Database / Performance Engineer
**مسؤول عن:**
- PostgreSQL.
- indexes.
- query plans.
- vacuum.
- monitoring.
- storage strategy.
**مصدر إضافي:** ORM + System configuration.

### 4.7 QA / Test Engineer
**مسؤول عن:**
- unit tests.
- integration tests.
- regression tests.
- UAT support.
- release validation.
**مصدر إضافي:** Testing Odoo.

### 4.8 Technical Lead
**مسؤول عن:**
- code review.
- technical decisions.
- standards.
- security.
- delivery readiness.
- mentoring.
**مصدر إضافي:** Developer + Testing + Security.

### 4.9 DevOps / Release Engineer
**مسؤول عن:**
- environments.
- deployments.
- backups.
- rollback.
- CI/CD.
- logs and observability.
- server hardening.
**مصدر إضافي:** System configuration + Testing.

### 4.10 Business Process Owner
**مسؤول عن:**
- تعريف سير العمل.
- اعتماد النماذج التشغيلية.
- تحديد نقاط الموافقة.
- تحديد الاستثناءات.
- مواءمة النظام مع سياسة الشركة.
- التأكد من توافق العمليات مع الحوكمة والـ ISO.
**مصدر إضافي:** Restrict access to data + Security.

### 4.11 Governance / Compliance Owner
**مسؤول عن:**
- ضبط السياسات.
- توثيق الإجراءات.
- التأكد من الفصل بين المهام.
- مراقبة الاعتمادات.
- متابعة التتبع والأثر التدقيقي.
- التأكد من أن الحل لا يكسر إجراءات المراجعة الداخلية.
**مصدر إضافي:** Security + System configuration.

---

## 5. المجالات التقنية الأساسية

### 5.1 Backend Development

#### ما يجب إتقانه
- ORM recordsets.
- relations.
- computed fields.
- constraints.
- inheritance.
- wizards.
- server actions.
- cron jobs.
- workflow methods.
**مصدر إضافي:** ORM API + Testing.

#### قواعد مهمة
- استخدم ORM بدل SQL متى أمكن.
- لا تعدل `self` مباشرة داخل `compute`.
- لا تعتمد على `onchange` كمنطق خادمي.
- استخدم `store=True` عند الحاجة للبحث أو التقارير.
- أضف `index=True` للحقول المفلترة بكثرة.
**مصدر إضافي:** ORM API + Security.

#### مثال مهني
```python
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProjectTask(models.Model):
    _name = 'project.task'
    _description = 'Task'

    name = fields.Char(required=True, index=True)
    amount = fields.Float()
    total = fields.Float(compute='_compute_total', store=True)

    @api.depends('amount')
    def _compute_total(self):
        for record in self:
            record.total = record.amount * 1.15

    @api.constrains('amount')
    def _check_amount(self):
        for record in self:
            if record.amount < 0:
                raise ValidationError(_('Amount cannot be negative'))
```
**مصدر إضافي:** ORM + Testing.

### 5.2 Frontend Development

#### ما يجب إتقانه
- OWL components.
- templates.
- services.
- state and props.
- registry.
- client actions.
- custom widgets.
**مصدر إضافي:** Owl components + Tutorials.

#### قواعد مهمة
- اجعل المكونات صغيرة وقابلة لإعادة الاستخدام.
- افصل البيانات عن العرض.
- استخدم `t-esc` بدل `t-raw` مع البيانات غير الموثوقة.
- اجعل التصميم متوافقاً مع RTL والجوال.
**مصدر إضافي:** Owl docs + Security.

#### OWL على الموقع والبوابة
يوضح طريقة استخدام Owl components على portal والـ website عبر `public_components` و `registry` و `web.assets_frontend` ووسوم `<owl-component>` في Odoo 19.
**مصدر إضافي:** Owl portal/website.

### 5.3 Website and Portal

#### Website
- صفحات تعريفية.
- صفحات خدمات.
- landing pages.
- forms.
- themes.
- snippets.
**مصدر إضافي:** Website docs + Tutorials.

#### Portal
- dashboard.
- orders.
- invoices.
- documents.
- tickets.
- profile.
- secure downloads.
**مصدر إضافي:** Owl on portal/website + Security.

#### قواعد مهمة
- عند صفحات العملاء استخدم portal layouts بدل website layouts.
- راعِ الصلاحيات والـ record rules.
- لا تُظهر بيانات حساسة إلا للمستخدم المخول.
- ابْنِ تجربة استخدام بسيطة وواضحة.
**مصدر إضافي:** Security + Restrict access to data.

### 5.4 APIs and Integration

#### النوع الحديث
يقدم Odoo 19 External JSON-2 API كواجهة HTTP حديثة عبر `/json/2/<model>/<method>` مع bearer API key، ويطبق access rights و record rules و field accesses بنفس نموذج الأمان الداخلي.
Reference: Odoo External JSON-2 API
**مصدر إضافي:** JSON-2 API + Security.

#### ما يجب إتقانه
- API keys.
- authentication.
- versioned endpoints.
- validation.
- pagination.
- error handling.
- idempotency.
- retries.
- webhooks.
- audit logs.
**مصدر إضافي:** JSON-2 API + HTTP controllers.

#### قواعد مهمة
- لا تكتب endpoints عامة بدون حماية.
- لا تعرض أكثر مما هو لازم.
- لا تعتمد على XML-RPC / old code إذا كان JSON-2 مناسباً.
- اجعل التكامل قابلاً للمراقبة والاسترداد.
**مصدر إضافي:** JSON-2 API + Security.

#### مثال JSON-2 API — Python
```python
import requests

BASE_URL = "https://mycompany.example.com/json/2"
API_KEY = "YOUR_API_KEY"
DATABASE = "mycompany"

headers = {
    "Authorization": f"bearer {API_KEY}",
    "X-Odoo-Database": DATABASE,
    "Content-Type": "application/json",
}

res = requests.post(
    f"{BASE_URL}/res.partner/search_read",
    headers=headers,
    json={
        "domain": [["is_company", "=", True]],
        "fields": ["name", "email", "phone"],
        "limit": 10,
        "order": "name asc",
    },
)
res.raise_for_status()
data = res.json()
```
**مصدر إضافي:** JSON-2 API.

#### مثال Controller — JSON API
```python
from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError

class ApiController(http.Controller):

    @http.route('/api/v1/partners', type='json', auth='user', csrf=False, methods=['POST'])
    def partners(self, domain=None, fields=None, limit=20):
        if not request.env.user.has_group('base.group_user'):
            raise AccessError("Not allowed")

        domain = domain or []
        fields = fields or ['name', 'email', 'phone']

        data = request.env['res.partner'].search_read(domain, fields, limit=limit)
        return {'success': True, 'count': len(data), 'data': data}
```
**مصدر إضافي:** HTTP Controllers + Security.

### 5.5 Database and Storage

#### ما يجب إتقانه
- PostgreSQL tuning.
- indexes.
- query plans.
- vacuum/autovacuum.
- locks and transactions.
- attachment storage.
- data retention.
**مصدر إضافي:** System configuration + ORM.

#### قواعد مهمة
- راقب الاستعلامات البطيئة.
- تجنب loops مع queries الداخلية.
- استخدم `search_read` و `read_group` عند الحاجة.
- لا تعتمد على raw SQL بشكل اعتباطي.
- عند وجود بيانات مكانية استخدم PostGIS.
**مصدر إضافي:** ORM + System configuration.

### 5.6 Reports

#### ما يجب إتقانه
- QWeb PDF.
- QWeb HTML.
- Excel exports.
- branded headers and footers.
- translations.
- multi-company layouts.
**مصدر إضافي:** Reports + Developer docs.

#### قواعد مهمة
- التقرير يجب أن يكون مفهوماً من أول مرة.
- لا تكدس البيانات دون ترتيب.
- حافظ على الاتساق البصري.
- راعِ طبيعة الطباعة والهوامش واللغة.
**مصدر إضافي:** Reports + Testing.

### 5.7 Automation

#### أدوات الأتمتة
- server actions.
- automated actions.
- cron jobs.
- scheduled sync.
- email workflows.
- marketing automation (عند الحاجة).
**مصدر إضافي:** Developer docs + Testing.

#### قواعد مهمة
- الأتمتة يجب أن تحل مشكلة حقيقية.
- لا تجعلها تخفي منطقاً معقداً لا يمكن تتبعه.
- كل automation يجب أن يكون له logging واضح.
**مصدر إضافي:** Testing + Security.

### 5.8 Security

#### ما يجب إتقانه
- ACL.
- groups.
- record rules.
- field-level access.
- safe controllers.
- safe rendering.
- safe attachments.
**مصدر إضافي:** Security + Restrict access to data.

#### خطوط حمراء
- SQL injection.
- XSS.
- CSRF.
- unsafe sudo.
- missing ACL.
- weak record rules.
- exposing sensitive records.
- bypassing ORM without reason.
**مصدر إضافي:** Security + System configuration.

تؤكد صراحة أن access rights و record rules اللتين تطبقان عبر ORM هما أساس التحكم.
**مصدر إضافي:** Security + Restrict access to data.

---

## 6. الخبرات البيزنس والورك فلو داخل الشركات

### 6.1 فهم العمليات الداخلية
يجب على الفريق فهم:
- دورة الطلب.
- دورة الشراء.
- دورة الاعتماد.
- دورة التوريد.
- دورة المخزون.
- دورة الفوترة.
- دورة التحصيل.
- دورة المشاريع.
- دورة الموارد البشرية.
- دورة خدمة العملاء.
- دورة الشكاوى والتصعيد.
- دورة الإغلاق والمراجعة.
**مصدر إضافي:** Restrict access to data + Developer docs.

### 6.2 تصميم الورك فلو
الورك فلو الناجح يجب أن يجيب على:
- من ينشئ الطلب؟
- من يراجعه؟
- من يعتمد؟
- متى ينتقل للحالة التالية؟
- ما الشروط؟
- ما الاستثناءات؟
- ما سجلات التدقيق؟
- ما آثار الرفض أو الإرجاع؟
**مصدر إضافي:** Security + Testing.

### 6.3 مستويات الاعتماد
- إنشاء.
- مراجعة.
- اعتماد أول.
- اعتماد ثانٍ.
- اعتماد استثنائي.
- تنفيذ.
- إغلاق.
- مراجعة لاحقة.
**مصدر إضافي:** Security + Developer docs.

### 6.4 فصل المهام
من منظور الحوكمة، يجب فصل:
- من يطلب.
- من يراجع.
- من يعتمد.
- من ينفذ.
- من يراجع التنفيذ.
- من يدقق لاحقاً.
**مصدر إضافي:** Restrict access to data + Security.

### 6.5 التتبع والأثر التدقيقي
كل عملية مهمة يجب أن تترك:
- who.
- what.
- when.
- before.
- after.
- reason.
- approval trail.
**مصدر إضافي:** Security + System configuration.

### 6.6 أمثلة تنظيمية

#### مقبول
- أمر شراء يمر بمراجعة ثم اعتماد ثم تنفيذ ثم إقفال.
- طلب خدمة يمر بتصنيف ثم اعتماد ثم تحويل ثم إغلاق.
**مصدر إضافي:** Security + Testing.

#### مفضل
- بناء حالات workflow واضحة.
- ربط كل انتقال بسبب وشروط.
- تسجيل مبررات الرفض والاستثناء.
**مصدر إضافي:** Security + Developer docs.

#### مرفوض
- تغيير حالة سجل بدون منطق اعتماد.
- تمرير الطلبات خارج السلسلة الإدارية.
- إلغاء أثر التدقيق.
**مصدر إضافي:** Security + Restrict access to data.

---

## 7. الحوكمة والمواءمة مع ISO

### 7.1 مبادئ عامة
الخبرة المطلوبة يجب أن تراعي:
- التوثيق.
- ضبط النسخ.
- الاعتمادات.
- التتبع.
- فصل المسؤوليات.
- إدارة المخاطر.
- تحسين مستمر.
- مراجعات دورية.
**مصدر إضافي:** Developer docs + Testing + Security.

### 7.2 متطلبات عملية
- كل عملية حرجة يجب أن تكون موثقة.
- كل استثناء يجب أن يسجل.
- كل تغيير يجب أن يكون قابلاً للمراجعة.
- كل اعتماد يجب أن يكون مرتبطاً بصاحب الصلاحية.
- كل تعديل مهم يجب أن يترك أثراً تدقيقياً.
- كل تكامل يجب أن يكون له owner و fallback.
**مصدر إضافي:** Security + System configuration.

### 7.3 ضوابط حوكمة
- عدم منح صلاحيات عامة بلا حاجة.
- عدم خلط الأدوار الحرجة.
- عدم تجاوز مراحل الموافقة.
- عدم تنفيذ عمليات حساسة دون trace.
- عدم الاعتماد على تعليمات شفهية غير موثقة.
**مصدر إضافي:** Security + Restrict access to data.

### 7.4 أمثلة

#### مفضل
```python
if not self.env.user.has_group('my_module.group_approver'):
    raise AccessError(_('You are not allowed to approve this document'))
```
**مصدر إضافي:** Security.

#### مقبول
```python
self.message_post(body=_('Approved by %s') % self.env.user.name)
```
**مصدر إضافي:** Developer docs + Security.

#### مرفوض
```python
self.sudo().write({'state': 'approved'})
```
**مصدر إضافي:** Security.

---

## 8. مستوى الخبرة المطلوب داخل الفريق

### 8.1 Junior
- فهم أساسيات Odoo.
- تنفيذ موديوﻻت بسيطة.
- تعديل views.
- استخدام ORM الأساسي.
**مصدر إضافي:** Tutorials + ORM.

### 8.2 Mid-Level
- بناء workflows.
- كتابة wizards.
- تطوير APIs.
- التعامل مع security basics.
- تنفيذ reports.
**مصدر إضافي:** Developer docs + Security + Reports.

### 8.3 Senior
- تصميم architecture.
- إدارة performance.
- OWL.
- portal and website.
- migrations.
- integration design.
- فهم business operations.
**مصدر إضافي:** OWL + Upgrade scripts + Developer docs.

### 8.4 Lead/Architect
- مراجعة code.
- اعتماد التصميم.
- إدارة المخاطر.
- توحيد standards.
- الإشراف على التسليم.
- مراجعة توافق الحل مع الحوكمة والـ ISO.
**مصدر إضافي:** Security + Testing + System configuration.

---

## 9. نظام العمل داخل الفريق

### 9.1 دورة المشروع
1. جمع المتطلبات.
2. تحليل الأعمال.
3. كتابة technical design.
4. تقسيم المهام.
5. التنفيذ.
6. مراجعة الكود.
7. الاختبار.
8. الأداء.
9. الأمان.
10. التوثيق.
11. النشر.
12. المراقبة بعد الإطلاق.
**مصدر إضافي:** Testing + System configuration + Developer docs.

### 9.2 آلية العمل
- كل feature لها owner.
- كل PR يراجع.
- كل release له checklist.
- كل تغيير كبير له test plan.
- كل integration له fallback plan.
- كل workflow critical له approval map.
**مصدر إضافي:** Testing + Security.

### 9.3 معايير التسليم
- code clean.
- docs جاهزة.
- tests ناجحة.
- security checked.
- performance checked.
- migration path defined.
- process approved.
- governance alignment confirmed.
**مصدر إضافي:** Testing + System configuration.

### 9.4 قاعدة صارمة للعمل
يجب عدم التنفيذ بعشوائية. إذا كان للحل أكثر من طريقة، يجب:
- شرح كل طريقة.
- توضيح المميزات.
- توضيح العيوب.
- توضيح التعارضات مع الموديولات الأخرى إن وجدت.
- توضيح أثر كل خيار على الأمان والأداء والترقية.
**مصدر إضافي:** Testing + Security + Upgrade scripts.

### 9.5 إدارة التحديات
أي تحدٍّ تقني أو تعارض وظيفي أو خطر تكاملي يجب:
- رفعه إلى GitHub أو نظام التتبع أولاً بأول.
- توثيقه.
- ربطه بالموديول أو الإصدار.
- عدم إخفائه داخل الكود أو تجاوزه بصمت.
**مصدر إضافي:** Testing + Developer docs.

---

## 10. الجودة والحوكمة التقنية

### 10.1 Code Review
- أسماء واضحة.
- منطق مقسّم.
- لا duplication.
- لا side effects خفية.
- لا bypass للصلاحيات.
- لا كسر لسلسلة الموافقات.
**مصدر إضافي:** Security + Testing.

### 10.2 Testing
- unit tests.
- integration tests.
- functional tests.
- portal tests.
- API tests.
- migration tests.
- workflow approval tests.
**مصدر إضافي:** Testing Odoo.

### 10.3 Documentation
- document module purpose.
- document models and fields.
- document endpoints.
- document rules.
- document deployment.
- document rollback.
- document business approvals.
**مصدر إضافي:** Developer docs + System configuration.

### 10.4 Observability
- logs.
- monitoring.
- alerts.
- error tracking.
- performance tracking.
- sync tracking.
- approval tracking.
- exception tracking.
**مصدر إضافي:** System configuration + Testing.

---

## 11. Website and Portal Engineering

### 11.1 Website Engineering
- themes.
- snippets.
- layouts.
- pages.
- SEO basics.
- assets.
- responsive behavior.
**مصدر إضافي:** Website docs + OWL.

### 11.2 Portal Engineering
- public_components.
- portal dashboards.
- secure visibility.
- customer documents.
- personalized views.
- safe downloads.
**مصدر إضافي:** Owl on portal/website + Security.

### 11.3 Portal example
```javascript
/** @odoo-module **/
import { Component, onMounted, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class GeoMapWidget extends Component {
    setup() {
        this.state = useState({
            loading: true,
            points: [],
        });
        onMounted(async () => {
            const res = await fetch("/api/v1/geo/points", {
                headers: { "Content-Type": "application/json" },
            });
            const data = await res.json();
            this.state.points = data.points || [];
            this.state.loading = false;
        });
    }
}
GeoMapWidget.template = "my_module.GeoMapWidget";
registry.category("public_components").add("my_module.GeoMapWidget", GeoMapWidget);
```
**مصدر إضافي:** Owl portal/website.

---

## 12. API Engineering

### 12.1 JSON-2 API
يقدم Odoo 19 External JSON-2 API كواجهة HTTP حديثة عبر `/json/2/<model>/<method>` مع bearer API key، وتوثيقه متاح في `/doc` حسب قاعدة البيانات.
Reference: Odoo External JSON-2 API
**مصدر إضافي:** JSON-2 API + Security.

### 12.2 Team Rules
- every endpoint versioned.
- every endpoint logged.
- every input validated.
- every output structured.
- every integration documented.
**مصدر إضافي:** JSON-2 API + Testing.

### 12.3 Security Rules
- API key rotation.
- least privilege.
- short-lived credentials where possible.
- separate keys per integration.
- error sanitization.
- rate limiting at gateway or application level.
**مصدر إضافي:** Security + System configuration.

### 12.4 JSON-2 example
```python
import requests

BASE_URL = "https://mycompany.example.com/json/2"
API_KEY = "YOUR_API_KEY"
DATABASE = "mycompany"

headers = {
    "Authorization": f"bearer {API_KEY}",
    "X-Odoo-Database": DATABASE,
    "Content-Type": "application/json",
}

res = requests.post(
    f"{BASE_URL}/res.partner/search_read",
    headers=headers,
    json={
        "domain": [["is_company", "=", True]],
        "fields": ["name", "email", "phone"],
        "limit": 10,
        "order": "name asc",
    },
)
res.raise_for_status()
data = res.json()
```
**مصدر إضافي:** JSON-2 API.

### 12.5 Controller example
```python
from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError

class ApiController(http.Controller):

    @http.route('/api/v1/partners', type='json', auth='user', csrf=False, methods=['POST'])
    def partners(self, domain=None, fields=None, limit=20):
        if not request.env.user.has_group('base.group_user'):
            raise AccessError("Not allowed")

        domain = domain or []
        fields = fields or ['name', 'email', 'phone']

        data = request.env['res.partner'].search_read(domain, fields, limit=limit)
        return {'success': True, 'count': len(data), 'data': data}
```
**مصدر إضافي:** HTTP Controllers + Security.

---

## 13. Database Governance

### 13.1 PostgreSQL
- tuning.
- indexes.
- autovacuum.
- locks.
- maintenance.
- bloat checks.
**مصدر إضافي:** System configuration + ORM.

### 13.2 Geospatial and Mapping
إذا كان المشروع يحتوي خرائط أو مواقع أو أصول هندسية، فالأفضل بناء طبقة مكانية عبر PostGIS وربطها من خلال Odoo ORM أو API أو تكامل مع QGIS أو ArcGIS أو AutoCAD حسب الحاجة.
**مصدر إضافي:** Developer docs + OCA geospatial ecosystem.

### 13.3 Data Governance
- retention.
- archiving.
- auditing.
- ownership.
- access classification.
**مصدر إضافي:** Security + System configuration.

---

## 14. GIS / CAD Integration

### 14.1 Scope
- ArcGIS.
- QGIS.
- PostGIS.
- AutoCAD.
- geolocation.
- spatial layers.
- map visualization.
- engineering data exchange.
**مصدر إضافي:** OCA geospatial + Odoo geolocation.

### 14.2 Recommended Architecture
- Odoo ORM for business entities.
- PostGIS for spatial storage.
- QGIS for analysis and editing.
- ArcGIS for enterprise mapping.
- AutoCAD for engineering drawings.
- API bridge for synchronization.
**مصدر إضافي:** OCA geospatial + Odoo docs.

### 14.3 ArcGIS references
- Reference: ArcGIS Maps SDK for JavaScript
- Reference: ArcGIS Get Started
- Reference: ArcGIS Sample Code
- Reference: ArcGIS References

### 14.4 OCA GIS references
- Reference: OCA/geospatial
- Reference: Leaflet Map View (OpenStreetMap)

### 14.5 ArcGIS integration example
```javascript
import Map from "@arcgis/core/Map";
import MapView from "@arcgis/core/views/MapView";
import FeatureLayer from "@arcgis/core/layers/FeatureLayer";

const map = new Map({
    basemap: "streets-vector",
});

const view = new MapView({
    container: "viewDiv",
    map,
    center: [46.6753, 24.7136],
    zoom: 11,
});

const layer = new FeatureLayer({
    url: "https://services.arcgis.com/your_service_url",
});

map.add(layer);
```
**مصدر إضافي:** ArcGIS Maps SDK + References.

### 14.6 Odoo + ArcGIS pattern
```python
from odoo import models, fields

class GeoAsset(models.Model):
    _name = 'geo.asset'
    _description = 'Geo Asset'

    name = fields.Char(required=True)
    latitude = fields.Float()
    longitude = fields.Float()
    arcgis_object_id = fields.Char(index=True)
    address = fields.Char()

    def action_push_to_arcgis(self):
        for rec in self:
            payload = {
                "name": rec.name,
                "latitude": rec.latitude,
                "longitude": rec.longitude,
                "address": rec.address,
            }
            # requests.post(ARC_GIS_URL, json=payload, headers=...)
```
**مصدر إضافي:** ArcGIS SDK + Odoo docs.

---

## 15. Migration and Upgrades

### 15.1 Scope
- versioned migrations.
- upgrade scripts.
- data transformation.
- schema adjustments.
- compatibility checks.
- rollback planning.
**مصدر إضافي:** Upgrade scripts + Developer docs.

### 15.2 Team Rules
- every release needs upgrade notes.
- every breaking change needs migration mapping.
- every version bump needs smoke tests.
- every custom integration needs compatibility review.
**مصدر إضافي:** Upgrade scripts + Testing.

---

## 16. Allowed / Accepted / Preferred / Forbidden / Rejected

### 16.1 قاعدة عليا
هذه المهارة مخصصة فقط لكل ما يخدم Odoo مباشرة، وتشمل:
- Backend.
- Frontend.
- Website.
- Portal.
- APIs.
- Reports.
- Database.
- Automation.
- Security.
- Integration.
- GIS/CAD عندما يكون مرتبطاً بـ Odoo.
- Upgrade and migration.
- Business workflows and governance داخل الشركات.

لا يتم تحويل أي طلب خارج هذه الحدود ويجب عدم التوسع فيه، ويُرد عليه فقط بما يخدم Odoo مباشرة. ولا يُحوّل إلى شرح عام خارج النظام، ولا إلى تقنيات غير مرتبطة بالمنصة.
**مصدر إضافي:** Developer docs + Security.

### 16.2 Allowed
```python
partner = self.env['res.partner'].search([('active', '=', True)])
```
```python
@api.depends('amount')
def _compute_total(self):
    for record in self:
        record.total = record.amount * 1.15
```
```html
<t t-esc="record.name"/>
```
**مصدر إضافي:** ORM + Security.

### 16.3 Accepted
```python
def action_sync(self):
    self.sudo().write({'synced': True})
```
```python
self.env.cr.execute(
    "UPDATE my_table SET state = %s WHERE id = %s",
    ['done', record.id]
)
```
```html
<t t-raw="safe_html"/>
```
**مصدر إضافي:** Security + Developer docs.

### 16.4 Preferred
```python
records = self.env['sale.order'].search([('state', '=', 'sale')])
```
```python
orders = self.env['sale.order'].read_group(
    [('state', '=', 'sale')],
    ['partner_id', 'amount_total:sum'],
    ['partner_id']
)
```
```javascript
registry.category("public_components").add("my_module.Widget", Widget);
```
```html
<t t-esc="partner.name"/>
```
**مصدر إضافي:** ORM + Owl.

### 16.5 Forbidden
```python
self.env.cr.execute("SELECT * FROM res_partner")
```
```python
self.sudo().write(vals)
```
```html
<div t-raw="user_input"/>
```
```python
query = "DELETE FROM sale_order WHERE id = " + str(order_id)
self.env.cr.execute(query)
```
**مصدر إضافي:** Security + System configuration.

### 16.6 Rejected
```python
partners = self.env['res.partner'].sudo().search([])
```
```python
import os
os.system("rm -rf /tmp/test")
```
```html
<t t-raw="comment.body"/>
```
```python
self.env.cr.execute("UPDATE account_move SET paid = TRUE")
```
**مصدر إضافي:** Security + Testing.

---

## 17. قواعد لا يجوز تجاوزها

### 17.1 الأمن أولاً
- لا SQL injection.
- لا XSS.
- لا CSRF غير مضبوط.
- لا sudo عشوائي.
- لا فتح بيانات دون قواعد وصول.
**مصدر إضافي:** Security + System configuration.

### 17.2 Odoo أولاً
- استخدم ORM عندما يكون ممكناً.
- استخدم inheritance بدل تعديل core.
- استخدم ACLs و record rules.
- استخدم OWL بالطريقة الرسمية.
- استخدم controllers أو JSON-2 بشكل مؤمن.
**مصدر إضافي:** ORM + Security + Owl + JSON-2.

### 17.3 قابلية الصيانة
- لا تكتب حلولاً "تشتغل الآن" وتكسر الترقية.
- لا تُدخل منطقاً غامضاً.
- لا تضع business logic داخل view أو template.
- لا تبْنِ feature لا يمكن اختبارها.
**مصدر إضافي:** Testing + Upgrade scripts.

### 17.4 الالتزام بنطاق المهارة
عدم توسيعه داخل الملف أي موضوع لا يخدم Odoo مباشرة.
الملف يجب أن يبقى:
- مختصراً في نطاقه.
- عميقاً في Odoo.
- صارماً في حدوده.
- واضحاً في المسموح والممنوع.
**مصدر إضافي:** Developer docs + Security.

---

## 18. DevOps وتأمين السيرفرات

### 18.1 التشغيل الآمن
عند نشر Odoo في بيئة إنتاج، يجب:
- استخدام HTTPS دائماً.
- تشغيل Odoo خلف reverse proxy.
- منع الوصول غير المصرح لصفحات إدارة قواعد البيانات.
- استخدام كلمات مرور قوية وفريدة.
- تعطيل demo data في البيئات العامة.
- عند الحاجة `list_db = False` أو استخدام `db_filter`.
- جعل PostgreSQL user غير superuser.
- عمل نسخ احتياطي يومي للـ database والـ filestore.
- عزل العملاء أو البيئات عند تعدد المستفيدين.
**مصدر إضافي:** System configuration.

### 18.2 الممارسات التشغيلية
- تحديثات منتظمة.
- مراقبة workers والـ timeouts.
- ضبط حدود الذاكرة والـ CPU.
- حماية الـ filestore.
- مراقبة السجلات.
- اختبار الاستعادة من النسخ الاحتياطية.
- فصل dev/staging/prod.
**مصدر إضافي:** System configuration + Testing.

### 18.3 قواعد DevOps
- كل نشر يجب أن يكون قابلاً للتراجع.
- كل تغيير إنتاجي يجب أن يمر عبر staging.
- كل integration يجب أن يمتلك مراقبة.
- كل مهمة حرجة يجب أن تمتلك runbook.
- كل failure must be logged and triaged.
**مصدر إضافي:** System configuration + Testing.

---

## 19. API وArcGIS References

### 19.1 Odoo API References
- Odoo External JSON-2 API
- Odoo Web Controllers
- Odoo Security
- Owl on Portal/Website

### 19.2 ArcGIS References
- ArcGIS Maps SDK for JavaScript
- ArcGIS Get Started
- ArcGIS Sample Code
- ArcGIS References

### 19.3 OCA GIS References
- OCA/geospatial
- Leaflet Map View (OpenStreetMap)

### 19.4 Integration rule
أي قرار تقني في APIs أو الخرائط يجب ألا يُنفذ بعشوائية. إذا وُجد أكثر من أسلوب:
- اعرض كل أسلوب.
- وّضح المميزات.
- وّضح العيوب.
- وّضح التعارضات مع الموديولات الأخرى إن وجدت.
- وّضح أثره على الأمان والأداء والترقية.
- اختر ما يخدم Odoo بأقل مخاطرة وأعلى قابلية للصيانة.
**مصدر إضافي:** Testing + Security + Upgrade scripts + ArcGIS samples.

---

## 20. الخلاصة
الخبير ليس مجرد مجموعة مبرمجين، بل نظام عمل هندسي متكامل. هذا الملف يحدد كيف يبني فريق Odoo حلولاً قوية، آمنة، قابلة للصيانة، وقابلة للترقية عبر جميع الإصدارات المستهدفة، مع احترام الحوكمة والـ ISO والورك فلو الداخلي للشركات، والعمل المنظم، ورفع التحديات أولاً بأول، وعدم التنفيذ بعشوائية.
**مصدر إضافي:** Developer docs + Security + Testing + System configuration.

---

### المراجع والروابط الخارجيّة
1. [Odoo Security Documentation](https://www.odoo.com/documentation/19.0/developer/reference/backend/security.html)
2. [ArcGIS JS SDK Downloads & Archive](https://developers.arcgis.com/javascript/latest/sdk-downloads-and-archive/)
3. [OCA Geospatial Repository](https://github.com/OCA/geospatial)
4. [ArcGIS Downloads](https://developers.arcgis.com/javascript/latest/downloads/)
5. [ArcGIS References](https://developers.arcgis.com/javascript/latest/references/)
6. [OCA Geospatial README](https://github.com/OCA/geospatial/blob/16.0/README.md)
7. [Odoo Base GeoEngine App](https://apps.odoo.com/apps/modules/9.0/base_geoengine)
8. [OCA Geospatial Website](https://oca.github.io/geospatial/)
9. [ArcGIS Previous Versions](https://developers.arcgis.com/javascript/latest/downloads-and-previous-versions/)
10. [T-Core OCA Geospatial](https://github.com/t-core-one/oca-geospatial)
