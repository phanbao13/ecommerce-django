tao moi truong ao env de cai dat cac lib can thiet o requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic

1. create .env file

SECRET_KEY= django secret key
DATABASE_ENGINE=django.db.backends.mysql #database mysql
DATABASE_NAME=...
DATABASE_USER=...
DATABASE_PASSWORD=...
DATABASE_HOST=localhost
DATABASE_PORT=3306
TIME_ZONE=Asia/Ho_Chi_Minh
LANGUAGE_CODE=vi


EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='your_email@gmail.com'
EMAIL_HOST_PASSWORD='your email password'
EMAIL_PORT=587

2.
Mình tạo 1 tài khoản paypal trước. Sau đó bạn truy cập và đăng nhập vào trang <https://developer.paypal.com/>, vào tab này <https://developer.paypal.com/developer/accounts/> để tạo 2 tài khoản sandbox giả định. Mình tạo 1 tài khoản personal (người mua) và business (người bán) với thông tin sau:

Personal: có email <my.app.personal@gmail.com>.
Business: có email <my.app.business@gmail.com>
Cả 2 tài khoản mình đều để tiền là $9.999.999 và loại thẻ thanh toán là VISA. Sau khi mình tạo 2 tài khoản sandbox, mình có thể đăng nhập 2 tài khoản này vào trang <https://sandbox.paypal.com/> để kiểm tra số tiền hiện có.

Mình vào trang này <https://developer.paypal.com/developer/applications/> tạo 1 app mới có tên My Greatkart và tài khoản sandbox mình chọn là tài khoản sandbox business bên trên, app type mình giữ nguyên. Sau khi tạo xong, mình copy Client ID của app vừa tạo

Sau đó, mình tạo 1 nút thanh toán bằng paypal cho người dùng (có hướng dẫn chi tiết của trang chủ paypal <https://developer.paypal.com/docs/checkout/integrate/>). Mọi người có thể xem demo ở đây <https://developer.paypal.com/demo/checkout/#/pattern/client>

Mình import script của paypal vào file base.html. Lưu ý: Đối số client-id trong đường dẫn chính là Client ID mình vừa copy bên trên

<script src="https://www.paypal.com/sdk/js?client-id=...&currency=USD"></script>
