# Quadcopter_MotionPrograming_Tugas1

Proyek ini dibuat menggunakan ROS Noetic dengan simulasi TurtleSim untuk menggambar angka 0–9 berdasarkan input dari topik ROS. Node utama (`digit_drawer`) akan membaca pesan angka dari topik `/digit_input`, lalu menggambar angka tersebut di canvas TurtleSim menggunakan kombinasi gerakan maju dan rotasi. Input angka dikirim oleh node kedua (`digit_input_node`) yang berjalan secara interaktif lewat terminal.

Fungsi `move_forward()` digunakan untuk menggerakkan turtle lurus ke depan sejauh jarak tertentu. Fungsi ini menghitung durasi gerak berdasarkan kecepatan tetap, yaitu: `durasi = jarak / kecepatan`, sehingga gerakan selalu terkontrol sesuai parameter. Sementara itu, `turn_degrees()` bertugas memutar turtle sebanyak sudut tertentu (dalam derajat), dan dikonversi menjadi radian karena ROS menggunakan satuan tersebut. Kecepatan rotasi tetap digunakan agar konversi ke durasi rotasi dapat dihitung dengan akurat menggunakan: `durasi = |radian| / kecepatan_angular`.

Proyek ini cocok untuk memahami pemrosesan gerak linear dan rotasi di TurtleSim menggunakan ROS Publisher dan Service. Setiap angka memiliki pola gerakan tersendiri, dan pemisahan fungsi per angka dilakukan agar struktur kode modular dan mudah dikembangkan.  
📹 [Demo Video](https://youtu.be/p24OWDacn6k)
