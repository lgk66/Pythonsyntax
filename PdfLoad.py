# java_interview_rag.py
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# 1. 加载PDF（用绝对路径！）
loader = PyPDFLoader(r"D:\全部文件\资料\面试题\（备份）最新面试总结3.29.pdf")
docs = loader.load()

# 2. 智能分块（保留题目-答案结构）
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=60,
    # 特别处理“问：xxx？答：xxx”的格式
    separators=["\n\n", "。", "？", "\n", "问：", "答：", "1.", "2.", "3."]
)
splits = text_splitter.split_documents(docs)

# 3. 存入向量库
embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url="http://127.0.0.1:11434")

# 尝试多种向量存储方案
vectorstore = None

# 方案1：尝试FAISS
try:
    from langchain_community.vectorstores import FAISS
    vectorstore = FAISS.from_documents(splits, embeddings)
    vectorstore.save_local("./java_vector_db")
    print("✅ 成功使用FAISS向量数据库")
except Exception as e:
    print(f"⚠️ FAISS不可用: {e}")
    
# 方案2：尝试DocArray
if vectorstore is None:
    try:
        from langchain_community.vectorstores import DocArrayInMemorySearch
        vectorstore = DocArrayInMemorySearch.from_documents(splits, embeddings)
        print("✅ 成功使用DocArray内存存储")
    except Exception as e:
        print(f"⚠️ DocArray不可用: {e}")

# 方案3：使用最基础的内存存储（总是可用）
if vectorstore is None:
    try:
        from langchain_community.vectorstores import InMemoryVectorStore
        vectorstore = InMemoryVectorStore.from_documents(splits, embeddings)
        print("✅ 成功使用基础内存向量存储")
    except Exception as e:
        print(f"⚠️ 基础内存存储也不可用: {e}")
        # 最后的备选方案：手动实现简单的向量存储
        print("🔄 使用简易向量存储实现...")
        from langchain_core.documents import Document
        import numpy as np
        from sklearn.metrics.pairwise import cosine_similarity
        
        class SimpleVectorStore:
            def __init__(self):
                self.documents = []
                self.embeddings = []
                
            def add_documents(self, docs):
                for doc in docs:
                    # 获取文档嵌入
                    emb = embeddings.embed_query(doc.page_content)
                    self.documents.append(doc)
                    self.embeddings.append(emb)
                
            def similarity_search(self, query, k=4):
                if not self.embeddings:
                    return []
                
                # 获取查询嵌入
                query_emb = embeddings.embed_query(query)
                
                # 计算相似度
                similarities = cosine_similarity([query_emb], self.embeddings)[0]
                
                # 获取最相似的文档索引
                top_indices = np.argsort(similarities)[-k:][::-1]
                
                # 返回结果
                results = []
                for idx in top_indices:
                    if similarities[idx] > 0.1:  # 设置最小相似度阈值
                        results.append(self.documents[idx])
                
                return results[:k]
            
            def as_retriever(self):
                return SimpleRetriever(self)
        
        class SimpleRetriever:
            def __init__(self, vectorstore):
                self.vectorstore = vectorstore
            
            def get_relevant_documents(self, query):
                return self.vectorstore.similarity_search(query)
        
        vectorstore = SimpleVectorStore()
        vectorstore.add_documents(splits)
        print("✅ 成功使用简易向量存储")

# 5. RAG链
llm = OllamaLLM(model="qwen:4b", base_url="http://127.0.0.1:11434", temperature=0.1)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# 6. 测试问题
questions = [
    "Java基本数据类型？",
    "接口和抽象类的区别是什么？",
    "方法的重载和重写"
]

for q in questions:
    result = qa_chain.invoke(q)
    print(f"\n【问题】{q}")
    print(f"【答案】{result['result']}")
    print(f"【来源】{[doc.metadata['source'] for doc in result['source_documents']]}")