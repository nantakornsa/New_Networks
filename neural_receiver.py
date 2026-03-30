import socket

# ==========================================
# Target Neural Router (เครื่องรับสัญญาณ)
# ==========================================

def start_neural_receiver(host='0.0.0.0', port=8080):
    # สร้าง Socket แบบ TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"🧠 [Target Neural Router] กำลังรอรับสัญญาณคลื่นสมองที่พอร์ต {port}...")
    
    while True:
        # รอการเชื่อมต่อจากผู้ส่ง
        client_connection, client_address = server_socket.accept()
        print(f"\n🔗 เชื่อมต่อสำเร็จ! รับสัญญาณจาก Edge Router: {client_address}")
        
        try:
            # รับข้อมูล (จำกัดที่ 1024 bytes)
            data = client_connection.recv(1024).decode('utf-8')
            if data:
                print(f"📥 สัญญาณที่ได้รับ (Encrypted): {data}")
                print("✅ แจ้งเตือน: กำลังจำลองภาพ/ความรู้สึกเข้าสู่สมองผู้รับ...")
            else:
                break
        finally:
            client_connection.close()

if __name__ == "__main__":
    start_neural_receiver()