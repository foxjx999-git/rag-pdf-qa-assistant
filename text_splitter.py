def split_text(text,chunk_size):
    """
    把长文本按固定长度切成多个小块。
    """
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)

    return chunks

def split_text_with_overlap(text, chunk_size, overlap):
    if overlap >= chunk_size:
        raise ValueError("overlap 必须小于 chunk_size")
    
    step = chunk_size -overlap
    chunks=[]

    for i in range(0, len(text), step):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)
    return chunks