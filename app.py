import streamlit as st
import random
import time
import socket

# ===================================================
# ส่วนที่ 1: คลาสการทำงาน (นำมาจากสถาปัตยกรรมเดิม)
# ===================================================
class WearableNeuralHeadset:
    def __init__(self, user_id, is_worn, has_consent):
        self.user_id = user_id
        self.is_worn_properly = is_worn
        self.kill_switch_active = False
        self.consent_given = has_consent

    def check_hardware_and_consent(self):
        if self.kill_switch_active:
            return False, "Hardware Kill Switch is ACTIVE."
        if not self.is_worn_properly:
            return False, "Headset not worn properly. Signal too weak."
        if not self.consent_given:
            return False, "Explicit Consent not given (PDPA/Neurorights)."
        return True, "Hardware OK & Consent Granted."

    def read_raw_signal(self):
        noise_level = random.uniform(0.1, 0.9)
        emotion_level = random.uniform(0, 1)
        raw_thought = f"RawEEG_Data_{random.randint(1000,9999)}"
        return noise_level, emotion_level, raw_thought

class SignalFilterAI:
    def filter_noise(self, noise_level, raw_thought):
        clean_thought = raw_thought.replace("RawEEG", "CleanIntent")
        return clean_thought

class IntentDecoder:
    def process(self, emotion_level, clean_thought):
        if emotion_level > 0.7:
            weight = "HIGH"
        elif emotion_level > 0.4:
            weight = "MEDIUM"
        else:
            weight = "LOW"
        intent_data = f"Intent_Extracted_[{clean_thought}]"
        return weight, intent_data

class RelationshipManager:
    def __init__(self):
        self.relationship_scores = {
            ("UserA", "UserB"): 0.9, # ครอบครัว
            ("UserA", "UserC"): 0.5, # เพื่อน
            ("UserA", "UserD"): 0.2  # คนแปลกหน้า
        }
    def get_score(self, sender, receiver):
        return self.relationship_scores.get((sender, receiver), 0)

class NeuralFirewall:
    def verify_and_anonymize(self, token, intent_data):
        if token != "VALID_TOKEN":
            return False, None
        anonymized_data = f"Encrypted({intent_data})"
        return True, anonymized_data

class QuantumRouter:
    def route(self, relationship_score, emotional_weight):
        if relationship_score >= 0.7 and emotional_weight == "HIGH":
            return "High-Speed Emotional Lane"
        elif relationship_score >= 0.4:
            return "Standard Secure Lane"
        else:
            return "Restricted Firewall Channel"

# ===================================================
# ส่วนที่ 2: การสร้างหน้า Web Interface ด้วย Streamlit
# ===================================================

st.set_page_config(page_title="Aura-Band Web Simulator", page_icon="🧠", layout="centered")

st.title("🧠 Aura-Band: Neural Communication Simulator")
st.markdown("ระบบจำลองการสื่อสารผ่านคลื่นสมองด้วยอุปกรณ์สวมใส่ (Wearable Headset)")

# แผงควบคุมด้านข้าง (Sidebar) สำหรับรับค่าจากผู้ใช้
st.sidebar.header("⚙️ System Configuration")
sender = st.sidebar.selectbox("Sender (ผู้ส่ง):", ["UserA"])
receiver = st.sidebar.selectbox("Receiver (ผู้รับ):", ["UserB (ครอบครัว)", "UserC (เพื่อน)", "UserD (คนแปลกหน้า)"])
# แปลงชื่อผู้รับให้ตรงกับ Database
receiver_id = receiver.split(" ")[0] 


st.sidebar.subheader("🌐 Network Configuration")
# สมมติว่า IP ของเครื่อง B คือ 192.168.1.5 (ต้องไปเช็กในเครื่อง B ด้วยคำสั่ง ipconfig / ifconfig)
receiver_ip = st.sidebar.text_input("IP Address ของเครื่องรับ:", "127.0.0.1") 
receiver_port = st.sidebar.number_input("Port:", value=8080)



st.sidebar.markdown("---")
st.sidebar.subheader("🛡️ Hardware & Ethics Check")
is_worn = st.sidebar.checkbox("สวมใส่อุปกรณ์ถูกต้อง (Hardware OK)", value=True)
has_consent = st.sidebar.checkbox("ให้ความยินยอมเปิดเผยข้อมูล (Explicit Consent)", value=True)
valid_token = st.sidebar.checkbox("ยืนยันตัวตนผ่าน (Valid Token)", value=True)

# ปุ่มกดเริ่มจำลอง
if st.button("🚀 Start Transmission", type="primary", use_container_width=True):
    token_str = "VALID_TOKEN" if valid_token else "INVALID"
    
    # เริ่มแสดงผลการทำงานทีละ Layer
    with st.status("Initializing Aura-Band System...", expanded=True) as status:
        
        # Initialize
        headset = WearableNeuralHeadset(sender, is_worn, has_consent)
        ai_filter = SignalFilterAI()
        decoder = IntentDecoder()
        relationship = RelationshipManager()
        firewall = NeuralFirewall()
        router = QuantumRouter()

        # [Layer 0]
        st.write("**[Layer 0] Checking Hardware & Consent...**")
        time.sleep(1)
        status_ok, msg = headset.check_hardware_and_consent()
        if not status_ok:
            st.error(f"❌ Session Terminated: {msg}")
            status.update(label="Transmission Failed", state="error", expanded=True)
            st.stop()
        st.success(f"✅ {msg}")

        # [Layer 1]
        st.write(f"**[Layer 1] Reading Surface EEG from {sender}...**")
        time.sleep(1)
        noise_level, emotion_level, raw_thought = headset.read_raw_signal()
        st.info(f"Raw Data: {raw_thought} | Noise Level: {noise_level:.2f}")
        
        if noise_level > 0.7:
            st.warning("⚠️ High Noise Detected: Filtering out muscle artifacts...")
            time.sleep(1)
        
        clean_thought = ai_filter.filter_noise(noise_level, raw_thought)
        st.success(f"✅ Signal Filtered: {clean_thought}")

        # [Layer 2]
        st.write("**[Layer 2] AI Semantic Decoder Processing...**")
        time.sleep(1)
        emotional_weight, intent_data = decoder.process(emotion_level, clean_thought)
        st.success(f"✅ Intent Extracted. Emotion Intensity: **{emotional_weight}**")

        # [Layer 3]
        st.write("**[Layer 3] Quantum-Inspired Routing...**")
        time.sleep(1)
        score = relationship.get_score(sender, receiver_id)
        lane = router.route(score, emotional_weight)
        st.success(f"✅ Routing Through: **{lane}** (Tie Score: {score})")

        # [Layer 4 & 5]
        st.write("**[Layer 4 & 5] Neural Firewall & Transmission...**")
        time.sleep(1)
        is_valid, anonymized_data = firewall.verify_and_anonymize(token_str, intent_data)
        
        if not is_valid:
            st.error("❌ Firewall Blocked: Invalid Token. Identity Spoofing Detected.")
            status.update(label="Blocked by Firewall", state="error", expanded=True)
            st.stop()

        st.success("✅ Data Anonymized and Encrypted.")
        
        # ---> เริ่มการทำงานของเครือข่ายของจริง <---
        st.write(f"📡 กำลังเชื่อมต่อผ่าน TCP/IP ไปยังเป้าหมาย: `{receiver_ip}:{receiver_port}`...")
        
        try:
            # สร้างตัวส่งสัญญาณ (TCP Client)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(3.0) # รอ 3 วินาที ถ้าไม่เจอให้ตัดจบ
            client_socket.connect((receiver_ip, receiver_port))
            
            # ส่งข้อมูลที่ถูกเข้ารหัสแล้ว
            client_socket.sendall(anonymized_data.encode('utf-8'))
            client_socket.close()
            
            st.success("✅ Neural Payload Delivered over Network!")
            status.update(label="Transmission Complete!", state="complete", expanded=False)
            
        except ConnectionRefusedError:
            st.error(f"❌ ไม่สามารถเชื่อมต่อเป้าหมายได้ (กรุณาตรวจสอบว่ารัน neural_receiver.py ที่เครื่อง {receiver_ip} หรือยัง)")
            status.update(label="Network Error", state="error", expanded=True)
            st.stop()
        except Exception as e:
            st.error(f"❌ เกิดข้อผิดพลาดของเครือข่าย: {e}")
            st.stop()
            
        time.sleep(1)
        
        status.update(label="Message Delivered Successfully!", state="complete", expanded=False)

    # สรุปผลลัพธ์สุดท้าย
    st.balloons()
    st.success(f"🎉 **Message Transmitted via Smartphone Edge Router**\n\n**Payload:** `{anonymized_data}`")