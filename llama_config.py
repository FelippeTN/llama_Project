import llama_cpp

def llama_config():
    return llama_cpp.Llama(
                model_path=f"llms/meta-llama-3-8b-instruct.Q4_K.gguf",
                chat_format="llama-3",
                n_gpu_layers=-1, 
                seed=42, 
                n_ctx=8090, 
                max_new_tokens=8090,
                n_batch=2048,
                n_threads=8,
                n_threads_batch=8,
            )