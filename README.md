Ini adalah hasil kode python dengan library Tkinter (GUI) untuk menghitung invers dengan metode kofaktor.
Program Invers Matriks Metode Kofaktor ini merupakan aplikasi berbasis Python yang dirancang untuk menghitung invers dari suatu matriks persegi menggunakan pendekatan matematis kofaktor (adjoint). Aplikasi ini dibuat sebagai media pembelajaran Aljabar Linear dengan tujuan membantu pengguna memahami konsep determinan, matriks kofaktor, adjoin, dan invers matriks secara terstruktur. Untuk meningkatkan kemudahan penggunaan, program dilengkapi dengan antarmuka grafis (Graphical User Interface) menggunakan library Tkinter sehingga pengguna tidak perlu berinteraksi langsung dengan terminal atau baris perintah.
Dalam penggunaannya, pengguna hanya perlu menentukan ukuran matriks (n × n) dan memasukkan elemen-elemen matriks ke dalam kolom input yang disediakan. Program kemudian memproses input tersebut dengan terlebih dahulu melakukan validasi untuk memastikan bahwa matriks yang dimasukkan berbentuk persegi dan memiliki determinan yang tidak sama dengan nol. Apabila determinan bernilai nol, program secara otomatis memberikan pemberitahuan bahwa matriks tidak memiliki invers. Jika validasi terpenuhi, sistem akan menghitung determinan matriks, menyusun matriks kofaktor, melakukan transpose untuk memperoleh adjoin, dan selanjutnya membagi adjoin dengan determinan sesuai dengan rumus invers matriks.

Seluruh perhitungan numerik dalam program ini menggunakan tipe data float agar operasi matematika seperti perkalian dan pembagian dapat dilakukan secara akurat, mengingat hasil invers matriks pada umumnya berupa bilangan desimal. Hasil akhir perhitungan invers ditampilkan langsung pada antarmuka grafis dalam format yang rapi sehingga mudah dibaca dan dipahami oleh pengguna. Selain itu, program juga dilengkapi dengan mekanisme penanganan kesalahan yang akan menampilkan pesan peringatan apabila terjadi kesalahan input, seperti jumlah baris dan kolom yang tidak sesuai atau input yang bukan berupa angka.

Program ini bersifat lintas platform dan dapat dijalankan pada sistem operasi Windows, macOS, maupun Linux selama Python telah terpasang. Karena menggunakan metode kofaktor yang bersifat rekursif, aplikasi ini lebih ditujukan untuk matriks berukuran kecil hingga sedang dan sangat sesuai digunakan untuk keperluan pembelajaran, tugas kuliah, serta demonstrasi konsep invers matriks. Dengan adanya aplikasi ini, diharapkan pengguna dapat lebih mudah memahami proses perhitungan invers matriks secara konseptual sekaligus praktis melalui visualisasi antarmuka grafis yang sederhana dan interaktif.

Metode kofaktor tidak efisien untuk matriks berukuran besar (n > 4)
Program ini disarankan untuk:
- Pembelajaran
- Tugas kuliah
- Demonstrasi akademik

Pengembang MUHAMMAD HADI LESMANA & ANDINI TIA ANDITA 
