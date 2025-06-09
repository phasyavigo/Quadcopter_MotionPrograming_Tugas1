# Quadcopter_MotionPrograming_Tugas1

Proyek ini dibuat menggunakan ROS Noetic dengan simulasi TurtleSim untuk menggambar angka 0–9 berdasarkan input dari topik ROS. Node utama (`digit_drawer.py`) akan membaca pesan angka dari topik `/digit_input`, lalu menggambar angka tersebut di canvas TurtleSim menggunakan kombinasi gerakan maju dan rotasi. Input angka dikirim oleh node kedua (`digit_input_node.py`) yang berjalan secara interaktif lewat terminal. Kedua node ini berada di folder `scripts/`.

Fungsi `move_forward()` digunakan untuk menggerakkan turtle secara linear sejauh jarak tertentu. Durasi gerak dihitung dengan rumus `durasi = jarak / kecepatan`, sehingga meskipun kecepatan tetap, jarak bisa diatur dinamis. Sementara itu, fungsi `turn_degrees()` digunakan untuk memutar turtle sebesar sudut tertentu (dalam derajat), yang akan dikonversi ke radian. Setelah itu durasi rotasi dihitung dari `|radian| / kecepatan_angular`, sehingga hasil rotasi menjadi presisi dan sesuai parameter yang diberikan.

Proyek ini cocok untuk memahami penerapan ROS Publisher dan Service dalam mengendalikan gerakan robot sederhana secara modular. Setiap angka dipisahkan dalam fungsi masing-masing untuk mempermudah perawatan dan pengembangan.  
📹 [Demo Video](https://youtu.be/p24OWDacn6k)
