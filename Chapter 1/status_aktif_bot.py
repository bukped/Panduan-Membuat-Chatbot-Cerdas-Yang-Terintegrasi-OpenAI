# Kode ini menunjukkan bagaimana program menentukan event "on_ready", yang akan dipanggil ketika bot Discord sukses terhubung dengan server.
# Event ini didefinisikan menggunakan decorator "@client.event", yang menunjukkan bahwa event ini akan dipicu oleh objek "client" dari kelas "commands.Bot".
# Pada event "on_ready", metode "start()" pada objek "change_status" akan dipanggil. Ini akan memulai tugas yang didefinisikan dalam tugas tersebut, seperti mengubah status bot.
# Teks "Bot is online! as Pepper PEW PEW" akan dicetak pada output, menunjukkan bahwa bot sukses terhubung dengan server dan siap digunakan.

@client.event
async def on_ready():
    change_status.start()
    print(f'Bot is online! as Pepper PEW PEW')
