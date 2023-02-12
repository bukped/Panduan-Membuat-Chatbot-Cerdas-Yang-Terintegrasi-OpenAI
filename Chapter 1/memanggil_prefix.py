# Kode ini menunjukkan bagaimana program membuat objek "client" sebagai instance dari kelas "commands.Bot" dari library "discord.ext.commands".
# Objek "client" akan digunakan sebagai bot Discord yang akan menangani perintah dan tugas yang diberikan oleh pengguna.
# Argumen "command_prefix" ditentukan sebagai string kosong, yang mengindikasikan bahwa bot tidak memerlukan prefix untuk memicu perintah.
# Argumen "intents" menentukan intents yang telah didefinisikan sebelumnya dalam variabel "intents". Ini mengindikasikan jenis data yang akan diterima dan dikirimkan oleh bot

client = commands.Bot(command_prefix='', intents=intents)
