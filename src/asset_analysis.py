"""
Modul Analisis Operasional Aset Publik (Smart City Asset Analytics)
Terinspirasi dari Kuliah Praktisi Informatika - Widi Primadepa, S.T.
"""

import os
import pandas as pd

def load_data(filepath):
    """Fungsi untuk memuat dataset CSV pengaduan aset."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File dataset tidak ditemukan di: {filepath}")
    return pd.read_csv(filepath)

def analyze_asset_performance(df):
    """Melakukan analisis diagnostik rata-rata waktu penyelesaian perbaikan."""
    print("=" * 60)
    print(" 📈 LAPORAN ANALISIS DIAGNOSTIK KINERJA PEMELIHARAAN ASET ")
    print("=" * 60)

    # Menghitung rata-rata hari penyelesaian berdasarkan tingkat urgensi
    summary = df.groupby('urgency_level')['days_to_resolve'].mean().reset_index()
    summary.columns = ['Tingkat Urgensi', 'Rata-Rata Hari Penyelesaian']

    print("\nRata-Rata Waktu Penyelesaian per Urgensi:")
    print(summary.to_string(index=False))

    print("\nStatus Penyelesaian Berdasarkan Jenis Aset:")
    status_summary = pd.crosstab(df['asset_type'], df['status'])
    print(status_summary)
    print("=" * 60)

if __name__ == "__main__":
    # Path relatif menuju file dataset
    data_path = os.path.join(os.path.dirname(__file__), '../data/asset_reports.csv')

    # Eksekusi pipeline analitik
    df_reports = load_data(data_path)
    analyze_asset_performance(df_reports)