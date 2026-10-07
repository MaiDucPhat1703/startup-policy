# Website tra cứu 5 nghị quyết TP. Hồ Chí Minh

Bản xuất từ website ChatGPT Sites đã chỉnh ngày 07/10/2026, gồm NQ 59, 62, 63, 64 và 65/2026/NQ-HĐND. Website có 81 điều: NQ 59 có 9 điều; NQ 62 có 12 điều; NQ 63 có 4 điều nghị quyết và 28 điều quy định kèm theo; NQ 64 có 14 điều; NQ 65 có 14 điều.

## 1. Bạn nhận được gì?

| Đường dẫn | Công dụng |
|---|---|
| `docs/index.html` | Trang tổng quan |
| `docs/nq-59.html` đến `docs/nq-65.html` | Các trang nghị quyết 59, 62, 63, 64 và 65 |
| `docs/style.css` | Màu sắc, cỡ chữ, khoảng cách, bố cục điện thoại và máy tính |
| `docs/view.js` | Mở/thu gọn các điều, mở điều khi bấm mục lục, in trang |
| `docs/articles.json` | Nội dung điều và khoản đã tách cấu trúc |
| `docs/NQ*_2026_goc.pdf` | 5 PDF nghị quyết gốc |
| `docs/ho_so/` | 14 mẫu phụ lục: trang xem, PDF đối chiếu và Word chuyển soạn |
| `docs/Tat_ca_mau_Word.zip` | Gói tải tất cả mẫu Word |
| `sources/` | Văn bản trích xuất để đối chiếu và tái tạo trang |
| `scripts/redesign.py` | Công cụ Python tái tạo trang từ dữ liệu nguồn |
| `requirements.txt` | Thư viện chỉ dùng khi chạy công cụ tái tạo |

Website là HTML/CSS/JavaScript tĩnh. Không cần API key, máy chủ riêng, npm hoặc Node.js để chạy. HTML trong `docs/` là mã nguồn có thể chỉnh sửa trực tiếp, không phải mã bị nén.

Bản GitHub dùng đường dẫn tương đối và trang có đuôi `.html`, để chạy khi đặt dưới tên kho bất kỳ. Bản này độc lập với website ChatGPT Sites; chỉnh trên GitHub không tự cập nhật website ChatGPT Sites và ngược lại.

## 2. Giải nén và xem thử

1. Tải file `startup-policy-github.zip`.
2. Trên Windows, nhấn chuột phải → **Extract All / Giải nén tất cả**.
3. Mở thư mục `startup-policy-github` vừa giải nén.
4. Mở `docs`, nhấp đúp `index.html`. Trình duyệt sẽ hiển thị trang tổng quan.
5. Thử mở từng nghị quyết, chuyển giữa các điều, bấm mở PDF và tải mẫu Word.

Nếu trình duyệt hạn chế mở tài liệu từ ổ đĩa, hãy kiểm tra lại sau khi website chạy trên GitHub Pages.

## 3. Tạo kho trên GitHub

1. Truy cập https://github.com và đăng nhập. Nếu chưa có tài khoản, chọn **Sign up**.
2. Mở https://github.com/new.
3. Ở **Repository name**, nhập `startup-policy` (hoặc tên bạn muốn).
4. Ở **Description**, có thể nhập: `Tra cứu 5 nghị quyết về khoa học, công nghệ và đổi mới sáng tạo tại TP. Hồ Chí Minh`.
5. Nếu muốn dùng GitHub Pages với tài khoản GitHub Free, chọn **Public**. Kho Public cho phép người khác xem mã và các tài liệu bạn tải lên; website Pages là website công khai.
6. Bật **Add a README file** nếu có tùy chọn này để khởi tạo nhánh mặc định.
7. Nhấn **Create repository**.

Bạn chưa cần chọn License. Nếu muốn cho phép người khác tái sử dụng mã theo một giấy phép cụ thể, có thể bổ sung giấy phép sau.

## 4. Upload mã bằng trình duyệt — không cần dòng lệnh

1. Trong kho vừa tạo, ở tab **Code**, chọn **Add file → Upload files**.
2. Mở thư mục `startup-policy-github` đã giải nén trên máy.
3. Kéo các thư mục `docs`, `sources`, `scripts` cùng các file `README.md` và `requirements.txt` vào vùng upload trên GitHub. Giữ nguyên cấu trúc thư mục.
4. **Không upload nguyên file ZIP**. GitHub không tự giải nén file ZIP thành website.
5. **Không kéo thêm thư mục cha `startup-policy-github`** vào kho. Bạn cần nhìn thấy `docs` ngay ở cấp đầu tiên của kho.
6. Chờ các file được tải lên. Gói này dưới 100 file và từng file dưới 25 MiB, phù hợp upload qua trình duyệt.
7. Nhập thông điệp, ví dụ `Add startup policy website`.
8. Chọn lưu trực tiếp vào nhánh mặc định của kho mới, rồi nhấn **Commit changes** (hoặc nút xác nhận tương ứng).
9. Sau khi upload, kiểm tra trong kho có `docs/index.html`, `docs/style.css`, `docs/view.js` và thư mục `docs/ho_so`.

Nếu kéo thả thư mục không hoạt động, dùng Chrome/Edge trên máy tính hoặc GitHub Desktop. Việc chọn từng file bằng hộp thoại có thể làm mất cấu trúc thư mục nếu chọn không đúng.

File `.nojekyll` nằm trong `docs/` giúp phục vụ website tĩnh. Nếu file này không được upload, mở kho → Add file → Create new file, nhập đường dẫn `docs/.nojekyll`, có thể nhập một dòng `Static website`, rồi Commit changes.

## 5. Bật GitHub Pages

1. Trong kho, chọn **Settings**.
2. Ở thanh bên trái, chọn **Pages**.
3. Tại **Build and deployment → Source**, chọn **Deploy from a branch**.
4. Tại **Branch**, chọn nhánh mặc định bạn vừa upload (thường là `main`).
5. Ở lựa chọn thư mục bên cạnh, chọn **`/docs`**. Không chọn `/(root)` cho cấu trúc của gói này.
6. Nhấn **Save**.
7. Chờ GitHub hoàn tất xuất bản. Có thể xem tiến độ ở tab **Actions**.
8. Trở lại **Settings → Pages**, bấm **Visit site** khi đường dẫn xuất hiện.

Địa chỉ thường có dạng:

```text
https://TEN_TAI_KHOAN.github.io/startup-policy/
```

Trang NQ 63 sẽ có dạng:

```text
https://TEN_TAI_KHOAN.github.io/startup-policy/nq-63.html
```

Thay `TEN_TAI_KHOAN` bằng username GitHub của bạn và `startup-policy` bằng tên kho đã tạo. Đây là mẫu địa chỉ, chưa phải website đã được xuất bản từ tài khoản của bạn.

## 6. Cập nhật nội dung và giao diện sau này

### Cách đơn giản: sửa file trực tiếp

1. Vào kho → mở `docs` → chọn file cần sửa.
2. Bấm biểu tượng bút chì **Edit this file**.
3. Sửa nội dung, rồi chọn **Commit changes**.
4. GitHub Pages tự xuất bản lại khi thay đổi được lưu vào nhánh và thư mục đã cấu hình.

| Muốn sửa | File nên sửa |
|---|---|
| Tiêu đề hoặc nội dung trang tổng quan | `docs/index.html` |
| Nội dung của NQ 63 | `docs/nq-63.html` |
| Nội dung của nghị quyết khác | Trang `docs/nq-*.html` tương ứng |
| Màu nền, màu nút, font, cỡ chữ | `docs/style.css` |
| Hành vi mục lục, mở/thu gọn | `docs/view.js` |
| Thay PDF gốc | PDF tương ứng trong `docs/`, giữ tên hoặc sửa đường dẫn liên quan |

Bạn cũng có thể sửa trên máy bằng VS Code rồi upload lại đúng đường dẫn. Nếu thay mẫu Word riêng, cập nhật cả ZIP tổng hợp để hai bản tải không lệch nhau.

### Dữ liệu và công cụ tái tạo — chỉ dành cho người muốn sửa bằng Python

`articles.json` là bản dữ liệu xuất ra, không được trình duyệt dùng để tạo trang. Chỉ sửa JSON sẽ không làm nội dung HTML tự thay đổi.

Công cụ tái tạo đọc `sources/NQ*.txt`, tiêu đề in đậm trong PDF gốc và danh sách mẫu tại `sources/forms-*.html`. Nếu cần dùng, cài Python rồi chạy tại thư mục gốc:

```bash
python -m pip install -r requirements.txt
python scripts/redesign.py
```

Sau đó đưa các file thay đổi trong `docs/` lên GitHub. Công cụ đã được chạy kiểm tra trong bản xuất này. Công cụ tái tạo sẽ ghi đè các trang HTML nghị quyết và trang tổng quan; các chỉnh sửa HTML thủ công cần được chuyển vào công cụ trước khi chạy lại.

## 7. Lỗi thường gặp

| Hiện tượng | Cách xử lý |
|---|---|
| Website báo 404 | Kiểm tra Pages chọn đúng nhánh và `/docs`; kiểm tra `docs/index.html` nằm đúng vị trí; chờ lần xuất bản hoàn tất |
| Trang chỉ hiện README | Bạn đang mở kho mã trên `github.com`; mở đường dẫn **Visit site** trong Settings → Pages |
| Có chữ nhưng mất màu/bố cục | Kiểm tra `docs/style.css` đã upload; giữ nguyên đường dẫn tương đối |
| Bấm nghị quyết bị 404 | Dùng liên kết có đuôi `.html` trong bản xuất này; kiểm tra các file `nq-*.html` |
| PDF hoặc Word không mở | Upload đủ PDF và thư mục `docs/ho_so`; giữ nguyên chữ hoa/chữ thường trong tên file |
| Không thấy tùy chọn nhánh | Upload hoặc khởi tạo kho trước để nhánh tồn tại |
| Không thấy Pages hoặc không bật được | Kiểm tra quyền quản trị kho và gói tài khoản; GitHub Free hỗ trợ Pages từ kho Public |
| Sửa rồi vẫn thấy bản cũ | Đợi lần xuất bản hoàn tất trong Actions, rồi nhấn Ctrl + F5 |

## 8. Các tài liệu chính thức để tham khảo

- Upload file: https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository
- Cấu hình nguồn GitHub Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- GitHub Pages: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages

## 9. Nguyên tắc nội dung

Nội dung điều, khoản, điểm trích từ 5 PDF được cung cấp. Bố cục, số thứ tự và tô nổi bật là cách hiển thị; không tạo thêm thủ tục hay giấy tờ. Các cột bổ sung chưa có căn cứ riêng vẫn để trống. File Word là bản chuyển soạn mẫu phụ lục, PDF gốc dùng để đối chiếu.
