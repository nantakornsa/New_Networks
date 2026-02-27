# Reframe Document
## โครงการ: New Network Technology

---

# 1. การทบทวนสถาปัตยกรรม (Architectural Review)

## 1.1 ภาพรวมของระบบ

โครงการ **New Network Technology** มีวัตถุประสงค์เพื่อออกแบบและพัฒนาโครงสร้างเครือข่ายรูปแบบใหม่
ที่มีความปลอดภัยสูง รองรับการขยายตัว และสามารถทำงานได้อย่างมีประสิทธิภาพ

ระบบถูกออกแบบให้รองรับ:
- โครงสร้างเครือข่ายแบบแบ่ง Segment
- การจัดการ VLAN
- Routing ระหว่างเครือข่าย
- ระบบรักษาความปลอดภัยหลายชั้น
- ความสามารถในการขยายระบบในอนาคต

สถาปัตยกรรมใช้แนวคิดแบบ Layered Architecture เพื่อให้จัดการและบำรุงรักษาได้ง่าย

---

## 1.2 โครงสร้างสถาปัตยกรรม

### 1) Core Network Layer
- Router
- Routing Protocol
- การกำหนดเส้นทางข้อมูล

### 2) Distribution / Access Layer
- Switch
- VLAN
- Subnetting
- IP Address Management

### 3) Security Layer
- Firewall
- Access Control List (ACL)
- Port Security
- การกำหนดสิทธิ์การเข้าถึง

### 4) Monitoring & Management Layer
- Network Monitoring Tools
- Log Management
- Traffic Analysis

---

## 1.3 หลักการออกแบบระบบ

- ความปลอดภัยเป็นอันดับแรก (Security First)
- รองรับการขยายตัว (Scalability)
- ความเสถียรของระบบ (Stability)
- โครงสร้างแบบแยกส่วน (Modular Design)
- ง่ายต่อการบำรุงรักษา (Maintainability)

---

# 2. การวิเคราะห์การนำไปพัฒนา (Implementation Analysis)

## 2.1 เครื่องมือและเทคโนโลยีที่ใช้

- Cisco Packet Tracer / GNS3
- Router และ Switch Configuration
- VLAN & Subnetting
- Static / Dynamic Routing
- ACL & Firewall Configuration
- Wireshark สำหรับวิเคราะห์ Packet

---

## 2.2 ขั้นตอนการพัฒนา

### Phase 1: เตรียมโครงสร้างพื้นฐาน
- ออกแบบ Topology
- วางแผน IP Address
- แบ่ง VLAN
- กำหนด Subnet

### Phase 2: ติดตั้ง Core Network
- ตั้งค่า Router
- ตั้งค่า Switch
- กำหนด Routing
- ทดสอบการเชื่อมต่อ

### Phase 3: เพิ่มระบบความปลอดภัย
- ตั้งค่า ACL
- กำหนด Firewall Rules
- เปิดใช้งาน Port Security
- ทดสอบการป้องกันการเข้าถึงที่ไม่ได้รับอนุญาต

### Phase 4: ทดสอบและปรับปรุง
- ทดสอบ Connectivity
- ทดสอบ Routing
- วิเคราะห์ Bandwidth
- ตรวจสอบ Latency และ Packet Loss

---

## 2.3 การวิเคราะห์ความเสี่ยง

| ความเสี่ยง | ผลกระทบ | แนวทางป้องกัน |
|------------|----------|----------------|
| Config ผิดพลาด | ระบบไม่ทำงาน | Backup Config ทุกครั้ง |
| IP Conflict | เครื่องเชื่อมต่อไม่ได้ | วางแผน IP อย่างเป็นระบบ |
| Routing Error | สื่อสารข้าม VLAN ไม่ได้ | ตรวจสอบ Routing Table |
| ตั้งค่า Security ผิด | ระบบไม่ปลอดภัย | ทดสอบ ACL ทุกครั้ง |

---

# 3. การกำหนดบทบาทหน้าที่ (Role Assignment)

## โครงสร้างทีมงาน

| รหัสนักศึกษา | ชื่อ | บทบาท | หน้าที่ |
|--------------|------|--------|---------|
| 673380086-8 | ภูริ ตั้งพงษ์ | Network Infrastructure Engineer | ออกแบบและตั้งค่า Router |
| 673380400-8 | ชินวัตร แสนเมือง | Switching & VLAN Specialist | ตั้งค่า VLAN และ Switch |
| 673380433-3 | เกียรติพงษ์ เผดิมศักดิ์ | Security Engineer | ดูแล ACL และ Firewall |
| 673380397-1 | ฉัดรนัย ไกรราช | Testing & Monitoring | ทดสอบระบบและวิเคราะห์ Packet |
| 673380085-0 | นันทกร แสวงจิตร | Project Manager & System Designer | วางแผนโครงการและออกแบบ Architecture |

---

## แนวทางการทำงาน

- ใช้ Agile Framework
- แบ่งการทำงานเป็น Sprint
- ประชุมติดตามความคืบหน้าทุกสัปดาห์
- ทบทวนและปรับปรุงหลังจบแต่ละ Sprint

---

# สรุป

เอกสาร Reframe นี้จัดทำขึ้นเพื่อทบทวนและวิเคราะห์:

- โครงสร้างสถาปัตยกรรมของระบบ
- ขั้นตอนการนำไปพัฒนา
- การแบ่งบทบาทหน้าที่ในทีม

เพื่อให้โครงการ **New Network Technology**
ดำเนินงานได้อย่างเป็นระบบ มีประสิทธิภาพ และสอดคล้องกับแผนงานที่กำหนดไว้
