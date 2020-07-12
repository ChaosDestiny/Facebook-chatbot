# Facebook-chatbot
## Mục tiêu
Xây dựng một chatbot hỗ trợ việc nghe nhạc, đọc thơ, kể chuyện cổ tích và hỏi đáp thông tin cá nhân

## Công nghệ sử dụng
Sinh viên sử dụng Rasa Framework, một thư viện mã nguồn mở hỗ trợ xây dựng chatbot để thực hiện project này.
Thư viện mã nguồn mở Rasa là một nền tảng trí tuệ nhan tạo xử lý hội thoại theo ngữ cảnh (contextual conversations). 
Quản lý hội thoại nâng cao của Rasa dựa trên Machine Learning và cho phép các cuộc hội thoại thông minh hơn và giúp nhân rộng dễ dàng hơn. 
Rasa Là framework duy nhất cho phép Bot đối thoại tinh vi hơn, có tương tác, được train dựa trên supervised machine learning (học có giám sát).

Framework Rasa bao gồm:
* Rasa_NLU: công cụ giúp xử lý phân loại ý định (intent classification), thu thập phản hồi (respond retrieval) và bóc tách thực thể (entity extraction), nó sẽ giúp chatbot hiểu người dùng muốn gì và bắt được các thông tin chính trong đoạn hội thoại.
* Rasa_Core: công cụ giúp chatbot lựa chọn hành động/phản hồi lại người dùng. Nó dựa trên các kịch bản và lịch sử trò chuyện cùng các thuật toán Học máy để đưa ra phản hồi tốt nhất ứng với những thông tin đã bóc tách được nhờ NLU.
* Channels: công cụ kết nối chatbot với người dùng và với hệ thống backend

## Hướng dẫn cài đặt
Đầu tiên, ta cài đặt rasa về máy, phiên bản sử dụng ở project này là 1.7.0

`pip install rasa==1.7.0`

Sau đó di chuyển đến thư mục muốn khởi tạo Rasa và bắt đầu khởi tạo với dòng lệnh:

`rasa init`

Trong folder đó sẽ xuất hiện các file:
* data/nlu.md
* config.yml
* data/stories.md
* domain.yml
* action.py
* enpoints.yml
* credentials.yml

