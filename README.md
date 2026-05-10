# AI PDF 文档问答助手

这是一个 `RAG` 入门项目。项目可以读取 `PDF` 文档内容，将文本切分成小块，通过本地相似度检索找到与用户问题相关的文档片段，然后调用大模型基于检索到的上下文回答问题。

## 功能

- 读取 `PDF` 文档文本
- 将长文本切分成带 `overlap` 的文本块
- 使用 `TF-IDF` 做本地相似度检索
- 根据用户问题检索相关文档片段
- 构造 `RAG Prompt`
- 调用大模型生成回答
- 当文档中没有答案时，提示没有找到相关信息
- 支持显示原始 `chunk index`，方便调试引用来源

## 技术栈

- `Python`
- `pypdf`
- `scikit-learn`
- `OpenAI API`
- `python-dotenv`

## 项目结构

```text
proj05-ai-pdf-qa-assistant/
├── main.py
├── config.py
├── pdf_loader.py
├── text_splitter.py
├── retriever.py
├── prompt_builder.py
├── llm_client.py
├── requirements.txt
├── .env
├── .gitignore
└── rag_chinese_practice.pdf
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置环境变量

在项目根目录新建 `.env` 文件：

```env
OPENAI_API_KEY=你的API_KEY
```

注意：不要把 `.env` 上传到 `GitHub`。

## 运行项目
```bash
python main.py
```
运行后输入问题，例如：

```text
这个项目的主要目标是什么？
```

退出程序：

```text
q
```

## 示例问题

```text
这个项目的主要目标是什么？
文本切块建议控制在多少中文字？
为什么不能每次都把整份 PDF 直接交给大模型？
如果文档中没有答案，AI 应该怎么回答？
这份文档的作者叫什么名字？
```

## 当前版本说明

当前版本是一个 RAG 入门 MVP，使用 TF-IDF 做本地相似度检索，还没有接入真正的 `Embedding` 向量模型和向量数据库。

后续可以升级为：

- 使用 `OpenAI Embedding`
- 接入 `FAISS` 或 `Chroma` 向量数据库
- 支持上传任意 `PDF`
- 做成 `Streamlit` 网页版
- 显示引用片段和页码
