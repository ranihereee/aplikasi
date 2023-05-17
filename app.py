import streamlit as st
[theme]
primaryColor="#00fff2"
backgroundColor="#fd93fe"
secondaryBackgroundColor="#ece1ec"
textColor="#f5f5fb"
font="serif"

# Membuat menu taksbar
menu = ["perkenalan", "perhitungan", "penjelasan"]

# Menambahkan menu taksbar ke dalam tampilan Streamlit
choice = st.sidebar.selectbox("Navigation", menu)

# Menampilkan konten terkait dengan pilihan menu yang dipilih
if choice == "perkenalan":
	st.write("Ini adalah halaman kontak")
	st.title('ALAT KELOMPOK 7')
	st.title('digunakan untuk memudahkan kalian menghitung _PARTIKULAT SECARA ISOKINETIK_ :blue :sunglasses:')

	st.caption('Alat ini dibuat oleh anggota kelompok 7 yaitu Akbar Kurnia ramadhan,Deby marsha,Kurnia Aynun,Nathalia,dan muhammad fauzi untuk keperluan tugas mata kuliah logika pemrograman komputer.')

	st.caption('**alat ini masih dalam versi percobaan**')
	st.caption(':red[______________________________________________________________________________________________]')



	st.caption(':red[______________________________________________________________________________________________]')


elif choice == "perhitungan":
	st.header(':blue[APLIKASI PERHITUNGAN PARTIKULAT SECARA ISOKINETIK]')
	
	import math

	st.title('Perhitungan')

	d = st.number_input('Diameter Saluran Gas (m)', value=0.5, step=0.1)
	v = st.number_input('Kecepatan Gas (m/s)', value=10, step=1)
	rho = st.number_input('Densitas Gas (kg/m3)', value=1.2, step=0.1)
	c = st.number_input('Konsentrasi Partikel Dalam Gas (mg/m3)', value=100, step=10)

	A = math.pi/4 * d**2


	Q = A * v


	C = c / 1000000

	massa = Q * rho * C


	massa_total = Q * c / 1000


	efisiensi = (massa_total - massa) / massa_total * 100



	if st.button('Hitung'):
	    # Output hasil perhitungan
	    st.write(f"Laju Aliran Gas = {Q:.2f} m3/s")
	    st.write(f"Massa Debu yang Terbawa oleh Gas = {massa:.4f} kg atau {massa*1000:.2f} mg")
	    st.write(f"Massa Total Debu yang Terukur = {massa_total:.2f} mg")
	    st.write(f"Efisiensi Pengendapan Debu = {efisiensi:.2f}%")

else:
	st.title("Penjelasan Sampling Isokinetik")

	st.write("Hai semuanya! Apakah kalian pernah mendengar tentang sampling isokinetik? Ini adalah metode pengambilan sampel yang digunakan untuk mengukur laju aliran gas atau cairan pada suatu sistem.")

	st.write("Tapi, kenapa disebut isokinetik? Karena metode ini memastikan bahwa laju aliran gas atau cairan yang diambil adalah konstan dan sebanding dengan laju aliran aktual dalam sistem.")

	st.write("Untuk melakukan sampling isokinetik, kita perlu menggunakan peralatan yang disebut dengan sampler isokinetik. Peralatan ini bekerja dengan cara mengatur kecepatan aliran sampel yang diambil agar sama dengan kecepatan aliran aktual dalam sistem.")

	st.write("Dengan begitu, sampel yang diambil akan mewakili kondisi aliran aktual dalam sistem. Metode sampling isokinetik ini biasa digunakan dalam berbagai aplikasi seperti pengukuran emisi gas buang, evaluasi kualitas udara dalam ruangan, dan sebagainya.")

	st.write("Jadi, itu dia penjelasan singkat tentang sampling isokinetik. Semoga bermanfaat dan tentunya lucu! Terima kasih sudah membaca!")
