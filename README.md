<h1 align="center"><project-name>TF-IDF basic model</h1>
<p align="center"><project-description>Model guessing the topic of sentences - basic model</p>

## Contributor
- Main contributor
  - [Phạm An Đức Vinh](https://www.facebook.com/phamanducvinhuet/)
- Contributor
  - [Nguyễn Trần Đạt](https://www.facebook.com/trandat81)
  - [Nguyễn Đức Trọng](https://www.facebook.com/Virtuuuuuu)
  - [Đoàn Văn Nguyên](https://www.facebook.com/profile.php?id=100081785383189)

## Building Model
- Dataset
  - Bộ dữ liệu chia thành 2 phần dể train và để test
  - Dữ liệu training được lưu dưới dạng JSON như sau:
    - > [business.json](TF-IDF/dataset/Training/business.json): chứa documents có các chủ đề về kinh doanh
    - > [car.json](TF-IDF/dataset/Training/car.json): chứa documents có các chủ đề về xe
    - > [education.json](TF-IDF/dataset/Training/education.json): chứa các bài báo có nội dung về giáo dục 
    - > [health.json](TF-IDF/dataset/Training/health.json): chứa các bài báo có nội dung về sức khỏe 
    - > [law.json](TF-IDF/dataset/Training/law.json): chứa các bài báo có nội dung về pháp luật 
    - > [science.json](TF-IDF/dataset/Training/science.json): chứa các bài báo có nội dung về khoa học
    - > [sport.json](TF-IDF/dataset/Training/sport.json): chứa các bài báo có nội dung về thể thao
  - Cấu trúc json
    > { "category": string, "documents" : string[] }
    >
  - Phân tích dữ liệu
    - Để xây dựng mô hình TF-IDF để đoán topic của một câu thì ta cần quan tâm đến các từ vựng học thuật của câu đó
    chính vì thế với các văn bản ta nên quan tâm tới một số dạng từ không nên lấy hết toàn bộ từ, như động, danh từ, tính từ
    - Khi chích lọc được những từ vựng quan trọng của một văn bản ta lúc này mới thu được dữ liệu tốt để sử dụng
  - Tiền xử lý dữ liệu
    - Sử dụng thư viện [underthesea](https://github.com/undertheseanlp/underthesea) để cắt câu ra thành các từ có nghĩa và ta chỉ thu về những từ là danh từ, động từ và tính từ vì đa số nếu các từ mang tính học thuật sẽ thuộc 1 trong 3 loại từ này
    - Tiền xử lý dữ liệu được chạy trước để chuẩn bị data "sạch" cho mô hình TF-IDF
    - Chạy tiền xử lý để đưa data tốt vào các file JSON khác ở "data-prepare"
    > python tien-xu-ly.py
    - Package data-prepare chính là dữ liệu đã được xử lý, dữ liệu JSON có dạng
    > { documents : [ category: string , words : string[] ] }
  - Công thức [tf-idf](https://www.geeksforgeeks.org/understanding-tf-idf-term-frequency-inverse-document-frequency/)
    > Khi một câu văn được đưa vào ta cũng sẽ chỉ lấy các động từ, danh từ tính từ của câu văn đó tính trọng số TF-IDF của từng từ trong câu với dữ liệu đã được chuẩn bị sẵn
    sau đó với mỗi category ta tính tổng trọng số TF-IDF của các từ mới được đưa ra với mỗi văn bản trong category đó, category nào có tổng trọng số lớn nhất thì sẽ là kết quả
  - Thử nghiệm
    - [testing-1](https://docs.google.com/spreadsheets/d/1eeGrsX_XLJHz1rLSxBmw8h4FXjk6ube0UWePpnqUeIg/edit#gid=0)
    - [testing-2](https://docs.google.com/spreadsheets/d/1nV9zvpNsbIQwOtwsiHsYX4kD8384hIv-Mh8yvw5CSRI/edit#gid=0)
  - Nhận xét và bàn luận chung về mô hình
    - Mô hình cắt giảm quá nhiều bước còn đơn sơ, dữ liệu training còn ít, chạy chậm, nhưng vẫn cho ra tỷ lệ
    đúng đủ tốt (90% với những câu ngắn)
  
  - Update trong tương lai:
    - TF-IDF của từng từ nên được tính trước và lưu vào data thì khi truy vấn sẽ nhanh hơn
    - Sử dụng [Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/) để cho ra được kết quả tốt hơn tý lệ đúng sẽ cao hơn
  

