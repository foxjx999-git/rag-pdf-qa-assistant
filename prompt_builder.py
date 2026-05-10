def build_prompt(question, search_results):
    context = ""

    # 遍历 search_results
    # 把每个 result["text"] 拼到 context 里

    for i, result in enumerate(search_results):
        context += f"片段 {i + 1}：\n"
        context += f"原始 chunk index：{result['index']}\n"
        context += f"相似度 score：{round(result['score'], 4)}\n"
        context += "内容：\n"
        context += result["text"]
        context += "\n\n"

    prompt = f"""
你是一个 PDF 文档问答助手。
请只根据下面提供的文档内容回答问题。
如果文档内容中没有答案，请说：文档中没有找到相关信息。
不要编造文档中没有出现的信息。

回答要求：
1. 如果文档中列出了多个目标，请尽量完整列出。
2. 不要只回答其中一个点。
3. 回答最后必须写明引用来源，格式为：
引用来源：原始 chunk index = xxx
不要只写“片段 1”或“片段 2”。

文档内容：
{context}

用户问题：
{question}
"""

    return prompt