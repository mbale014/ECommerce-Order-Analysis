# Judul Project
Data Engineering dan Analisis Perilaku Konsumen E-commerce Pesan Antar

## Repository Outline
1. SQL_Query.txt - File ini berisi URL dataset. Query SQL  (DDL dan DML) untuk pembuatan table dan melakukan insert data ke database.
2. Data_raw.csv - File ini berisi dataset original
3. Data_clean.csv - File ini berisi data yang telah dilakukan Data cleaning
4. DAG_airflow.py - File yang berisi DAG untuk dijalankan dengan menggunakan Apache Airflow
5. DAG_graph.jpg - Screenshot yang menampilkan alur graph dari DAG yang dibuat
6. conceptual_questions.txt - File ini berisi jawaban conceptual problem
7. Great_Expectations.ipynb - File ini berisi Expectations yang digunakan untuk melakukan validasi data
8. README.md - File ini berisi informasi tentang project kali ini
9. /images - Folder ini berisi daftar screenshot

## Problem Background
Di era modern saat ini, masyarakat di berbagai belahan dunia sudah banyak yg memilih platform online ecommerce sebagai sarana belanja online mereka. Aplikasi layanan pesan antar bahan makanan online seperti Swiggy, Zomato, Blinkit, dsb terus berlomba - lomba mencari ide dan kreatifitas yg akan menuju ke profit maksimal. Hal ini menunjukkan bahwa untuk mencapai tujuan tersebut, perusahaan perlu mengerti apa saja yg konsumen inginkan seperti produk yg dibeli, waktu pembelian, dan bagaimana cara meningkatkan kepuasan konsumen.

## Project Output
Output project adalah report yg berisi karakteristik - karakteristik mengenai perilaku konsumen baik dari demografik konsumer hingga aspek penjualan dan produk

## Data
Dataset yang digunakan dalam proyek ini berasal dari **Kaggle.com** dan berisi:  
- **100 ribu baris data**  
- **11 fitur**, termasuk produk pembelian, lama pesan antar, dan rating layanan

## Method
Project ini mengenai analisis data e-commerce untuk memahami perilaku konsumen melalui pendekatan berbasis data. Metode yang digunakan meliputi:

- Data Cleaning: Menghapus data duplikat, handling missing value, dan memastikan konsistensi format data menggunakan Python dan library Pandas.
- Data Validation: Menggunakan Great Expectations untuk memvalidasi integritas dan kualitas data.
- Exploratory Data Analysis (EDA): Melakukan analisis statistik deskriptif dan visualisasi untuk mengidentifikasi pola, tren, dan anomali dalam perilaku konsumen.
- ETL Pipeline: Menggunakan Apache Airflow untuk mengotomatisasi proses ekstraksi, transformasi, dan loading data ke dalam database.
- Reporting: Menyusun laporan yang mencakup wawasan demografis, preferensi produk, waktu pembelian, dan rekomendasi untuk meningkatkan kepuasan konsumen dengan ElasticSearch + kibana.

## Stacks
- **Bahasa Pemrograman**: Python, SQL
- **Library**: Pandas, NumPy, Great Expectations
- **Deployment**: Apache Airflow , ElasticSearch dan kibana

## Hasil & Implementasi  
Hasil dari proyek ini adalah:

- Laporan Analisis: Berisi wawasan tentang demografi konsumen, produk yang paling diminati, waktu pemesanan puncak, dan faktor yang memengaruhi rating layanan, divisualisasikan melalui dashboard interaktif di Kibana.
- Rekomendasi Bisnis: Strategi untuk meningkatkan kepuasan konsumen, seperti optimalisasi waktu pengiriman dan penawaran produk yang sesuai dengan preferensi konsumen.
- Pipeline Otomatis: Proses ETL yang dijalankan melalui Apache Airflow untuk memastikan pembaruan data secara berkala ke Elasticsearch.
- Validasi Data: Dataset yang telah divalidasi untuk memastikan keandalan analisis.

Implementasi dari hasil ini dapat digunakan oleh perusahaan e-commerce untuk membuat keputusan berbasis data, seperti menyesuaikan strategi pemasaran, meningkatkan efisiensi pengiriman, dan personalisasi layanan, dengan memanfaatkan dashboard Kibana untuk pemantauan real-time.

## Reference
Kaggle Dataset: https://www.kaggle.com/datasets/logiccraftbyhimanshi/e-commerce-analytics-swiggy-zomato-blinkit     
Apache Airflow Documentation: https://airflow.apache.org/docs/      
Great Expectations Documentation: https://docs.greatexpectations.io/        
Pandas Documentation: https://pandas.pydata.org/docs/       
Elasticsearch Documentation: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html     
Kibana Documentation: https://www.elastic.co/guide/en/kibana/current/index.html     

---
