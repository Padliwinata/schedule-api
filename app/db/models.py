from typing import List
from pydantic import BaseModel
from datetime import time


class Sesi(BaseModel):
    kode: str
    hari: str
    jam_mulai: time
    jam_selesai: time


class Dosen(BaseModel):
    nama: str
    kesanggupan: List[str]


class Matkul(BaseModel):
    nama: str
    dosen: Dosen


class AsprakJadwal(BaseModel):
    kode: str
    matkul: List[str]
    kesanggupan: List[str]


class Asprak(AsprakJadwal):
    nama: str
    angkatan: str


class Jadwal(BaseModel):
    ruangan: str
    sesi: Sesi
    matkul: Matkul
    kelas: str
    asprak: AsprakJadwal
