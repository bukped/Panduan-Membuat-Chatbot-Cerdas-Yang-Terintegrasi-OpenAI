# kode menyimpan data token, Kode ini menunjukkan bagaimana program mengambil environment variables untuk digunakan dalam aplikasi.
# Pertama, variabel "openai.api_key" ditentukan dengan mengambil nilai dari environment variable "OPENAI" melalui fungsi "os.environ". Variabel ini akan digunakan sebagai kunci API untuk mengakses layanan OpenAI.
# Yang kedua, variabel "TokenDiscord" ditentukan dengan mengambil nilai dari environment variable "DISCORD". Variabel ini akan digunakan sebagai token Discord untuk mengidentifikasi aplikasi ketika terhubung dengan server Discord.

load_dotenv()
openai.api_key = os.environ['OPENAI']
TokenDiscord = os.environ['DISCORD']
