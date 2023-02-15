import openai
import openai_secret_manager
# Mengambil API key dari OpenAI
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("openai")

# Importing the OpenAI library

# Setting the API key
openai.api_key = secrets["api_key"]

# Membuat prompt untuk digenerate
prompt = (f"Q:What is the capital of France?")
# Menggunakan fungsi generate untuk menghasilkan teks
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
)
# Menampilkan teks yang dihasilkan
print(response["choices"][0]["text"])
