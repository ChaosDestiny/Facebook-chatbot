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

### File config.yml
Đây là nơi cấu hình cho NLU và cả Core, nơi chúng ta lựa chọn ngôn ngữ, model cần thiết.
```python
language: "en"

pipeline:
- name: "WhitespaceTokenizer"
- name: "RegexFeaturizer"
- name: "CRFEntityExtractor"
- name: "EntitySynonymMapper"
- name: "CountVectorsFeaturizer"
- name: "CountVectorsFeaturizer"
  analyzer: "char_wb"
  min_ngram: 1
  max_ngram: 5
- name: "EmbeddingIntentClassifier"
  batch_strategy: sequence
```
Vì ta xây dựng bộ dữ liệu từ vựng từ đầu nên việc sử dụng ngôn ngữ tiếng Anh (en) và tiếng Việt (vi) đều được. Pipeline là một quy trình hoàn chỉnh từ lựa chọn Tokenizer, Featurizer, Extractor đến Classiffer, giúp NLU bắt được các intent và entity từ hội thoại.
```python
policies:
  - name: MemoizationPolicy
  - name: KerasPolicy
  - name: MappingPolicy
  - name: FallbackPolicy
    nlu_threshold: 0.3
    core_threshold: 0.3
    fallback_action_name: "action_default_fallback"
```
Policies là các quy ước để Rasa_Core lựa chọn hành động tiếp theo dựa trên các entity và intent đã thu nhận được từ NLU. Chúng ta lần lượt khai báo cái Policy cần thiết. Ở đây, ta dùng một số policy như: MemoizationPolicy (quyết định message đầu ra dựa vào thông tin của những đoạn hội thoại trước đó), KerasPolicy (sử dụng mạng LSTM để tính xác suất đưa ra lựa chọn cho message tiếp theo), MappingPolicy(quyết định message dựa vào dữ liệu đã mapping) và trong trường hợp, việc tính xác suất đầu ra không thể vượt được ngưỡng mà FallbackPolicy đề ra, message trả ra sẽ là một action_default_fallback.

### File nlu.md
Đây là file data, gồm các câu nói của người dùng đã được gán nhãn intent và entity, dùng để train cho NLU. Data càng phong phú thì khả năng đáp ứng của chatbot càng cao.
### File 
