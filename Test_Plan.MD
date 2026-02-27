# 🧪 Test Plan – Aura-Link Communication Architecture

## 1. วัตถุประสงค์ (Objective)

เอกสารฉบับนี้จัดทำขึ้นเพื่อกำหนดแผนการทดสอบระบบ Aura-Link  
ซึ่งเป็นต้นแบบสถาปัตยกรรมการสื่อสารผ่านความคิดแบบเชิงแนวคิด (Mockup)

วัตถุประสงค์หลัก:
- ทดสอบตรรกะการจัดเส้นทาง (Routing Logic)
- ทดสอบระบบตรวจสอบความปลอดภัย (Firewall Validation)
- ทดสอบการไหลของข้อมูลระหว่าง Layer
- ตรวจสอบการจัดการกรณีขอบเขตและข้อผิดพลาด

---

## 2. ขอบเขตการทดสอบ (Scope)

การทดสอบครอบคลุมเฉพาะระดับ Simulation และ Mockup ได้แก่:

- Emotion Vector Processing
- Relationship-based Routing
- Firewall Verification
- Data Flow ระหว่าง Layer

ไม่ครอบคลุม:
- ฮาร์ดแวร์จริง (BCI)
- ระบบ Quantum จริง
- การเชื่อมต่อเครือข่ายจริง

---

## 3. ประเภทการทดสอบ (Test Types)

- Unit Testing
- Integration Testing
- Security Testing
- Boundary Testing
- Negative Testing
- Load Testing (เชิงจำลอง)

---

## 4. ตารางกรณีทดสอบ (Test Cases)

| Test ID | ประเภท | เงื่อนไข | ค่าทดสอบ | ผลลัพธ์ที่คาดหวัง |
|----------|----------|------------|------------|-------------------|
| TC-01 | Unit | ความสัมพันธ์สูง | tie_score = 0.85 | เลือก High-Speed Lane |
| TC-02 | Unit | ความสัมพันธ์ต่ำ | tie_score = 0.30 | เลือก Standard Lane |
| TC-03 | Boundary | ค่าเท่ากับเกณฑ์ | tie_score = 0.70 | เลือก High-Speed Lane |
| TC-04 | Negative | ค่าติดลบ | tie_score = -0.1 | แสดงข้อผิดพลาด |
| TC-05 | Negative | ค่าเกินช่วง | tie_score = 1.5 | แสดงข้อผิดพลาด |
| TC-06 | Security | Token ถูกต้อง | valid_token | อนุญาตส่งข้อมูล |
| TC-07 | Security | Token ไม่ถูกต้อง | invalid_token | ถูกบล็อกโดย Firewall |
| TC-08 | Integration | Data Flow ครบทุก Layer | input → output | ส่งข้อมูลสำเร็จ |
| TC-09 | Load | ส่งคำขอ 100 ครั้ง | 100 requests | ระบบยังตอบสนองได้ |
| TC-10 | Security Edge | ไม่มี Token | null | ถูกปฏิเสธการส่งข้อมูล |

---

## 5. เกณฑ์การผ่านการทดสอบ (Pass Criteria)

- Routing ทำงานถูกต้องไม่น้อยกว่า 95%
- Firewall บล็อกการเข้าถึงที่ไม่ถูกต้อง 100%
- ไม่มีการ crash เมื่อรับค่าผิดปกติ
- Data Flow ทำงานครบทุก Layer

---

## 6. ความเสี่ยงที่ต้องติดตาม (Risk Areas)

- การคำนวณ tie_score ผิดพลาด
- การข้ามขั้นตอน Firewall
- การไม่จัดการค่า Edge Case
- การทำงานผิดพลาดเมื่อรับคำขอจำนวนมาก

---

## 7. เครื่องมือที่ใช้ในการทดสอบ (Testing Tools)

- Python Simulation Script
- Manual Logic Verification
- Diagram Flow Analysis

---

## 8. สรุป

Test Plan นี้ครอบคลุมการตรวจสอบ:
- ตรรกะการจัดเส้นทางตามระดับความสัมพันธ์
- ความปลอดภัยของข้อมูลก่อนส่งออก
- ความถูกต้องของโครงสร้างแบบ Multi-layer
- การจัดการกรณีผิดพลาดและค่าขอบเขต

เอกสารนี้จัดทำเพื่อสนับสนุนการประเมินในระดับ System Design และ Software Architecture Prototype
