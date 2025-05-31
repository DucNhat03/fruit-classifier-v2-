from flask import Flask, render_template, request, jsonify, redirect, url_for, session, flash  # Nhập các module Flask cần thiết
import cv2  # Thư viện xử lý ảnh OpenCV
import numpy as np  # Thư viện tính toán số học
import joblib  # Dùng để load mô hình đã train
import os  # Thư viện thao tác với hệ thống file
import uuid  # Thêm thư viện uuid để tạo tên file ngẫu nhiên
import json
from datetime import datetime
from functools import wraps

app = Flask(__name__)  # Khởi tạo ứng dụng Flask
app.secret_key = 'fruit_vending_machine_key'  # Cần thiết cho session
UPLOAD_FOLDER = 'static/uploads'  # Thư mục lưu ảnh người dùng upload
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Cấu hình thư mục upload cho Flask

# Tạo thư mục upload nếu chưa tồn tại
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Tạo thư mục cho hóa đơn
RECEIPTS_FOLDER = 'static/receipts'
os.makedirs(RECEIPTS_FOLDER, exist_ok=True)

# Tạo thư mục cho cơ sở dữ liệu
DATA_FOLDER = 'data'
os.makedirs(DATA_FOLDER, exist_ok=True)

# File lưu trữ dữ liệu
PRODUCTS_FILE = os.path.join(DATA_FOLDER, 'products.json')
USERS_FILE = os.path.join(DATA_FOLDER, 'users.json')

# Khởi tạo dữ liệu mặc định
def init_data():
    # Khởi tạo sản phẩm mặc định
    if not os.path.exists(PRODUCTS_FILE) or os.path.getsize(PRODUCTS_FILE) == 0:
        default_products = {
            "Apple 5": {"name": "Apple 5", "price": 35000, "description": "Táo xanh tươi ngon", "stock": 100, "image": "apple5.jpg"},
            "Apple 6": {"name": "Apple 6", "price": 40000, "description": "Táo đỏ cao cấp", "stock": 80, "image": "apple6.jpg"},
            "Apricot 1": {"name": "Apricot 1", "price": 60000, "description": "Mơ tươi ngọt", "stock": 50, "image": "apricot1.jpg"},
            "Avocado 1": {"name": "Avocado 1", "price": 65000, "description": "Bơ chín mềm", "stock": 30, "image": "avocado1.jpg"},
            "Banana 1": {"name": "Banana 1", "price": 30000, "description": "Chuối già thơm ngon", "stock": 120, "image": "banana1.jpg"},
            "Blackberrie 1": {"name": "Blackberrie 1", "price": 120000, "description": "Dâu đen tím", "stock": 25, "image": "blackberry1.jpg"},
            "Blueberry 1": {"name": "Blueberry 1", "price": 150000, "description": "Việt quất nhập khẩu", "stock": 20, "image": "blueberry1.jpg"},
            "Carrot 1": {"name": "Carrot 1", "price": 25000, "description": "Cà rót tươi", "stock": 90, "image": "carrot1.jpg"},
            "Cherry 1": {"name": "Cherry 1", "price": 250000, "description": "Cherry đỏ cao cấp", "stock": 15, "image": "cherry1.jpg"},
            "Lemon 1": {"name": "Lemon 1", "price": 45000, "description": "Chanh vàng chua", "stock": 60, "image": "lemon1.jpg"},
            "Lychee 1": {"name": "Lychee 1", "price": 85000, "description": "Vải thiều Việt Nam", "stock": 40, "image": "lychee1.jpg"},
            "Strawberry 1": {"name": "Strawberry 1", "price": 180000, "description": "Dâu tây Đà Lạt", "stock": 35, "image": "strawberry1.jpg"},
            "Strawberry Wedge 1": {"name": "Strawberry Wedge 1", "price": 190000, "description": "Dâu tây cắt lát", "stock": 30, "image": "strawberry_wedge1.jpg"},
            "Tomato 1": {"name": "Tomato 1", "price": 35000, "description": "Cà chua bi", "stock": 80, "image": "tomato1.jpg"},
            "Watermelon 1": {"name": "Watermelon 1", "price": 20000, "description": "Dưa hấu đỏ", "stock": 50, "image": "watermelon1.jpg"}
        }
        with open(PRODUCTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_products, f, ensure_ascii=False, indent=2)
    
    # Khởi tạo người dùng mặc định
    if not os.path.exists(USERS_FILE) or os.path.getsize(USERS_FILE) == 0:
        default_users = {
            "admin": {
                "username": "admin",
                "password": "admin123",
                "role": "admin",
                "full_name": "Administrator"
            },
            "user": {
                "username": "user",
                "password": "user123",
                "role": "user",
                "full_name": "Customer"
            }
        }
        with open(USERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_users, f, ensure_ascii=False, indent=2)

# Khởi tạo dữ liệu khi start app
init_data()

# Hàm helper để đọc/ghi dữ liệu
def load_products():
    try:
        with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_products(products):
    with open(PRODUCTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=2)

def load_users():
    try:
        with open(USERS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USERS_FILE, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

# Decorator cho việc xác thực
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Vui lòng đăng nhập để tiếp tục', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or session.get('role') != 'admin':
            flash('Bạn không có quyền truy cập', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Load các mô hình và công cụ tiền xử lý đã lưu
rf_model = joblib.load("models/random_forest_model.pkl")  # Load mô hình Random Forest
svm_model = joblib.load("models/svm_model.pkl")  # Load mô hình SVM
scaler = joblib.load("models/scaler.pkl")  # Load đối tượng chuẩn hóa dữ liệu
pca = joblib.load("models/pca.pkl")  # Load mô hình giảm chiều PCA
id_to_label_dict = joblib.load("models/id_to_label_dict.pkl")  # Load từ điển ánh xạ ID -> nhãn

# Cơ sở dữ liệu giá trái cây (VND/kg)
fruit_prices = {
    "Apple 5": 35000,
    "Apple 6": 40000,
    "Apricot 1": 60000,
    "Avocado 1": 65000,
    "Banana 1": 30000,
    "Blackberrie 1": 120000,
    "Blueberry 1": 150000,
    "Carrot 1": 25000,
    "Cherry 1": 250000,
    "Lemon 1": 45000,
    "Lychee 1": 85000,
    "Strawberry 1": 180000,
    "Strawberry Wedge 1": 190000,
    "Tomato 1": 35000,
    "Watermelon 1": 20000
}

# Hàm tiền xử lý ảnh đầu vào
def preprocess_image(image_path):
    image = cv2.imread(image_path)  # Đọc ảnh từ đường dẫn
    image = cv2.resize(image, (45, 45))  # Resize ảnh về kích thước cố định (45x45)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Chuyển ảnh từ BGR sang RGB
    image_flat = image.flatten().reshape(1, -1)  # Chuyển ảnh thành vector hàng 1 chiều
    image_scaled = scaler.transform(image_flat)  # Chuẩn hóa vector ảnh
    image_pca = pca.transform(image_scaled)  # Giảm chiều ảnh bằng PCA
    return image_pca  # Trả về ảnh đã được xử lý

# Hàm tính độ tin cậy của dự đoán
def get_prediction_confidence(model, image_pca, pred_class):
    # Lấy xác suất dự đoán cho các lớp
    if hasattr(model, 'predict_proba'):
        proba = model.predict_proba(image_pca)[0]
        # Lấy chỉ số của lớp đã dự đoán
        class_idx = list(model.classes_).index(pred_class) if pred_class in model.classes_ else 0
        # Lấy xác suất của lớp đã dự đoán
        confidence = proba[class_idx] * 100
    else:
        # Nếu mô hình không hỗ trợ xác suất, trả về giá trị mặc định
        confidence = 85.0 if model == rf_model else 90.0
    
    return round(confidence, 1)

# Route đăng nhập
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        users = load_users()
        
        if username in users and users[username]['password'] == password:
            session['user_id'] = username
            session['role'] = users[username]['role']
            session['full_name'] = users[username]['full_name']
            flash(f'Chào mừng {users[username]["full_name"]}!', 'success')
            
            if users[username]['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng', 'error')
    
    return render_template('login.html')

# Route đăng xuất
@app.route("/logout")
def logout():
    session.clear()
    flash('Đã đăng xuất thành công', 'info')
    return redirect(url_for('index'))

# Route chính - chuyển hướng theo role
@app.route("/")
def index():
    if 'user_id' in session:
        if session.get('role') == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('user_dashboard'))
    return redirect(url_for('login'))

# Dashboard cho user
@app.route("/user_dashboard")
@login_required
def user_dashboard():
    if session.get('role') != 'user':
        return redirect(url_for('admin_dashboard'))
    
    products = load_products()
    return render_template('user_dashboard.html', products=products)

# Dashboard cho admin
@app.route("/admin_dashboard")
@admin_required
def admin_dashboard():
    products = load_products()
    return render_template('admin_dashboard.html', products=products)

# Route mua hàng cho user (không cần upload ảnh)
@app.route("/purchase/<product_id>", methods=["GET", "POST"])
@login_required
def purchase(product_id):
    products = load_products()
    
    if product_id not in products:
        flash('Sản phẩm không tồn tại', 'error')
        return redirect(url_for('user_dashboard'))
    
    product = products[product_id]
    
    if request.method == "POST":
        weight = float(request.form.get('weight', 1.0))
        
        if weight <= 0:
            flash('Số lượng không hợp lệ', 'error')
            return render_template('purchase.html', product=product, product_id=product_id)
        
        if product['stock'] < weight:
            flash('Không đủ hàng trong kho', 'error')
            return render_template('purchase.html', product=product, product_id=product_id)
        
        # Tính tổng tiền
        total_price = product['price'] * weight
        
        # Tạo hóa đơn
        receipt = {
            'product_id': product_id,
            'product_name': product['name'],
            'weight': weight,
            'price_per_kg': product['price'],
            'total_price': total_price,
            'customer': session['full_name'],
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'receipt_id': str(uuid.uuid4())[:8]
        }
        
        # Cập nhật tồn kho
        products[product_id]['stock'] -= weight
        save_products(products)
        
        # Lưu hóa đơn
        receipt_filename = f"{receipt['receipt_id']}.json"
        receipt_path = os.path.join(RECEIPTS_FOLDER, receipt_filename)
        with open(receipt_path, 'w', encoding='utf-8') as f:
            json.dump(receipt, f, ensure_ascii=False, indent=2)
        
        flash('Mua hàng thành công!', 'success')
        return render_template('receipt.html', receipt=receipt)
    
    return render_template('purchase.html', product=product, product_id=product_id)

# Route thêm sản phẩm (Admin)
@app.route("/admin/add_product", methods=["GET", "POST"])
@admin_required
def add_product():
    if request.method == "POST":
        product_id = request.form.get('product_id')
        name = request.form.get('name')
        price = float(request.form.get('price'))
        description = request.form.get('description')
        stock = float(request.form.get('stock'))
        image = request.form.get('image', 'default.jpg')
        
        products = load_products()
        
        if product_id in products:
            flash('ID sản phẩm đã tồn tại', 'error')
            return render_template('add_product.html')
        
        products[product_id] = {
            'name': name,
            'price': price,
            'description': description,
            'stock': stock,
            'image': image
        }
        
        save_products(products)
        flash('Thêm sản phẩm thành công!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('add_product.html')

# Route sửa sản phẩm (Admin)
@app.route("/admin/edit_product/<product_id>", methods=["GET", "POST"])
@admin_required
def edit_product(product_id):
    products = load_products()
    
    if product_id not in products:
        flash('Sản phẩm không tồn tại', 'error')
        return redirect(url_for('admin_dashboard'))
    
    if request.method == "POST":
        products[product_id]['name'] = request.form.get('name')
        products[product_id]['price'] = float(request.form.get('price'))
        products[product_id]['description'] = request.form.get('description')
        products[product_id]['stock'] = float(request.form.get('stock'))
        products[product_id]['image'] = request.form.get('image', 'default.jpg')
        
        save_products(products)
        flash('Cập nhật sản phẩm thành công!', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('edit_product.html', product=products[product_id], product_id=product_id)

# Route xóa sản phẩm (Admin)
@app.route("/admin/delete_product/<product_id>")
@admin_required
def delete_product(product_id):
    products = load_products()
    
    if product_id in products:
        del products[product_id]
        save_products(products)
        flash('Xóa sản phẩm thành công!', 'success')
    else:
        flash('Sản phẩm không tồn tại', 'error')
    
    return redirect(url_for('admin_dashboard'))

# Route xem lịch sử bán hàng (Admin)
@app.route("/admin/sales_history")
@admin_required
def sales_history():
    receipts = []
    for filename in os.listdir(RECEIPTS_FOLDER):
        if filename.endswith('.json'):
            with open(os.path.join(RECEIPTS_FOLDER, filename), 'r', encoding='utf-8') as f:
                receipt = json.load(f)
                receipts.append(receipt)
    
    # Sắp xếp theo thời gian gần nhất
    receipts.sort(key=lambda x: x['timestamp'], reverse=True)
    
    return render_template('sales_history.html', receipts=receipts)

# Route lịch sử mua hàng của user
@app.route("/purchase_history")
@login_required
def purchase_history():
    user_receipts = []
    for filename in os.listdir(RECEIPTS_FOLDER):
        if filename.endswith('.json'):
            with open(os.path.join(RECEIPTS_FOLDER, filename), 'r', encoding='utf-8') as f:
                receipt = json.load(f)
                if receipt.get('customer') == session['full_name']:
                    user_receipts.append(receipt)
    
    # Sắp xếp theo thời gian gần nhất
    user_receipts.sort(key=lambda x: x['timestamp'], reverse=True)
    
    return render_template('user_history.html', receipts=user_receipts)

# Route nhận diện trái cây bằng AI (cho admin hoặc demo)
@app.route("/ai_recognition", methods=["GET", "POST"])
@login_required
def ai_recognition():
    if request.method == "POST":  # Nếu người dùng gửi ảnh lên
        file = request.files["image"]  # Lấy file ảnh từ form
        if file:  # Kiểm tra có ảnh hay không
            # Tạo tên file ngẫu nhiên để tránh trùng lặp
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Tạo đường dẫn lưu ảnh
            file.save(filepath)  # Lưu ảnh vào thư mục upload

            image_pca = preprocess_image(filepath)  # Tiền xử lý ảnh

            rf_pred = rf_model.predict(image_pca)[0]  # Dự đoán với mô hình Random Forest
            svm_pred = svm_model.predict(image_pca)[0]  # Dự đoán với mô hình SVM

            # Lấy nhãn từ ID dự đoán và làm sạch tên
            rf_label = id_to_label_dict[rf_pred].split("\\")[-1]
            svm_label = id_to_label_dict[svm_pred].split("\\")[-1]

            # Tính độ tin cậy cho mỗi dự đoán
            rf_confidence = get_prediction_confidence(rf_model, image_pca, rf_pred)
            svm_confidence = get_prediction_confidence(svm_model, image_pca, svm_pred)
            
            # Sử dụng mô hình có độ tin cậy cao hơn
            final_label = rf_label if rf_confidence >= svm_confidence else svm_label
            final_confidence = max(rf_confidence, svm_confidence)
            
            # Lấy thông tin sản phẩm từ cơ sở dữ liệu
            products = load_products()
            product_info = products.get(final_label, None)

            # Trả kết quả về giao diện
            return render_template("ai_recognition.html", 
                                  rf_label=rf_label, 
                                  svm_label=svm_label,
                                  rf_confidence=rf_confidence,
                                  svm_confidence=svm_confidence,
                                  final_label=final_label,
                                  final_confidence=final_confidence,
                                  product_info=product_info,
                                  image_path=filepath)

    # Nếu truy cập lần đầu hoặc không upload ảnh
    return render_template("ai_recognition.html")

# Chạy ứng dụng Flask ở chế độ debug
if __name__ == "__main__":
    app.run(debug=True)