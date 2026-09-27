import streamlit as st
import joblib
import os
import numpy as np

# LOAD MODEL
def load_prediction_model(model_file):
    """Memuat model regresi yang sudah disimpan."""
    
    model = joblib.load(
        open(os.path.join(model_file), "rb")
    )
    
    return model

# PROGRAM UTAMA
def main():
    st.title("Prediksi Sales dari Biaya Iklan TV")
    header = """
    <div style="background-color:#726E6D;padding:10px;">
        <h3 style="color:white">
            Prediksi Sales Menggunakan Regresi Linear Sederhana
        </h3>
    </div>
    """

    st.markdown(header, unsafe_allow_html=True)
    menu = ["Prediksi Sales", "Apa itu Regresi?"]
    pilihan = st.sidebar.selectbox(
        "Menu",
        menu
    )

    # MENU 1: PREDIKSI SALES
    if pilihan == "Prediksi Sales":

        st.subheader(
            "Prediksi Sales Berdasarkan Biaya Iklan TV"
        )

        biaya_iklan_tv = st.number_input(
            "Masukkan biaya iklan TV (US$):",
            min_value=0.0,
            value=5.0,
            step=0.1
        )

        if st.button("Proses Prediksi"):
            model = load_prediction_model(
                "models/linear_regression_advertising.pkl"
            )

            # Mengubah input menjadi format array
            data_input = np.array(
                [[biaya_iklan_tv]]
            )

            # Melakukan prediksi
            hasil_prediksi = model.predict(
                data_input
            )

            # Mengambil hasil prediksi
            sales = float(
                hasil_prediksi[0][0]
            )

            # Konversi ke satuan sebenarnya
            biaya_dollar = biaya_iklan_tv * 1000
            jumlah_sales = sales * 1000

            st.success(
                f"""
                **Hasil Prediksi**

                Biaya iklan TV: **$ {biaya_dollar:,.2f}**

                Prediksi Sales: **{jumlah_sales:,.0f} unit**
                """
            )

    # MENU 2: INFORMASI REGRESI
    elif pilihan == "Apa itu Regresi?":

        st.subheader(
            "Apa itu Regresi Linear Sederhana?"
        )

        st.write(
            """
            Regresi linear sederhana merupakan metode statistik
            yang digunakan untuk memodelkan hubungan antara
            satu variabel bebas (X) dan satu variabel terikat (y).

            Pada aplikasi ini:

            • Variabel X = TV, yaitu biaya iklan TV.

            • Variabel y = Sales, yaitu jumlah penjualan.

            Model digunakan untuk memprediksi Sales berdasarkan
            biaya iklan TV yang dimasukkan oleh pengguna.
            """
        )

# MENJALANKAN PROGRAM
if __name__ == "__main__":
    main()