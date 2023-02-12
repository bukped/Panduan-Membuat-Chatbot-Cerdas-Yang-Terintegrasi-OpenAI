# Kode ini menunjukkan bagaimana program menentukan event "on_message", yang akan dipanggil setiap kali ada pesan yang diterima oleh bot.
# Event ini didefinisikan menggunakan decorator "@client.event", yang menunjukkan bahwa event ini akan dipicu oleh objek "client" dari kelas "commands.Bot".
# Pertama, program memeriksa apakah pengirim pesan adalah bot sendiri dengan membandingkan "message.author" dengan objek "client.user". Jika ya, maka program akan kembali dan tidak melakukan apa-apa.
# Jika pesan bukan dari bot sendiri, program memeriksa apakah pesan diawali dengan "prepik". Jika ya, program memecah pesan menjadi beberapa bagian berdasarkan spasi dan menghapus bagian pertama (yaitu "prepik"). Bagian-bagian yang tersisa akan digabung kembali menjadi string satu dengan metode "join()".
# Kemudian, program memanggil metode "create()" dari objek "openai.Completion", dengan berbagai argument untuk menentukan konfigurasi model, seperti nama model ("text-davinci-003"), prompt (string hasil), suhu (0.9), jumlah token maksimum (1024), dan lain-lain.
# Akhirnya, program mengirimkan pilihan teks pertama dari objek "response.choices" menggunakan metode "send()" dari "message.channel". Ini menunjukkan bahwa program akan mengirimkan jawaban bot ke channel Discord yang sama dengan pesan yang diterima.

# Function OpenAI
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Tidak Menggunakan Prefix
    # if message.content.startswith(""):

    # Menggunakan Prefix
    if message.content.startswith(prepik):
        inputan = message.content.split()

    inputan.pop(0)

    hasil = " ".join(inputan)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=hasil,
        temperature=0.9,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    await message.channel.send(response.choices[0].text)
