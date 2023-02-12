# Kode ini menunjukkan bagaimana program menentukan tugas yang dikenal sebagai "change_status". Tugas ini akan berulang setiap 20 detik, seperti yang ditentukan oleh decorator "@tasks.loop(seconds=20)".
# Variabel "status" adalah list yang berisi nama-nama status aktivitas bot Discord.
# Pada tugas "change_status", metode "change_presence" dari objek "client" akan dipanggil dengan argument "activity=discord.Game(choice(status))". Ini akan mengubah status aktivitas bot ke salah satu dari nama-nama status yang ditentukan dalam variabel "status", secara acak, menggunakan metode "choice()" dari module "random".
# Dengan demikian, setiap 20 detik, bot akan secara acak mengubah status aktivitasnya ke salah satu dari nama-nama status yang ditentukan.

status = ['Dahar', 'Modol', 'Tunduh', 'Mannasu', 'Manre',
          'Kobe Oser', 'Ayaine Mambri', 'Nawamar', 'Bolehh']


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))
