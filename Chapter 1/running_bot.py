# Kode ini menunjukkan bagaimana program melakukan "run()" pada objek "client" dengan argument "TokenDiscord".
# Metode "run()" adalah metode yang dipanggil untuk menjalankan bot Discord. Argument "TokenDiscord" adalah token Discord yang digunakan untuk mengidentifikasi aplikasi dan memungkinkan akses ke API Discord. Token ini diambil dari variabel env yang diatur sebelumnya menggunakan perintah "os.environ['DISCORD']".
# Dengan demikian, kode ini menunjukkan bahwa program akan menjalankan bot Discord dengan menggunakan token yang diterima sebagai argument, Bot akan terhubung dengan server Discord dan siap menerima dan menanggapi pesan dari pengguna.


client.run(TokenDiscord)
