sebelum anda menjalankan program di atas pastikan anda sudah menginstal Python dan Distribusi Python, yaitu Anaconda di komputer anda. Jika sudah, buat sebuah environment atau gunakan environment default di anaconda, lalu buka command prompt environment yang anda gunakan.
ketik "pip install ultralytics" di command prompt untuk menginstall library YOLO di Anaconda.
stelah proses instalasi selesai lalu pastikan command prompt anda berada di folder program deteksi-APD.
kemudian ketikkan perintah "yolo task=detect mode=predict conf=0.5 show=True model=DeteksiAPD.pt source=NamaVideo.mp4"
anda dapat menggunakan jenis file lain selain video pada bagian "source", seperti file gambar. jika anda ingin menggunakan webcam laptop anda untuk melakukan deteksi real time anda dapat mengubah nilai source dengan angka "0".
jika ada pertanyaan dapat menghubungi saya melalui email di tri.warisman@gmail.com

program ini bersifat open source dan anda dapat mengembangkannya untuk kepentingan individual ataupun komersil.
