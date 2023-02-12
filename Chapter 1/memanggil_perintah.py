# Kode ini menunjukkan bagaimana program menentukan "intents" atau niat dari aplikasi Discord.
# Intents adalah tipe dari data yang dapat diterima dan dikirimkan oleh aplikasi Discord. Misalnya, aplikasi mungkin ingin menerima informasi tentang member yang sedang online, atau konten pesan yang diterima.
# Ketika aplikasi terhubung dengan server Discord, informasi intents ini akan digunakan untuk menentukan jenis data yang akan diterima dan dikirimkan.

intents = discord.Intents.all()
intents.presences = True
intents.message_content = True
