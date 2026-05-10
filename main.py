from pdf_loader import load_pdf_text

from text_splitter import split_text_with_overlap
from retriever import semantic_search
from prompt_builder import build_prompt
from llm_client import ask_llm

from config import PDF_PATH, CHUNK_SIZE, CHUNK_OVERLAP, TOP_K, MIN_SCORE, DEBUG


def main():
    text = load_pdf_text(PDF_PATH)

    chunks = split_text_with_overlap(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP)

    print("the pdf length is: ", len(text))
    print("chunk 数量：", len(chunks))

    while True:
        question = input("请输入你的问题，输入 q 退出：")
        question = question.strip()

        if not question:
            print("问题不能为空，请重新输入。")
            continue

        if question in ["q", "exit", "退出"]:
            print("程序已退出。")
            break

        results = semantic_search(chunks,question, top_k=TOP_K,min_score=MIN_SCORE)

        

        if DEBUG:
            print("\n===== 检索结果 DEBUG =====")

            for result in results:
                print("------")
                print("原始 chunk index:", result["index"])
                print("score:", round(result["score"], 4))
                print(result["text"][:200])

            print("===== DEBUG 结束 =====\n")

        if not results:
            print("AI 回答：")
            print("文档中没有找到相关信息。")
            continue

        prompt = build_prompt(question, results)

        prompt = build_prompt(question, results)

        answer = ask_llm(prompt)

        print("AI 回答：")
        print(answer)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: 
        print ("\n程序已中断，已退出。")
    
    except FileNotFoundError as e:
        print(e)
        print("请检查 config.py 里的 PDF_PATH 是否正确。")

    except ValueError as e:
        print(e)

    except RuntimeError as e:
        print(e)
        print("请检查 API Key、网络连接、模型名称或账户额度。")